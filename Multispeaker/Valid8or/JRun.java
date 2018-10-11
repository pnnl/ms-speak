
import java.io.*;
import org.apache.commons.cli.*;

/*
java -cp "../lib/*" JRun -sd "/home/carl/Desktop/MS-SPEAK/V507/XSDS/EndPoints/" -ep "CD_Server" -xf "/home/carl/Desktop/MS-SPEAK/files/InitCDReq.xml" -v 2
 */
public class JRun  { // extends JReturn
	private static JValid m_v5JV;
	private static JReturn Result=JReturn.INIT_FAIL;
	private static int verbosity=0;
	//// constructor
	public JRun() {
    }
	/*
	 * Typically, in languages where main returns int (such as C and C++) the return code of 
	 * main becomes the exit code of the process, which is often used by command interpreters 
	 * and other external programs to determine whether the process completed successfully. 
	 * 
	 * To achieve the same effect in Java, use the System.exit method.
	 * 		i.e. System.exit(42);
	 * to see the return when java is called from the command line:
	 * 		echo $?
	 */
	public static void main(String[] args) {
		try {
			CommandLine cmd;
			CommandLineParser parser = new DefaultParser();

			HelpFormatter formatter = new HelpFormatter();
			String header = "Validate XML against a schema.\n\n";
			String footer = "\nPlease report issues at github.com/pnnl/ms-speak";

			/* Option
			 * opt - short representation of the option
			 * longOpt - the long representation of the option
			 * hasArg - specifies whether the Option takes an argument or not
			 * description - describes the function of the option
				//opt = Option.builder("h").longOpt("help")
				//		.desc("usage help").hasArg(false).argName("hlp").build();		
			 */
			OptionGroup grpHlp = new OptionGroup();
			grpHlp.setRequired(false);
			Options hlpOpts = new Options();
			Option optHlp = new Option("h", "help", false, "usage help)");
			optHlp.setRequired(false);	
			grpHlp.addOption(optHlp);	
			
			Option optVer = new Option("v", "ver", false, "version)");
			optVer.setRequired(false);
			grpHlp.addOption(optVer);	
			
			hlpOpts.addOptionGroup(grpHlp);			
		
			Options options = new Options();
			
			Option opt = new Option("sd", "schema", true, "schema xsd directory to use");
			opt.setRequired(true);
			options.addOption(opt);		
			
			opt = new Option("ep", "endpoint", true, "endpoint server name");
			opt.setRequired(true);
			options.addOption(opt);		
			
			opt = new Option("xf", "xmlfile", true, "xml file to validate");
			opt.setRequired(true);
			options.addOption(opt);
		
			opt = new Option("v", "verbosity", true, "Debug Verbosity (default: 0 )");
			opt.setRequired(false);
			options.addOption(opt);			

			String schema_dir="";
			String endpoint="";
			String xml_file="";
			try {
				
				// this parses the command line but doesn't throw an exception on unknown options
				// options - the specified Options
				// arguments - the command line arguments
				// stopAtNonOption - if true an unrecognized argument stops the parsing and the remaining 
				// arguments are added to the CommandLines args list. If false an unrecognized 
				// argument triggers a ParseException.
				cmd = parser.parse(hlpOpts, args, true);
				Option opts[] = cmd.getOptions();
				if( opts.length != 0 ) {
					if (cmd.hasOption("h")) {
						formatter.printHelp("JRun", header, options, footer, true);
						System.exit(JReturn.SUCCESS.value());		
						return;
					} else if (cmd.hasOption("v")) {			
						System.out.println("--->Version: " + "1.0.0");
						System.exit(JReturn.SUCCESS.value());		
						return;
					}
				}				
				
				cmd = parser.parse(options, args);
				if (cmd.hasOption("h")) {
					formatter.printHelp("JRun", header, options, footer, true);
					System.exit(JReturn.SUCCESS.value());		
					return;
				}
				schema_dir = cmd.getOptionValue("schema");
				endpoint = cmd.getOptionValue("endpoint");
				xml_file = cmd.getOptionValue("xmlfile");
				if (cmd.hasOption("verbosity")) {
					verbosity = Integer.parseInt(cmd.getOptionValue("verbosity"));
				}
			} catch (ParseException e) {
				System.out.println("--->" + e.getMessage());
				formatter.printHelp("JRun", header, options, footer, true);
				System.exit(Result.value());
			}
			m_v5JV = new JValid(verbosity);
        	Result = run(schema_dir, endpoint, xml_file);
			if( verbosity > 2 )
				if( Result == JReturn.SUCCESS )
					System.out.println("--->JRUN::Success");
				else {
					System.out.println("--->JRUN::Failure");
				}
			System.exit(Result.value());		
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			System.exit(JReturn.EXCEPTION.value());
		}
	}
	//// run
	public static JReturn run(String xsddir, String ep, String xml_file) throws Exception {
		JReturn vRet;
		// capture any output to console stderr, to baos string
		ByteArrayOutputStream baos = new ByteArrayOutputStream();
		System.setErr(new PrintStream(baos));
		try {
			vRet = InitXsds(xsddir, ep);
			if( vRet == JReturn.SUCCESS )
				vRet = Validate(xml_file);
			return vRet;
		} catch (Exception ex) {
			String err = baos.toString();
			System.out.println("Exception Raised While Validating Data:\n" + err);
			System.out.println("Schema Dir: " + xsddir );
			System.out.println("EndPoint: " + ep );
			System.out.println("XML File:" + xml_file );
			System.setOut(new PrintStream(new FileOutputStream(FileDescriptor.err))); // revert back to the original stderr stream
			throw new RuntimeException("Translation Exception", ex);
		}
	}
	//// InitXsds
	public static JReturn InitXsds(String xsdpath, String ep){
		JReturn vRet=JReturn.INITXSD_FAIL;
		try {
			vRet = m_v5JV.init_xsds(xsdpath,ep);
			if( verbosity == 2 )
				if( vRet == JReturn.SUCCESS )
					System.out.println("--->JRUN::XSDs Initialized Successfully.");
				else
					System.out.println("--->JRUN::Failed to Initialize XSDs.");
			
		} catch (Exception ex) {
			System.out.println("--->JRUN::InitXsds Exception: " +ex.toString());
		}
		return vRet;
	}
	//// Validate
	public static JReturn Validate(String xmlFilePath){
		JReturn vRet=JReturn.VALID8_FAIL;

		try {
			if( verbosity > 2 ){
				System.out.println("--->JRUN::Validating XML file " + xmlFilePath);
			}
			File xmlFile = new File(xmlFilePath);
			String xml_data = JValid.fileToString(xmlFile);

			if( xml_data != null ){
				vRet = m_v5JV.validate(xml_data);
				if( verbosity == 2 ){
					if( vRet == JReturn.SUCCESS )
						System.out.println("--->JRUN::Successfully Validated XML file " + xmlFilePath);
					else
						System.out.println("--->JRUN::Failed to Validate XML file " + xmlFilePath);
				}
			}
			//System.out.println("Exit JRun::Validate().");
		} catch (Exception ex) {
			if( verbosity > 0 )
				System.out.println("--->JRUN::Validate Exception: " +ex.toString());
		}
		return vRet;
	}
}
