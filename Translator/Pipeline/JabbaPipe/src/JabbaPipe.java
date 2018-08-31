import java.io.*;
import java.net.*;
import java.nio.file.Paths;
import java.sql.Date;
import java.text.SimpleDateFormat;
import java.util.Enumeration;
import java.util.Hashtable;
import java.util.StringTokenizer;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.LogRecord;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;

import org.apache.commons.cli.*;

/*
 * Multispeak Translator/Validator between version 3 and version 5 messages.
 * 
 * 												Jabba
 *							-----------------------------------------
 * Requester 				|    	  	  RequestForwarder			 |			Responder
 * 	(i.e, v3Request) ------>( mbInp )-----> =====v====== 			 |	(i.e., v5 Endpoint Server)
 * 		 NOT 200 OK  <------( mdErr )<-----|  Validate	|--->( mdFwd ) -----> v5Request ---|
 * 							|~~~~~~~~~~~~~~|     &  	|~~~~~~~~~~~~|					   |
 * 		  v3Response <------( mdFwd )<-----| Translate	|<---( mbInp )<----- v5Response <---
 * 		 NOT 200 OK  <------( mdErr )<----- =====^====== 			 |
 * 							|    	  	  ResponseForwarder			 |
 *							-----------------------------------------
 *
		class JabbaPipe {
			main(){
				open log, parse cmdline options
				new JSecureListen(8443);
				thePipelineServer = new PipelineServer(BIND_IP, LISTEN_PORT, FORWARD_IP, FORWARD_PORT);
				thePipelineServer.run("./xslt/ms_msg.xslt", "./xslt/ms_msg.xslt");
			}
			run( String xsltFile, String xmlData )
				URL[] saxload = { ... }
				TransformerFactory()
			}
		}

		class PipelineServer {
			run(String v3xsltFile, String v5xsltFile) {
				load V3 and V5 validator
				Socket requestSocket = m_ServerSocket.accept();
				connectionThread = new ConnectionHandlerThread(requestSocket, v3xsltFile, v5xsltFile, ...)
			}
		}

		class ConnectionHandlerThread extends Thread {
			public void run() {
				Connect to the destination server
				RequestForwarder = new ForwarderThread()
				ResponseForwarder = new ForwarderThread()
			}
		 }

		class ForwarderThread extends Thread {
			mfirstJV = GlobalStuff.getFirstValidator( mIsRequestForwarder );
			mlastJV  = GlobalStuff.getLastValidator( mIsRequestForwarder );
			public void run() {
				JabbaPipe mPipeline = new JabbaPipe();
				xmlInData = mbInp.read();
				mfirstJV.validate(xmlInData);
				xmlOutData = mPipeline.run(mXsltFile, xmlInData) // translate the message
				mlastJV.validate(xmlOutData);
				mdFwd.write(xmlOutData); // forward the message
			}
		}
 *
 */

class GlobalStuff {
	private static int m_dbgLevel = 0;
	private static int m_threadcnt = 2; // start at '2' since 'main' is Thread-1
	private static boolean m_wait = false;
	private static boolean m_consoleLog = false;
	private static boolean m_valid8 = true;
	private static boolean m_assumeV3 = true;
	private static boolean m_EmuV5Srvr = false;
	private static Logger logger;

	public static int m_TotalRequests = 0;
	public static int m_TotalResponses = 0;
	public static int m_TotalRequestsOk = 0;
	public static int m_TotalResponsesOk = 0;
	public static int m_RqstPostCheckFailed = 0;
	public static int m_RespPostCheckFailed = 0;
	public static int m_RqstValidateFailed = 0;
	public static int m_RespValidateFailed = 0;
	public static int m_RqstTranslateFailed = 0;
	public static int m_RespTranslateFailed = 0;
	public static int m_RespNotOkay = 0;
	
	public static JValid m_v3JV = null;
	public static JValid m_v5JV = null;
	
	public enum LogType {
	    OK_200, VALID8, XL8, POSTCHECK, NOT_OK, NO_VALID8
	}

	/*
	 * Actually, probably makes more sense to assume that requests are coming in as V5, since there are no
	 * DEVICES that talk V5 yet, so more likely that a Utility would be using V5 protocol but talking to 
	 * V3 devices... but, oh well.
	 */
	public static JValid getFirstValidator( boolean bIsRequester ) {
		if( bIsRequester ){
			if( m_assumeV3 )
				return m_v3JV;
			else
				return m_v5JV;
		}
		else{
			if( m_assumeV3 )
				return m_v5JV;
			else
				return m_v3JV;
		}
	}

	public static JValid getLastValidator( boolean bIsRequester ) {
		if( bIsRequester ){
			if( m_assumeV3 )
				return m_v5JV;
			else
				return m_v3JV;
		}
		else{
			if( m_assumeV3 )
				return m_v3JV;
			else
				return m_v5JV;
		}
	}
	
	public static boolean isValidPublicIp(InetAddress iNetAddr) {
		if (iNetAddr instanceof Inet6Address)
			System.out.println("Address is a V6 IP");
		return !(iNetAddr.isSiteLocalAddress() || iNetAddr.isAnyLocalAddress()
				|| iNetAddr.isLinkLocalAddress()
				|| iNetAddr.isLoopbackAddress() || iNetAddr
					.isMulticastAddress());
	}

	/*
	 * isSiteLocalAddress: For an Inet4Address, it checks to see if it's one of
	 * the RFC1918 "unrouteable" addresses: 10.0.0.0/8, 172.16.0.0/12,
	 * 192.168.0.0/16. For an Inet6Address, it checks the first two octets to
	 * see if it's a real "site local" address.
	 */
	public static InetAddress getAddress(String ipType) {
		try {
			int getPub = 0;
			if (ipType == "Public")
				getPub = 1;
			else if (ipType == "LoopBack")
				getPub = 2;

			Enumeration<NetworkInterface> eNI = NetworkInterface
					.getNetworkInterfaces();
			while (eNI.hasMoreElements()) {
				NetworkInterface NI = (NetworkInterface) eNI.nextElement();
				Enumeration<InetAddress> eNetAddr = NI.getInetAddresses();
				while (eNetAddr.hasMoreElements()) {
					InetAddress iNetAddr = (InetAddress) eNetAddr.nextElement();
					if (iNetAddr instanceof Inet6Address) {
						continue;
					} else if (iNetAddr instanceof Inet4Address) {
						// System.out.println("IPv4 Addr: " + iNetAddr.getHostAddress());
						;
					} else {
						System.out.println("What the ....?");
					}

					if (getPub == 1) {
						if (GlobalStuff.isValidPublicIp(iNetAddr)) {
							return iNetAddr;
						}
						if (iNetAddr.isSiteLocalAddress()) {
							return iNetAddr;
						}
					} else {
						if ((getPub == 2) && iNetAddr.isLoopbackAddress()) {
							return iNetAddr;
						} else if ((getPub == 0)
								&& iNetAddr.isSiteLocalAddress()) {
							return iNetAddr;
						}
					}
				}
			}
		} catch (SocketException e) {
			e.printStackTrace();
		}
		return null;
	}
	
	public static Logger getLogger() {
		return logger;
	}
	public static void setLogger(Logger var) {
		logger = var;
	}

	public static int getDebugLevel() {
		return m_dbgLevel;
	}
	public static void setDebugLevel(int var) {
		m_dbgLevel = var;
	}

	public static int getThreadCnt() {
		return m_threadcnt;
	}
	public static void setThreadCnt(int var) {
		m_threadcnt = var;
	}

	public static boolean getWait() {
		return m_wait;
	}
	public static void setWait(boolean val) {
		m_wait = val;
	}

	public static boolean Log2Console() {
		return m_consoleLog;
	}
	public static void Log2Console(boolean val) {
		m_consoleLog = val;
	}

	public static boolean assumeV3Requests() {
		return m_assumeV3;
	}
	public static void assumeV3Requests(boolean val) {
		m_assumeV3 = val;
	}

	public static boolean doValid8() {
		return m_valid8;
	}
	public static void doValid8(boolean val) {
		m_valid8 = val;
	}
	
	public static boolean EmuV5Srvr() {
		return m_EmuV5Srvr;
	}
	public static void EmuV5Srvr(boolean val) {
		m_EmuV5Srvr = val;
	}

	public final static void clearConsole() {
		try {
			final String os = System.getProperty("os.name");

			if (os.contains("Windows")) {
				Runtime.getRuntime().exec("cls");
			} else {
				Runtime.getRuntime().exec("clear");
			}
		} catch (final Exception e) {
			// Handle any exceptions.
		}
	}
}
/*
 * PATTERN = "yyyy-MM-dd'T'HH:mm:ss.SSSXXX"; will produce output like
 * this: 2016-08-19T17:43:14.295+09:00 INFO Hey
 *
 * The below, produces like: Mar 07, 2017 7:47:31 AM ForwarderThread UpdateLogStats Hey
 */
class JabbaFormatter extends SimpleFormatter {
	private static final String PATTERN = "yyyy-MM-dd HH:mm:ss";

	@Override
	public String format(final LogRecord record) {
		String str = String.format("%1$s", formatMessage(record));
		if( GlobalStuff.Log2Console() ){
			System.out.println(str);
		}
		return String.format("%1$s %2$-7s %3$s\n",
				new SimpleDateFormat(PATTERN).format(new Date(record
						.getMillis())), record.getLevel().getName(), str );
		/*return String.format("%1$s %2$-7s %3$s\n",
				new SimpleDateFormat(PATTERN).format(new Date(record
						.getMillis())), record.getLevel().getName(),
				formatMessage(record));*/
	}
}
class JabbaRuntimeException extends RuntimeException {
	private int status;
	private static final long serialVersionUID = -724970790805990517L;

	public JabbaRuntimeException(String message, int status) {
		super(message);
		this.status = status;
	}

	public JabbaRuntimeException(String message, int status, Throwable cause) {
		super(message, cause);
		this.status = status;
	}

	@Override
	public String toString() {
		return super.toString();
	}

	@Override
	public String getMessage() {
		return super.getMessage() + ", returning Http Status:" + status;
	}

	public int getStatus() {
		return status;
	}
}

public class JabbaPipe {

	public static void main(String[] args) throws Exception {
		String LOOP_BIND_IP = "127.0.0.1"; // The default IP address to bind to
										   // for listening for Request traffic
		String LOOP_DESTINATION_HOST = "127.0.0.1"; // IP address to forward
													// Response traffic to
		String DEF_BIND_IP = "0.0.0.0"; // The default IP address to bind to for
										// listening for Request traffic
		int LOOP_LISTEN_PORT = 7776;  	// The loopback port to listen on for Request traffic
		int LISTEN_PORT = 8080;   		// The port to listen on for Request traffic
		int FORWARD_PORT = 7777;   		// IP port to forward Request traffic to (only permit 21/22/443/80/8080)

		GlobalStuff.setLogger(Logger.getLogger("JabbaLog"));
		Logger logger = GlobalStuff.getLogger();
		FileHandler fh=null;

		try {
			// This block configure the logger with handler and formatter
			fh = new FileHandler("Jabba.log", true); // note: 'true' tells it to append
			logger.addHandler(fh);
			if( !GlobalStuff.Log2Console() )
				logger.setUseParentHandlers(false);
			
			// configure logger to print on one line
			System.setProperty("java.util.logging.SimpleFormatter.format",
					"%1$tF %1$tT %4$s %2$s %5$s%6$s%n");
			JabbaFormatter formatter = new JabbaFormatter();
			fh.setFormatter(formatter);
			
			// the following statement is used to log any messages
			logger.setLevel(Level.ALL);
			logger.info("\n ******* Jabba Started. *******");
			/*
			
			System.out.println("JAVA_HOME is: " + System.getenv("JAVA_HOME"));
			System.out.println("CLASSPATH is: " + System.getenv("CLASSPATH"));
			System.out.println("java.class.path is: " + System.getProperty("java.class.path"));
			System.out.println("CURR_WORKDIR is: " + System.getProperty("user.dir"));
			
			 * logger.severe( " ******* This is a severe message. *******");
			 * logger.warning(" ******* This is a warning message. *******");
			 * logger.config( " ******* This is a config message. *******");
			 * logger.fine(   " ******* This is a fine message. *******");
			 * logger.finer(  " ******* This is a finer message. *******");
			 * logger.finest( " ******* This is the finest message. *******");
			 */

			/*
			 * To remove the console handler, use
			 * logger.setUseParentHandlers(false); since the ConsoleHandler is
			 * registered with the parent logger from which all the loggers
			 * derive.
			 * 
			 * ConsoleHandler handler = new ConsoleHandler(); // PUBLISH this
			 * level handler.setLevel(Level.FINER); logger.addHandler(handler);
			 * 
			 * The levels in descending order are: SEVERE (highest value)
			 * WARNING INFO CONFIG FINE FINER FINEST (lowest value) In addition
			 * there is a level OFF that can be used to turn off logging, and a
			 * level ALL that can be used to enable logging of all messages.
			 * logger.severe("..."); logger.warning("...");
			 * logger.config("..."); logger.fine("..."); logger.finer("...");
			 * logger.finest("...");
			 * 
			 * seems as though only INFO and WARNING get written to console.
			 * java.util.logging has a root logger that defaults to Level.INFO,
			 * and a ConsoleHandler attached to it that also defaults to
			 * Level.INFO. FINE is lower than INFO, so fine messages are not
			 * displayed by default.
			 */
		} catch (SecurityException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

		InetAddress PublicIp = GlobalStuff.getAddress("Public");
		if (PublicIp == null) {
			logger.severe("Failed to Find a Public IP.");
			System.exit(1);
			return;
		}

		System.setProperty("java.net.preferIPv4Stack", "true");
		InetAddress LoopBackIp = GlobalStuff.getAddress("LoopBack");
		if (LoopBackIp == null) {
			logger.warning("Failed to Find a LoopBackIp IP, using localhost.");
			LoopBackIp = Inet4Address.getLocalHost();
		}
		logger.info("Public IP of system is: " + PublicIp.getHostAddress());
		String DEF_DESTINATION_HOST = LoopBackIp.getHostAddress();

		Options options = new Options();
		String desc = "IP Address to bind to for listening for Request traffic (default: "
				+ DEF_BIND_IP + " )";
		Option ReqBindIp = new Option("ReqIp", true, desc);
		ReqBindIp.setRequired(false);
		options.addOption(ReqBindIp);

		desc = "The port to listen on for Request traffic (default: "
				+ LISTEN_PORT + " )";
		Option ReqPort = new Option("ReqPort", true, desc);
		ReqPort.setRequired(false);
		options.addOption(ReqPort);

		desc = "IP Address to forward Request to (default: "
				+ DEF_DESTINATION_HOST + " )";
		Option FwdIp = new Option("FwdIp", true, desc);
		FwdIp.setRequired(false);
		options.addOption(FwdIp);

		desc = "IP port to forward Request to (default: " + FORWARD_PORT
				+ " )";
		Option FwdPort = new Option("FwdPort", true, desc);
		FwdPort.setRequired(false);
		options.addOption(FwdPort);

		desc = "Use Loopback mode (default: False )";
		Option LoopBack = new Option("L", "LoopBack", false, desc); // .hasArg(false);
		LoopBack.setRequired(false);
		options.addOption(LoopBack);

		desc = "Wait for User Input to Continue (default: False )";
		Option waitOpt = new Option("w", "Wait", false, desc);
		waitOpt.setRequired(false);
		options.addOption(waitOpt);

		desc = "Emulate Response Server (default: False )";
		Option emuOpt = new Option("e", "Emu", false, desc);
		emuOpt.setRequired(false);
		options.addOption(emuOpt);

		desc = "Use Public Server IP (default: 0.0.0.0 )";
		Option PubOpt = new Option("P", "Pub", false, desc);
		PubOpt.setRequired(false);
		options.addOption(PubOpt);

		desc = "Debug Level (default: 0 )";
		Option dbgLevel = new Option("d", "dbgLevel", true, desc);
		dbgLevel.setRequired(false);
		options.addOption(dbgLevel);

		desc = "Log output to console also";
		Option consoleLog = new Option("lc", "consoleLog", false, desc);
		consoleLog.setRequired(false);
		options.addOption(consoleLog);

		desc = "Skip validation";
		Option noValid8 = new Option("nv", "noValid8", false, desc);
		noValid8.setRequired(false);
		options.addOption(noValid8);

		desc = "Assume V5 Requests rather than V3";
		Option V5Reqs = new Option("v5", "V5Reqs", false, desc);
		V5Reqs.setRequired(false);
		options.addOption(V5Reqs);

		Option helpoption = Option.builder("h").longOpt("help")
				.desc("usage help").hasArg(false).argName("hlp").build();
		options.addOption(helpoption);

		HelpFormatter hlpformatter = new HelpFormatter();
		String header = "Multispeak Translator/Validator for version 3 and version 5 messages.\n\n";
		String footer = "\nPlease report issues at www.pnnl.gov/givethemtowill";

		CommandLine cmd;
		CommandLineParser parser = new DefaultParser();

		try {
			cmd = parser.parse(options, args);
		} catch (ParseException e) {
			logger.severe(e.getMessage());
			hlpformatter.printHelp("JabbaPipe", header, options, footer, true);
			System.exit(1);
			return;
		}
		
		boolean Log2console = false;
		if (cmd.hasOption("lc"))
			Log2console = true;
		GlobalStuff.Log2Console(Log2console);

		if (cmd.hasOption("h")) {
			hlpformatter.printHelp("JabbaPipe", header, options, footer, true);
			System.exit(1);
			return;
		}

		String BIND_IP;
		String FORWARD_IP;
		String REQUEST_PORT = cmd.getOptionValue("ReqPort");
		if (cmd.hasOption("L")) {
			BIND_IP = LOOP_BIND_IP;
			FORWARD_IP = LOOP_DESTINATION_HOST;
			LOOP_LISTEN_PORT = 7776; // The port to listen on for Request
										// inbound traffic
			if (REQUEST_PORT != null)
				LISTEN_PORT = Integer.parseInt(REQUEST_PORT);
			else
				LISTEN_PORT = LOOP_LISTEN_PORT;
		} else {
			BIND_IP = cmd.getOptionValue("ReqIp");
			if (BIND_IP == null) {
				if (cmd.hasOption("P")) {
					BIND_IP = PublicIp.getHostAddress();
				} else {
					BIND_IP = DEF_BIND_IP;
				}
			}
			FORWARD_IP = cmd.getOptionValue("FwdIp");
			if (FORWARD_IP == null)
				FORWARD_IP = DEF_DESTINATION_HOST;
			if (REQUEST_PORT != null)
				LISTEN_PORT = Integer.parseInt(REQUEST_PORT);
		}

		String FWD_PORT = cmd.getOptionValue("FwdPort");
		if (FWD_PORT != null)
			FORWARD_PORT = Integer.parseInt(FWD_PORT);

		boolean Wait = false;
		if (cmd.hasOption("Wait"))
			Wait = true;
		GlobalStuff.setWait(Wait);

		boolean Emulate = false;
		if (cmd.hasOption("Emu"))
			Emulate = true;
		GlobalStuff.EmuV5Srvr(Emulate);

		int dbglev = -1;
		if (cmd.hasOption("dbgLevel")) {
			String Debug_Level = cmd.getOptionValue("dbgLevel");
			dbglev = Integer.parseInt(Debug_Level);
		}
		GlobalStuff.setDebugLevel(dbglev);
		
		boolean V3Reqs = true;
		if (cmd.hasOption("v5"))
			V3Reqs = false;
		GlobalStuff.assumeV3Requests(V3Reqs);

		boolean Valid8 = true;
		if (cmd.hasOption("nv"))
			Valid8 = false;
		GlobalStuff.doValid8(Valid8);

		//JSecureListen jsecure = 
		new JSecureListen(8443);

		PipelineServer thePipelineServer = new PipelineServer(BIND_IP, LISTEN_PORT, FORWARD_IP, FORWARD_PORT);
		// thePipelineServer.run( "v3v5_mr_PingUR.xsl", "v5v3_mr_PingURLResponse.xsl" );
		thePipelineServer.run("./xslt/ms_msg.xslt", "./xslt/ms_msg.xslt");
	}

	// @SuppressWarnings("unchecked")
	public String run(String xsltFile, String xmlData) throws Exception {
		Logger logger = GlobalStuff.getLogger();

		String result = null;
		URL[] saxload = { 
				new URL("file://" + Paths.get(".").toAbsolutePath().normalize().toString() + "/lib/saxonsa.jar") ,
				new URL("file://" + Paths.get(".").toAbsolutePath().normalize().toString() + "/lib/XMLConverters.jar"), 
				new URL("file://" + Paths.get(".").toAbsolutePath().normalize().toString() + "/lib/commons-cli-1.3.1.jar") };

		ClassLoader saxucl = URLClassLoader.newInstance(saxload);
		Class<?> saxclv = saxucl.loadClass("com.ddtek.xmlconverter.ConverterFactory");
		Class<?> xxclv = saxucl.loadClass("net.sf.saxon.TransformerFactoryImpl");
		com.ddtek.xmlconverter.ConverterFactory cFactory = (com.ddtek.xmlconverter.ConverterFactory) saxclv.newInstance();
		TransformerFactory tFactory = (TransformerFactory) xxclv.newInstance();
		com.ddtek.xmlconverter.ConverterResolver resolver = cFactory.newResolver();
		tFactory.setAttribute(net.sf.saxon.lib.FeatureKeys.VERSION_WARNING,	new Boolean(false));
		tFactory.setURIResolver(resolver);

		// Declares for XSLT node XSLTOperator
		// capture any output to console stderr, to baos string
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setErr(new PrintStream(baos));

		try {
			StringReader reader = new StringReader(xmlData);
			StringWriter writer = new StringWriter();
			
			tFactory = (TransformerFactory) xxclv.newInstance();
			Transformer transformer = tFactory
					.newTransformer(new javax.xml.transform.stream.StreamSource(xsltFile));
			transformer.transform(new javax.xml.transform.stream.StreamSource(reader),
					new javax.xml.transform.stream.StreamResult(writer));

			result = writer.toString();
			System.setOut(new PrintStream(new FileOutputStream(FileDescriptor.err))); // revert back to the original stderr stream
			return result;
		} catch (Exception e) {
			String err = baos.toString();
			logger.severe("Exception Raised While Translating Data:\n" + err);
			logger.severe("Input Data:\n" + xmlData + "\n");
			System.setOut(new PrintStream(new FileOutputStream(FileDescriptor.err))); // revert back to the original stderr stream
			throw new RuntimeException("Translation Exception", e);
		}
	}

	// --------------------------- APIs
	// -------------------------------------------------------------------------
	// API to allow a program to bind data to the pipeline input ports
	// @SuppressWarnings("rawtypes")
	private Hashtable<String, StreamSource> m_pipelineInputs = new Hashtable<String, StreamSource>();

	// @SuppressWarnings("unchecked")
	public void bindInputObject(String portName, Object obj, Object ignored) {

		if (!(obj instanceof InputStream))
			throw new IllegalArgumentException(
					"bindInputObject for inline pipeline code supports only InputStream.");

		m_pipelineInputs.put(portName, new StreamSource((InputStream) obj));
	}

	// API to allow an program to bind data to the pipeline output ports
	// @SuppressWarnings("rawtypes")
	private Hashtable<String, StreamResult> m_pipelineOutputs = new Hashtable<String, StreamResult>();

	// @SuppressWarnings("unchecked")
	public void bindOutputObject(String portName, Object obj) {

		if (!(obj instanceof OutputStream))
			throw new IllegalArgumentException(
					"bindOutputObject for inline pipeline code supports only OutputStream.");

		m_pipelineOutputs.put(portName, new StreamResult((OutputStream) obj));
	}
}

/**
 * PipelineServer is a simple TCP bridging software that allows a TCP port on
 * some host to be transparently forwarded to some other TCP port on some other
 * host. PipelineServer continuously accepts request connections on the
 * listening TCP port (source port) and starts a thread (ConnectionHandlerThread) that
 * connects to the destination host and starts forwarding the data between the
 * requester socket and destination socket.
 */
class PipelineServer {
	int BACK_LOG = 8; // "An accumulation, especially of unfinished work or unfilled orders."
	private ServerSocket m_ServerSocket;
	private String m_BindIp;
	private String m_RqstIp;
	private String m_RespIp;
	private int m_BindPort;
	private int m_RespPort;

	public PipelineServer(String BindIp, int BindPort, String RespIp, int RespPort)
			throws IOException {
		m_ServerSocket = null;
		m_BindIp   = BindIp;   // Listener Ip
		m_BindPort = BindPort; // Listener Port
		m_RespIp   = RespIp;   // Responder Ip
		m_RespPort = RespPort; // Responder Port
	}

	/**
	 * Starts a socket server then Waits for a Requesting client to connect and
	 * then spawns a handler(ConnectionHandlerThread) which creates the pipeline object
	 * and connects to the destination ResponseServer. After connecting to the
	 * ResponseServer, 1 ForwarderThread is created to handle data coming from
	 * the Requester and forwards it to the ResponseServer (RequestForwarder)
	 * and another ForwarderThread is created to handle data coming from the
	 * ResponseServer and forwards it to the Requester (ResponseForwarder).
	 *
	 */
	public void run(String v3xsltFile, String v5xsltFile) {
		Logger logger = GlobalStuff.getLogger();
		int iDebug = GlobalStuff.getDebugLevel();

		try {
			InetAddress addr = InetAddress.getByName(m_BindIp);
			m_ServerSocket = new ServerSocket(m_BindPort, BACK_LOG, addr);
			InetAddress PublicIp = GlobalStuff.getAddress("Public");
			String listenString = String.format("Pipeline Server at %s is listening on %s:%d", PublicIp.getHostAddress(), m_BindIp, m_BindPort);

			logger.info( listenString );
			if( !GlobalStuff.Log2Console() )
				if (iDebug >= 0)
					System.out.println( listenString );

			try {
				
				URL[] load = {
						new URL("file://" + Paths.get(".").toAbsolutePath().normalize().toString() + "/lib/valid.jar") ,
						new URL("file://" + Paths.get(".").toAbsolutePath().normalize().toString() + "/lib/XMLConverters.jar"), 
						new URL("file://" + Paths.get(".").toAbsolutePath().normalize().toString() + "/lib/commons-cli-1.3.1.jar")
					};
				try {
					// capture any output to console, to baos string
					ByteArrayOutputStream baos = new ByteArrayOutputStream();
					System.setOut(new PrintStream(baos));
				
					Class<?> clv = URLClassLoader.newInstance(load).loadClass("JValid");
					GlobalStuff.m_v3JV = (JValid) clv.newInstance();
					GlobalStuff.m_v3JV.init_xsds("./v3/SchemaExtracted");
					GlobalStuff.m_v5JV = (JValid) clv.newInstance();
					GlobalStuff.m_v5JV.init_xsds("./v5/EndPoints/server_xsds");

					System.setOut(new PrintStream(new FileOutputStream(FileDescriptor.out))); // revert back to the original stdout stream

					if (GlobalStuff.m_v3JV == GlobalStuff.m_v5JV){
						throw new Exception("Only got one object returned.");
					}
				} catch (Exception e) {
					String ErrString = String.format("Failed to load V3 or V5 validator: %s", e,toString() );
					throw new RuntimeException(ErrString);
				}
				if (iDebug >= 0)
					System.out.println("Pipeline Server::Waiting for connection from Request Client....");
				while (true) {
					try {
						Socket requestSocket = m_ServerSocket.accept();
						InetAddress ReqAddr = requestSocket.getInetAddress();
						logger.info("Pipeline Server Connected to Request Client @" + ReqAddr );
						// at this point we could use the requestor IP to determine m_RespIp via the routing table (TBD)
						m_RqstIp   = ReqAddr.getHostAddress();
						ConnectionHandlerThread connectionThread = new ConnectionHandlerThread(
								requestSocket, v3xsltFile, v5xsltFile, m_RqstIp, m_RespIp, m_RespPort);
						connectionThread.start();
						// try to connect to destination server before getting connected to by requester....
						//Socket requestSocket = m_ServerSocket.accept();
					} catch (IOException e) {
						logger.info("Pipeline Server::Error on accept socket!");
					}
					if (iDebug >= 1)
						System.out.println("Pipeline Server::Waiting for connection from another Request Client....");
				}
			} catch (RuntimeException e) {
				logger.severe(e.getMessage());
			} finally {
				logger.info("Pipeline Server exiting...");
			}
		} catch (IOException e) {
			logger.severe("Pipeline Server::Error on socket creation!");
		}
		finally {
			if (m_ServerSocket != null){
				try {
					m_ServerSocket.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
	}
}

/**
 * ConnectionHandlerThread is responsible for starting forwarding between a requesting
 * client and a responding server. It keeps track of the requester and servers
 * sockets that are both closed on input/output error during the forwarding. The
 * forwarding is bidirectional and is performed by two ForwarderThread
 * instances.
 */
class ConnectionHandlerThread extends Thread {
	private Socket mRequestSocket;
	String mv3Xslt;
	String mv5Xslt;
	private Socket mResponseSocket;
	private boolean mForwardingActive = false;
	private String m_RqstIp;
	private String m_RespIp;
	private int m_RespPort;

	int miDebug = GlobalStuff.getDebugLevel();
	
	public boolean mBrokeConnection = false;

	public ConnectionHandlerThread(Socket aRequestSocket, String v3xsltFile,
			String v5xsltFile, String RqstIp, String RespIp, int RespPort) {
		mRequestSocket = aRequestSocket;
		mv3Xslt = v3xsltFile;
		mv5Xslt = v5xsltFile;
		m_RqstIp   = RqstIp;
		m_RespIp   = RespIp;
		m_RespPort = RespPort;
	}

	/**
	 * Establishes connection to the destination server and starts bidirectional
	 * forwarding of data between the requester and the server.
	 */
	public void run() {
		InputStream  requesterIn  = null; // coming FROM the requester
		OutputStream requesterOut = null; // going TO the requester
		InputStream  responderIn  = null;
		OutputStream responderOut = null;
		int try_num = 0;
		int BUFFER_SIZE = 0x3FFF;
		Logger logger = GlobalStuff.getLogger();

		while (true) {
			try {
				if( requesterIn == null ){
					// Turn on keep-alive
					mRequestSocket.setKeepAlive(true);
					// Obtain request input & output streams
					requesterIn = mRequestSocket.getInputStream();
					requesterOut = mRequestSocket.getOutputStream();
					mRequestSocket.setReceiveBufferSize(BUFFER_SIZE);
				}
				if (GlobalStuff.EmuV5Srvr() == false) {
					// Connect to the destination server
					logger.info("-Connecting to the destination endpoint server at "
									+ m_RespIp + ":" + m_RespPort + " ...");
					mResponseSocket = new Socket(m_RespIp, m_RespPort);
					if (miDebug >= 2)
						System.out.println("-ConnectionHandlerThread::Connected.");

					// Turn on keep-alive
					mResponseSocket.setKeepAlive(true);
					// Obtain server input & output streams
					responderIn = mResponseSocket.getInputStream();
					responderOut = mResponseSocket.getOutputStream();
					mResponseSocket.setReceiveBufferSize(BUFFER_SIZE);
				}
				break;
			} catch (IOException ioe)   // connect will generate a
										// ConnectionRefused exception if the
										// remote host is not listening on the
										// socket
			{
				if (try_num < 1) { // <= 16
					try_num = try_num + 1;
					double seconds_to_wait = Math.min(16, Math.pow(2, try_num));
					System.err.println("ConnectionHandlerThread::Failed to connect to "
							+ m_RespIp + ":" + m_RespPort + ", retrying in "
							+ seconds_to_wait + " seconds...");
					// use a progressively longer sleep period each request:
					try {
						Thread.sleep((long) (seconds_to_wait * 1000));
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				} else {
					logger.severe("Translator Failed to Connect to Endpoint Server @" + m_RespIp + ":" + m_RespPort + ".");
					if( requesterOut != null ){
						String reply = JabbaConstructHeader.construct_http_header(503,0, 0);
						DataOutputStream mdErr = new DataOutputStream(requesterOut);
						try {
							mdErr.writeBytes(reply);
						} catch (IOException e) {
							e.printStackTrace();
						}
					}
					connectionBroken("ConnectionHandlerThread");
					return;
				}
			}
		}

		// Start forwarding data between requester and responder
		ForwarderThread RequestForwarder;
		mForwardingActive = true;
		if (GlobalStuff.EmuV5Srvr()) {
			RequestForwarder = new ForwarderThread(this, true
					, requesterIn, requesterOut, requesterOut /* mbInp, mdFwd, mdErr */
					, mv3Xslt, mRequestSocket, m_RqstIp, m_RespIp, m_RespPort);
		} else {
			RequestForwarder = new ForwarderThread(this, true
					, requesterIn, responderOut, requesterOut 
					, mv3Xslt, mRequestSocket, m_RqstIp, m_RespIp, m_RespPort);
			// we won't ever respond back to the Endpoint Server, so set output sockets to those of requester:
			ForwarderThread ResponseForwarder = new ForwarderThread(this, false
					, responderIn, requesterOut, requesterOut 
					, mv5Xslt, mResponseSocket, m_RespIp, m_RqstIp, m_RespPort);
			ResponseForwarder.start();
		}
		RequestForwarder.start();
	}

	/**
	 * Called by some of the forwarding threads to indicate that its socket
	 * connection is broken and both requester and server sockets should be
	 * closed. Closing the requester and server sockets causes all threads
	 * blocked on reading or writing to these sockets to get an exception and to
	 * finish their execution.
	 */
	public synchronized void connectionBroken(String tId) {
		// Logger logger = GlobalStuff.getLogger();
		mBrokeConnection = true;

		try {
			mResponseSocket.close();
		} catch (Exception e) {
		}

		try {
			mRequestSocket.close();
		} catch (Exception e) {
		}

		if (mForwardingActive) {
			if (miDebug >= 2) {
				System.out.println("ConnectionHandlerThread::TCP Forwarding "
						+ mRequestSocket.getInetAddress().getHostAddress()
						+ ":" + mRequestSocket.getPort() + " <--> "
						+ mResponseSocket.getInetAddress().getHostAddress()
						+ ":" + mResponseSocket.getPort() + " stopped.");
			}
			mForwardingActive = false;
		}
	}
}

/**
 * ForwarderThread handles the TCP forwarding between a socket input stream (source) and a socket 
 * output stream (dest). It reads the input stream and forwards everything to the output stream. 
 * If some of the streams fails, the forwarding stops and the parent is notified to close all its 
 * sockets.
 */
class ForwarderThread extends Thread {
	JabbaPipe mPipeline;
	ConnectionHandlerThread mReqParent;
	/*
	 * The static keyword in Java means that the variable or function is shared between all instances of 
	 * that class as it belongs to the type, not the actual objects themselves. 
	 */
	boolean mIsRequestForwarder;
	boolean mValid8v3First;
	static Logger logger = GlobalStuff.getLogger();

	BufferedReader   mbInp;
	DataOutputStream mdFwd;
	DataOutputStream mdErr;

	String mXsltFile;
	String mMsgId;
	String mId;
	String mMyIp;
	String mFwdIp;
	String m1stMsgType;
	String m2ndMsgType;
	String mXl8MsgType;
	Socket mSocket;
	int mCnt;
	int mJrrTokenExpect;
	int mRespPort;
	JValid mfirstJV = null;
	JValid mlastJV  = null;

	/**
	 * Creates a new traffic redirection thread specifying its parent, input
	 * stream and output stream.
	 */
	public ForwarderThread(ConnectionHandlerThread aParent, boolean isArequester,
			InputStream aInputStream, OutputStream aOutputStream, OutputStream aErrorStream,
			String XsltFile, Socket aSocket, String myIp, String fwdIp, int rspPort) {
		mReqParent = aParent;
		mIsRequestForwarder = isArequester;

		mbInp = new BufferedReader(new InputStreamReader(aInputStream));
		mdFwd = new DataOutputStream(aOutputStream);
		mdErr = new DataOutputStream(aErrorStream);

		mXsltFile = XsltFile;
		mSocket   = aSocket;
		mMyIp     = myIp;
		mFwdIp    = fwdIp;
		mRespPort = rspPort;

		mCnt = GlobalStuff.getThreadCnt();
		
		if( GlobalStuff.doValid8() ){
			mfirstJV = GlobalStuff.getFirstValidator( mIsRequestForwarder );
			mlastJV  = GlobalStuff.getLastValidator( mIsRequestForwarder );
		}
		
		GlobalStuff.setThreadCnt(GlobalStuff.getThreadCnt() + 1);

		if (mIsRequestForwarder){
			mValid8v3First = GlobalStuff.assumeV3Requests();
			mId = "Thread-" + mCnt +  "::RequestForwarder ";
			mMsgId = "->> Request Received from " + mMyIp;
			mJrrTokenExpect=3;
			if( mValid8v3First){
				m1stMsgType = "V3";
				m2ndMsgType = "V5";
			}
			else{
				m1stMsgType = "V5";
				m2ndMsgType = "V3";
			}
			mXl8MsgType = "----->translating "+ m1stMsgType + " Request.";
			m1stMsgType = "----->validating " + m1stMsgType + " Request.";
			m2ndMsgType = "----->validating " + m2ndMsgType + " Request.";			
		}
		else{
			mValid8v3First = GlobalStuff.assumeV3Requests();
			mId = "Thread-" + mCnt +  "::ResponseForwarder ";
			mMsgId = "Received Response from " + mMyIp;
			mJrrTokenExpect=3;
			if( mValid8v3First){
				m1stMsgType = "V5";
				m2ndMsgType = "V3";
			}
			else{
				m1stMsgType = "V3";
				m2ndMsgType = "V5";
			}
			mXl8MsgType = "<-----translating "+ m1stMsgType + " Response.";
			m1stMsgType = "<-----validating " + m1stMsgType + " Response.";
			m2ndMsgType = "<-----validating " + m2ndMsgType + " Response.";
		}
	}

	/**
	 */
	public String RequestType() {
		if (mIsRequestForwarder){
			return "Request";
		}
		else{
			return "Response";
		}
	}

	/**
	 * Runs the thread. Continuously reads the input stream and writes the read
	 * data to the output stream. If reading or writing fail, exits the thread
	 * and notifies the parent about the failure.
	 */
	public void run() {
		int iDebug = 0;
		byte[] buffer = null;
		char[] cbuffer = null;
		String xmlInData = null;
		String xmlOutData = null;
		String reply = null;
		String httpStatusCode=null;
		String httpStatusMsg=null;
		try {
			iDebug = GlobalStuff.getDebugLevel();
			/*
			 * readLine() - Deprecated. This method does not properly convert
			 * bytes to characters. As of JDK 1.1, the preferred way to read
			 * lines of text is via the BufferedReader.readLine() method.
			 * Programs that use the DataInputStream class to read lines can be
			 * converted to use the BufferedReader class by replacing code of
			 * the form: DataInputStream d = new DataInputStream(in); with:
			 * BufferedReader d = new BufferedReader(new InputStreamReader(in));
			 */
			
			// create the pipeline, 
			// both the client request socket and the server reponse socket have their own pipelines
			mPipeline = new JabbaPipe();
			//int socktmo = 25000;// wait 25k milliseconds for data after initial connection, then wait for 
			int socktmo = 0;	// try waiting forever for data after initial connection, then wait for 
								// more date indefinitely, until socket is closed
			if (!mIsRequestForwarder){
				socktmo = 0;//W8 forever for Endpoint Server to respond
			}

			boolean doBreak;
			boolean readNull;
			while (true) {
				String currentLine = null, strContentLength = null, originalHdr = null;
				String header = null;
				String ErrString = null;
				int ErrCode = 417;
				int datalength = 0;
				doBreak = true;
				readNull = false;
				boolean doContinue = false;
				try {
					/*
					 * With setSoTimeout set to a non-zero timeout, a read() call on the InputStream associated 
					 * with this Socket will block for only this amount of time. If the timeout expires, a 
					 * java.net.SocketTimeoutException is raised, though the Socket is still valid. 
					 * The option must be enabled prior to entering the blocking operation to have effect. 
					 * The timeout must be > 0. A timeout of zero is interpreted as an infinite timeout
					 */
					if (iDebug >= 1) {
						System.out.println(mId + "Waiting For Data..." );
					}
					mSocket.setSoTimeout(socktmo);// set a timeout, as we only reach here after a connection is made
					currentLine = mbInp.readLine();
					if( currentLine == null ){
						System.out.println(mId + "Reading NULL data..." );
						readNull = true;
						break;
					}
					logger.info(mMsgId);
					socktmo = 0;
					/* get all 'words', POST should have 3
						http://stackoverflow.com/questions/5725430/http-test-server-that-accepts-get-post-calls
						http://httpbin.org/
							If you set your URLRequest to http://httpbin.org/post/ then set your POST data correctly, 
							this URL should bounce back your input to you for testing.
					 */
					StringTokenizer tokenizer = new StringTokenizer(currentLine);
					String JrrString=null;
					int JrrTokenCount = tokenizer.countTokens();
					if (mIsRequestForwarder){
						GlobalStuff.m_TotalRequests++;						
						if( JrrTokenCount != mJrrTokenExpect ){
							JrrString = ":";
							for(int i = 0; i<JrrTokenCount; i++){
								JrrString=JrrString+"\n\ttoken["+i+"]: "+tokenizer.nextToken();
							}
							JrrString=JrrString+"\n";
							throw new JabbaRuntimeException(String.format(
									"Unexpected number of tokens in request, expected %d, got %d%s.",
									mJrrTokenExpect, JrrTokenCount, JrrString), 406);
						}
						else{
							String httpMethod   = tokenizer.nextToken(); // "POST"
							String httpPath     = tokenizer.nextToken(); // i.e., "/omsservices/services/OA_ServerSoap"
							String httpProtocol = tokenizer.nextToken(); // "HTTP/1.1"				
							if (iDebug >= 1) {
								System.out.println( String.format(mId + "Got Method: %s, Path: %s, Protocol: %s", httpMethod, httpPath, httpProtocol));
							}	
							if (httpMethod.equals("GET")) {
								throw new RuntimeException("Unexpected GET request.");
							} else if (!httpMethod.equals("POST")) {
								throw new JabbaRuntimeException(String.format("Unexpected request method:  %s.", httpMethod), 405);
							}
							logger.info(String.format("Processing Request for Path: '%s'", httpPath));
						}
					}
					else{ // ResponseForwarder
						GlobalStuff.m_TotalResponses++;
						if( JrrTokenCount < mJrrTokenExpect ){
							JrrString = ":";
							for(int i = 0; i<JrrTokenCount; i++){
								JrrString=JrrString+"\n\ttoken["+i+"]: "+tokenizer.nextToken();
							}
							JrrString=JrrString+"\n";
							throw new JabbaRuntimeException(String.format(
									"Unexpected number of tokens in response, expected %d, got %d%s.",
									mJrrTokenExpect, JrrTokenCount, JrrString), 406);
						}
						else{
							String httpProtocol  = tokenizer.nextToken();	// "HTTP/1.1"				
							httpStatusCode       = tokenizer.nextToken();	// i.e., "200"
							httpStatusMsg = tokenizer.nextToken();	// i.e., "OK"
							while (tokenizer.hasMoreTokens() ){
								httpStatusMsg = httpStatusMsg+" "+tokenizer.nextToken();
							}
							if (iDebug >= 1) {
								System.out.println( String.format(mId + "Got Protocol: %s, Status Code: %s, Status Message: '%s'", httpProtocol, httpStatusCode, httpStatusMsg));
							}
						}
					}
					if (GlobalStuff.EmuV5Srvr()) {
						header = "HTTP/1.1 200 OK";
					} else {
						header = currentLine; // "POST / HTTP/1.1" In HTTP 1.1,
					}
					header = header.concat(System.getProperty("line.separator"));
					originalHdr = header;
					mSocket.setSoTimeout(3000);
					do {
						// save http header for the v5 forward
						try {
							currentLine = mbInp.readLine();
							String lccl = currentLine.toLowerCase();
							if (lccl.indexOf("content-length:") != -1) {
								strContentLength = currentLine.split(" ")[1];
								datalength = Integer.parseInt(strContentLength);
								currentLine = currentLine.concat(System.getProperty("line.separator"));
								originalHdr = originalHdr.concat(currentLine);
								currentLine = currentLine.replace(strContentLength, "XXXLENXXX");
								header = header.concat(currentLine);
								// now read rest of header until blank line
								do {
									currentLine = mbInp.readLine();
									if (currentLine.isEmpty()) {
										header = header.concat(System.getProperty("line.separator"));
										originalHdr = originalHdr.concat(System.getProperty("line.separator"));
										break;
									}
									currentLine = currentLine.concat(System.getProperty("line.separator"));
									header = header.concat(currentLine);
									originalHdr = originalHdr.concat(currentLine);
								} while (mbInp.ready());
							} else {
								currentLine = currentLine.concat(System.getProperty("line.separator"));
								header = header.concat(currentLine);
								originalHdr = originalHdr.concat(currentLine);
							}
						} catch (SocketTimeoutException e) {
							throw new JabbaRuntimeException("Time-out reading HTTP Header.", 408);
						} catch (IOException e) {
							logger.severe("IOException reading HTTP Header.");
							reply = JabbaConstructHeader.construct_http_header(417, 0, 0);
							mdErr.writeBytes(reply);
							throw new IOException(e);
						}
					} while (mbInp.ready() && (datalength == 0));

					if (datalength > 0) {
						if (iDebug >= 1) {
							System.out.println( String.format(mId + "Header(%d):%s\nContent-Length: %d",
									header.length(), header, datalength));
						}

						cbuffer = new char[datalength];
						int cbidx = 0;
						int amount_expected = datalength;
						int amount_read = 0;
						try {
							do {
								amount_read = mbInp.read(cbuffer, cbidx, amount_expected);
								amount_expected = amount_expected - amount_read;
								cbidx = cbidx + amount_read;
							} while (amount_expected > 0);
						} catch (SocketTimeoutException e) {
							/*
							 * if the request http is ok, but the responder's is
							 * not, we should prob. return a 400 to the
							 * requester, not the responder?? responder is not
							 * waiting for anything back,is it?
							 */
							throw new JabbaRuntimeException(String.format(
											"Time-out reading HTTP Content: read %d bytes so far, expected another %d.",
											amount_read, amount_expected), 408);
						} catch (IOException e) {
							throw new JabbaRuntimeException("IOException reading HTTP Content.", 411);
						}
						if (iDebug >= 1) {
							System.out.println( String.format(mId + "Content Read Length: %d",cbidx));
						}
						xmlInData = new String(cbuffer).substring(0, datalength);
						if (!mIsRequestForwarder) {
							if (!httpStatusCode.equals("200")) {
								UpdateLogStats( mIsRequestForwarder, GlobalStuff.LogType.NOT_OK, httpStatusCode, httpStatusMsg, false );
								buffer = AssembleReturn( originalHdr, xmlInData, false, false );								
								mdErr.write(buffer); // just forward to requester
								doBreak = false;
								continue;
							}
						}
						doBreak = false;
					} else {
						throw new JabbaRuntimeException("Failed to Get Data Length.", 411);
					}
				} catch (JabbaRuntimeException e) {
					ErrCode = e.getStatus();
					ErrString = String.format("%s", e.getMessage());
					// remove any remaining bytes from the request/response
					do {
						mbInp.readLine();
					} while (mbInp.ready());
					doContinue = true;
				} catch (java.util.NoSuchElementException e) {
					ErrString = String.format("%s processing aborted: NoSuchElementException Reading Socket.", RequestType() );
				} catch (SocketTimeoutException e) {
					ErrString = String.format("%s processing aborted: Time-out Reading Socket.", RequestType() );
				} catch (SocketException e) {
					ErrString = String.format("%s processing aborted: SocketException Reading Socket.", RequestType() );
				} catch (Exception e) {
					ErrString = String.format("Exception: %s, %s", e,getName(), e.getMessage() );
				}
				finally {
					if (iDebug == 100){
						System.out.println( "\n----Received:\n" +  xmlInData);
					}					
					if( mReqParent.mBrokeConnection )
						break;
					if( readNull ){
						break;
					}
					if( doBreak || doContinue ){
						UpdateLogStats( mIsRequestForwarder, GlobalStuff.LogType.POSTCHECK, null, null, false );
						if( ErrString != null ) // !ErrString.isEmpty()
							logger.severe( ErrString );
						reply = JabbaConstructHeader.construct_http_header(ErrCode, 0, 0);
						mdErr.writeBytes(reply);
						if( doBreak ){
							break;
						}
						continue;
					}
				}
				try {
					if (iDebug >= 2) {
						if (GlobalStuff.getWait()) {
							System.out.println("press ENTER to forward message on...");
							try {
								System.in.read(); // wait for user input
							} catch (IOException e) {
								e.printStackTrace();
							}
						}
					}
					boolean good = false;
					if( GlobalStuff.doValid8() ){
						if( !mIsRequestForwarder ){ // skip Valid8 of v5 response
							good = true;
							System.out.println( "Skipping " + m1stMsgType );
						}
						else{
							try {
								if (iDebug == 0)
									System.out.println( m1stMsgType );
								//ByteArrayOutputStream baos = new ByteArrayOutputStream();
								//System.setOut(new PrintStream(baos));
								good = mfirstJV.validate(xmlInData);
								if (iDebug == 0){
									String msg = "SUCCESS " + m1stMsgType;
									System.out.println( msg );
									logger.info(String.format("%s", msg));
								}							
								//System.setOut(new PrintStream(new FileOutputStream(FileDescriptor.out))); // revert back to the original stdout stream
							} catch (Exception ex) {
								if (iDebug == 0)
									System.out.println( "FAILED " + m1stMsgType );
							    good = false;
								logger.severe(String.format( "%s Exception Validating Data: %s, data:\n%s",
										mId, ex.toString(), xmlInData));
							}
						}
					}
					else{
						good = true;
						UpdateLogStats( mIsRequestForwarder, GlobalStuff.LogType.NO_VALID8, null, null, false );
					}
					if (good) {
						xmlOutData = null;
						if (iDebug == 0)
							System.out.println(mXl8MsgType);
						try {
							xmlOutData = mPipeline.run(mXsltFile, xmlInData);
						} catch (Exception ex) {
							xmlOutData = null;
							logger.severe("JT.translate" + ex.toString());
						}
						if (xmlOutData == null) {
							if (iDebug == 0)
								System.out.println( "FAILED *******> " + mXl8MsgType + "<*******" );

							UpdateLogStats( mIsRequestForwarder, GlobalStuff.LogType.XL8, null, null, false );
							reply = JabbaConstructHeader.construct_http_header(417, 0, xmlInData.length());
							buffer = AssembleReturn( reply, xmlInData, false, false );
							mdErr.write(buffer);
							continue;
						}
						else { // good translate
							if (iDebug == 0){
								String msg = "SUCCESS " + mXl8MsgType;
								System.out.println( msg );
								logger.info(String.format("%s", msg));
							}
							if( GlobalStuff.doValid8() ){
								boolean skipafterxl8 = true;
								if( skipafterxl8 ){ // mIsRequestForwarder, skip Valid8 after xl8
									good = true;
									System.out.println( "Skipping " + m2ndMsgType );
								}
								else{
									try {
										if (iDebug == 0)
											System.out.println( m2ndMsgType );
										//ByteArrayOutputStream baos = new ByteArrayOutputStream();
										//System.setOut(new PrintStream(baos));
										mlastJV.validate(xmlOutData);
										if (iDebug == 0){
											String msg = "SUCCESS " + m2ndMsgType;
											System.out.println( msg );
											logger.info(String.format("%s", msg));
										}							
										//System.setOut(new PrintStream(new FileOutputStream(FileDescriptor.out))); // revert back to the original stdout stream
									} catch (Exception ex) {
										if (iDebug == 0)
											System.out.println( "FAILED " + m2ndMsgType );
										UpdateLogStats( mIsRequestForwarder, GlobalStuff.LogType.VALID8, null, null, !mValid8v3First );
										logger.severe(String.format( "%s Exception Validating Data: %s, data:\n%s",
												mId, ex.toString(), xmlOutData));
										//  chm 3.9.2017
										reply = JabbaConstructHeader.construct_http_header(417, 0, xmlOutData.length());
										buffer = AssembleReturn( reply, xmlOutData, false, false );
										mdErr.write(buffer);
										continue; 
									}
								}
							}
							else{
								UpdateLogStats( mIsRequestForwarder, GlobalStuff.LogType.NO_VALID8, null, null, false );
							}
						}
					} else { // NOT good validate
						UpdateLogStats( mIsRequestForwarder, GlobalStuff.LogType.VALID8, null, null, mValid8v3First );
						reply = JabbaConstructHeader.construct_http_header(417, 0, xmlInData.length());
						buffer = AssembleReturn( reply, xmlInData, false, false );
						mdErr.write(buffer);
						continue;
					}
				} catch (Exception e) {
					reply = JabbaConstructHeader.construct_http_header(417, 0, 0);
					mdErr.writeBytes(reply);
					logger.severe(String.format("%s Exception Translating Data: %s, data:\n%s",
							mId, e.toString(), xmlInData));
					continue; // break; try keeping socket open until requester closes
				}

				buffer = AssembleReturn( header, xmlOutData, true, false );
				mdFwd.write(buffer); // forward the message

				if (iDebug == 0)
					if (mIsRequestForwarder)
						System.out.println("Forwarded Request, Waiting for Response From Server...");
					else
						System.out.println("*** SUCCESSFULLY FORWARDED RESPONSE !! ***, Waiting for new Request...\n");
				
				UpdateLogStats( mIsRequestForwarder, GlobalStuff.LogType.OK_200, null, null, false );
				
				try {
					if (iDebug >= 2) {
						Thread.sleep(2000);
						GlobalStuff.clearConsole();
					}
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			} // while not broken
		} catch (IOException e) {
			if (iDebug >= 2){ // 
				System.out.println("\nRead/write failed --> connection is broken\n");
			}
			e.printStackTrace();
		}
		if (iDebug == 0)
			if (mIsRequestForwarder)
				System.out.println("RequestForwarder socket broken.\n");
			else
				System.out.println("ResponseForwarder socket broken.\n");
		// Notify parent thread that the connection is broken
		mReqParent.connectionBroken(mId);
	}
	
	// ////////////////
	public byte [] AssembleReturn( String hdr, String bdy, boolean newLength, boolean dbg ) {

		int bdylen = bdy.length();
		if( newLength ){
			String strContentLength = Integer.toString(bdylen);
			hdr = hdr.replace("XXXLENXXX", strContentLength);
		}
		int hdrlen = hdr.length();
		int datalen = hdrlen + bdylen;
		byte [] buff = new byte[datalen];
		System.arraycopy(hdr.getBytes(), 0, buff, 0, hdrlen);
		System.arraycopy(bdy.getBytes(), 0, buff, hdrlen, bdylen);

		if (dbg) {
			System.out.println( String.format("AssemblingReturn:\nHeader(%d):\n%s\nContent(%d):\n%s",
					hdrlen, hdr, bdylen, bdy));
		}

		return buff;
	}

	// ////////////////
	// logs failures in the process of validating and translating requests and responses.
	// if no failures along the way, logs success.
	//
	public static void UpdateLogStats( boolean bRequester, GlobalStuff.LogType LogType, 
									   String httpStatusCode, String msg, boolean v3 ) {
		int reqrspTotal;
		int rqstCntUpdate = 0;
		int respCntUpdate = 0;
		int ActionCount; // validate, translate or post failure, or fwd success count 
		String msgtype;
		String action;
		String action2 = " ";

		if (bRequester) {
			msgtype = "Request";
			reqrspTotal = GlobalStuff.m_TotalRequests;
			rqstCntUpdate++;
		}
		else{
			msgtype = "Response";
			reqrspTotal = GlobalStuff.m_TotalResponses;
			respCntUpdate++;
		}

		switch (LogType) {
			case OK_200:
				if (bRequester)
					ActionCount = GlobalStuff.m_TotalRequestsOk;
				else
					ActionCount = GlobalStuff.m_TotalResponsesOk;

				GlobalStuff.m_TotalRequestsOk  += rqstCntUpdate;// note: only one of these will be non-zero
				GlobalStuff.m_TotalResponsesOk += respCntUpdate;
				ActionCount += rqstCntUpdate;// note: only one of these will be non-zero
				ActionCount += respCntUpdate; 
					
				logger.info(String.format("%d out of %d %ss sucessfully forwarded.",
											ActionCount, reqrspTotal, msgtype));
				return;

			case VALID8:
				if( v3 ){
					action = "Validate";
					action2 = " V3 ";
				}
				else{
					action = "Validate";
					action2 = " V5 ";
				}
				if (bRequester)
					ActionCount = GlobalStuff.m_RqstValidateFailed;
				else
					ActionCount = GlobalStuff.m_RespValidateFailed;
				break;

			case XL8:
				action = "Translate";
				if (bRequester)
					ActionCount = GlobalStuff.m_RqstTranslateFailed;
				else
					ActionCount = GlobalStuff.m_RespTranslateFailed;
				break;

			case POSTCHECK:
				action = "POST Header Check";
				if (bRequester)
					ActionCount = GlobalStuff.m_RqstPostCheckFailed;
				else
					ActionCount = GlobalStuff.m_RespPostCheckFailed;
				break;

			case NOT_OK:
				if (bRequester){
					logger.severe(String.format("*** Sanity Failure: NOT_OK Passed by Requester."));
					return;
				}
				else{
					GlobalStuff.m_RespNotOkay++;
					logger.info(String.format("Validation and Translation skipped, Response Status(%s '%s') not 'OK', for of %d out of %d Responses.",
							httpStatusCode, msg, GlobalStuff.m_RespNotOkay, GlobalStuff.m_TotalResponses));
					return;
				}

			case NO_VALID8:
				logger.info(String.format("*** Validation Skipped. ***"));
				return;
					            	            
			default:
				logger.severe(String.format("*** Sanity Failure default value: %d.", LogType));
				return;
		} //  end switch

		if( LogType == GlobalStuff.LogType.POSTCHECK){
			GlobalStuff.m_RqstPostCheckFailed += rqstCntUpdate;// note: only one of these will be non-zero
			GlobalStuff.m_RespPostCheckFailed += respCntUpdate;
			ActionCount += rqstCntUpdate;// note: only one of these will be non-zero
			ActionCount += respCntUpdate; 
			logger.warning(String.format("%d out of %d %ss have failed a %s.", ActionCount, reqrspTotal, msgtype, action));
		}
		else{
			GlobalStuff.m_RqstValidateFailed += rqstCntUpdate;
			GlobalStuff.m_RespValidateFailed += respCntUpdate;
			ActionCount += rqstCntUpdate;// note: only one of these will be non-zero
			ActionCount += respCntUpdate; 
			logger.warning(String.format("Failed to %s%s%s Successfully, total of %d out of %d %ss have failed to %s.",
					action, action2, msgtype, ActionCount, reqrspTotal, msgtype, action));
		}
	}

	// ////////////////
	public static String getStackTrace(Throwable t) {
		StringWriter sw = new StringWriter();
		t.printStackTrace(new PrintWriter(sw));
		return sw.toString();
	}
}
