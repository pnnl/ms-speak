
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.ByteArrayInputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;

import javax.xml.validation.*;
import javax.xml.transform.Source;
import javax.xml.transform.stream.StreamSource;

  /**
   * grep -rio --include='*.xsd' --include='*.xml' -e 'targetNamespace="[^"]*"'
   * grep -rio --include='*.xsd' --include='*.xml' -e 'schemaLocation="[^"]*"'
  EXAMPLE:
        JValid JV = new JValid("v3/SchemaExtracted");
					or
		JValid JV = new JValid();
		JV.init_xsds("../V507_Endpoints/CD_Server");

		boolean good = false;
		try {
			good = JV.validate(JV.fileToString(new File("./wake3.xml")));
		} catch (Exception ex) {
		  System.out.println("JV.validate" + ex.toString());
		}

		if (good) {
			System.out.println("Validated!");
		} else {
			System.out.println("Failed to validate");
		}
  **/

public class JValid {//extends JParseSOAP{

	private class validatorcontainer {
	  Validator valid;
	  String xsdfile;
	}
	private int m_Verbosity;
	private ArrayList <Validator>A;
	private ArrayList <validatorcontainer>V;
	//private File[] filereference;

	// constructors
	public JValid(int Verbosity) {
        //super(0);
		m_Verbosity = Verbosity;
	}

	/*public JValid(String path) {
		A =  new ArrayList<Validator>();
		V = new ArrayList<validatorcontainer>();
		File[] xsds = get_xsd_files(path);
	}*/
 
 
	// only use with default constructor
	public JReturn init_xsds(String xsdpath, String endpoint) {
		A =  new ArrayList<Validator>();
		V = new ArrayList<validatorcontainer>();

		File[] xsds = get_xsd_files(xsdpath,endpoint);
		if (xsds == null)
			return JReturn.INIT_FAIL;
		if (xsds.length == 0)
			return JReturn.INIT_FAIL;
		return JReturn.SUCCESS;
	}
	
	// return array of Files
	// Note, the server xsd files import relative to ../../xsd
	//		this routine expects to be passed a path such as '..../Endpoints'
    // 		which holds server folders, such as 'CD_Server', 'MR_Server' etc.
    //		each of which holds an xsd file.
    //		It also assumes that the 'EndPoints' folder will have an additional
    //		folder in it called 'xsd' which holds the xsd files that the server
    //		xsds import, i.e.,:
    //			~/MS-SPEAK/V507/XSDS
    //					/EndPoints
    //						/CD_Server
    //							CD_Server.xsd
    //					/xsd
    //						MultiSpeak.xsd, mspCommonTypes.xsd, soapEnvelope.xsd ....
    //		Note the inclusion of soapEnvelope.xsd, it must be added to the xsd folder.
    //
	//@SuppressWarnings("unused")
	private File[] get_xsd_files (String path, String endpoint)
	{
		String currdir="";
		
		File XsdPath=new File(path);
		if( XsdPath.isDirectory() ) {
			File cd=new File(".");
			try {
				currdir = cd.getCanonicalPath();
			} catch (IOException e) {
				e.printStackTrace();
				return null;
			}
			System.setProperty("user.dir", path);
		}
		else {
			System.out.println("--->JValid::Path must be to a directory: " +path);
			return null;
		}
		
	    File xfile = new File("../xsd/");
	    String HdrPath = "";
	    try {
		    HdrPath = xfile.getCanonicalPath();
			//System.out.println("Absolute Path: " + HdrPath);// /home/carl/MS-SPEAK/V507/XSDS/xsd
		} catch (IOException e) {
			e.printStackTrace();
			System.setProperty("user.dir", currdir);
			return null;
		}
		// 9.15.18 - add in MsgHeader and envelope xsds
		File reqfile = new File(HdrPath+"/MultiSpeakWebServicesRequestMsgHeader.xsd");
		File resfile = new File(HdrPath+"/MultiSpeakWebServicesResponseMsgHeader.xsd");
		File envfile = new File(HdrPath+"/soapEnvelope.xsd");
	
		List<File> xsds = new ArrayList<File>();
		xsds.add(reqfile);
		xsds.add(resfile);
		xsds.add(envfile);
		
		File xsdfolder = new File(path);// should be pointing to ../Endpoints
		File[] EndPointServers = xsdfolder.listFiles();
		for (int i = 0; i < EndPointServers.length; i++) {
			if (EndPointServers[i].isFile()) {
				System.out.println("--->JValid::Omitting File " + EndPointServers[i].getName());
				//System.out.println("--->JValid::Adding File " + EndPointServers[i].getName());
				//xsds.add( EndPointServers[i] );
			} else if (EndPointServers[i].isDirectory()) {
				if( !EndPointServers[i].getName().equals(endpoint) ){
					continue;
				}					
				
				File[] ServerXsds = EndPointServers[i].listFiles();
				xsds.addAll(Arrays.asList(ServerXsds));
			}
			else{
				System.out.println("--->JValid::Invalid XSD Path " + EndPointServers[i].getPath());
			}
		}		
		
		File[] listOfFiles = new File[xsds.size()];
		listOfFiles = xsds.toArray(listOfFiles);

		if( listOfFiles == null ) {
			System.out.println("--->JValid::Faild to find XSDs @ path: " + path);
		}
		else {
			for (int i = 0; i < listOfFiles.length; i++) {
				if (listOfFiles[i].isFile()) {
					if( !getFileExtension(listOfFiles[i]).equals("xsd") ){
						listOfFiles[i] = null;
						continue;
					}					
					if( m_Verbosity == 2 )
						System.out.println("--->JValid::File " + listOfFiles[i].getName());
				} else if (listOfFiles[i].isDirectory()) {
					if( m_Verbosity == 2 )
						System.out.println("--->JValid::Directory " + listOfFiles[i].getName());
				}
				else{
					System.out.println("--->JValid::Invalid XSD Path " + listOfFiles[i].getPath());
					listOfFiles = null;
					break;
				}
			}
			if( listOfFiles != null ) {
				//filereference = listOfFiles;
				try {
					populateListWithValidators(listOfFiles);
				} catch (Exception ex) {
					System.out.println("--->JValid::Exception: create validators: " +ex.toString());
					listOfFiles = null;//new File[0]; // return empty list
				}
			}
		}
		System.setProperty("user.dir", currdir);
		return listOfFiles;
	}

	//// populateListWithValidators
	private void populateListWithValidators(File[] listOfFiles) throws Exception
	{
		File currxsd = new File("n/a");
		try {
			SchemaFactory factory = SchemaFactory.newInstance("http://www.w3.org/2001/XMLSchema");
			for (int i = 0; i < listOfFiles.length; i++) {
				if( listOfFiles[i] == null )
					continue;
				currxsd = listOfFiles[i];
				Schema schema = factory.newSchema(currxsd);
				Validator validator = schema.newValidator();
				A.add(validator);
				validatorcontainer vtmp= new validatorcontainer();
				vtmp.valid   = validator;
				vtmp.xsdfile = listOfFiles[i].getName();
				V.add(vtmp);
			}
		} catch (Exception ex) {
			System.out.println("--->JValid::Exception: populateListWithValidators: " + currxsd.getPath());
			//throw new IOException("Failed to populate ListWith Validators");
			//throw new Exception(ex.toString());
			throw ex;
		}
	}
	
	/*  MultiSpeakRequestMsgHeader -
	 * 		'datetime':  2018-08-26T07:15:08-03:00
	 * 		'Context0':  is not facet-valid with respect to enumeration '[Development, Production, Study, Testing, Training, Other]'
	 * 		'cNameT'  :  is not facet-valid with respect to enumeration '[GlobalDomain, RegisteredName, SystemName, NounType, Other]'
	 * 		'regid'   :  is not facet-valid with respect to pattern '[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}' for type 'MultiSpeakGUID'
	 * 						644e1dd7-2a7f-18fb-b8ed-ed78c3f92c2b
	 * 
	 * 	  can only have one or the other of the following, else get:
	 * 			Invalid content was found starting with element 'request:DataSetState'. No child element is expected at this point.
	      <request:DoNotReply>
	      		<com:registrationID>644e1dd7-2a7f-18fb-b8ed-ed78c3f92c2b</com:registrationID>
	      </request:DoNotReply>
	      <request:DataSetState>
	      		<com:PublishDataSetState>
	      			<com:DataSetID>DS-ID-234</com:DataSetID>
	      			<com:PreviousDataSetID>DS-ID-233</com:PreviousDataSetID>
	      		</com:PublishDataSetState>
	      </request:DataSetState>
	 *
	 *  MultiSpeakResponseMsgHeader -
	 *  	'Other Attribute':  is not facet-valid with respect to enumeration '[0, 1, 2, 3, 4, 5, 6, 7, Other]'
	 *  	'level'          :  is not facet-valid with respect to enumeration '[Inform, Warning, Fatal, Catastrophic, Other]'
	 */
	public JReturn validate(String soap_xml) throws Exception {
		// chm 9.14.18 - parse both soap header and body since
		//				 the request:MultiSpeakMsgHeader is in there...
		boolean b_env = false;
		boolean b_bod = false;
		boolean b_hdr = false;
		boolean bFoundTNS = false;
		
		JParseSOAP jsoap = new JParseSOAP(m_Verbosity);
		String[] head_ret = jsoap.soap_head(soap_xml); // extract ms-part of hdr
		String head_xml = head_ret[0];
		if( head_xml.isEmpty() ) {
			throw new Exception( "Failed to extract Header" );
		}

		String[] body_ret = jsoap.soap_body(soap_xml); // extract soap body
		String body_xml = body_ret[0];
		if( body_xml.isEmpty() ) {
			throw new Exception( "Failed to extract Body" );
		}
		
		InputStream env_in = new ByteArrayInputStream(soap_xml.getBytes(StandardCharsets.UTF_8));
		InputStream head_in = new ByteArrayInputStream(head_xml.getBytes(StandardCharsets.UTF_8));
		InputStream body_in = new ByteArrayInputStream(body_xml.getBytes(StandardCharsets.UTF_8));

		Source soap_envelope = new StreamSource(env_in);
		Source ms_head       = new StreamSource(head_in);
		Source ms_body       = new StreamSource(body_in);
		for (validatorcontainer valid8: V) { //  set 'valid8' to each of the values in 'V' in turn.
			try {
				if (valid8.xsdfile.toLowerCase().indexOf("soapEnvelope".toLowerCase()) != -1) { // soap envelope file?
					if( m_Verbosity == 3 ) {
						System.out.println("Validating Soap Envelope through " + valid8.xsdfile);
						//System.out.println(soap_xml);
					}
					valid8.valid.validate(soap_envelope);
					b_env = true;
					if( m_Verbosity == 3 ) 
						System.out.println("--->Envelope Validated.");
				} 		
				else if ( valid8.xsdfile.toLowerCase().indexOf("MsgHeader".toLowerCase()) != -1) { // ms header file?{
					if( !b_hdr ) {
						// check if is 'request' or 'response'
						if (valid8.xsdfile.toLowerCase().indexOf(head_ret[1].toLowerCase()) != -1) {
							if( m_Verbosity == 3 ) {
								System.out.println("Validating Multispeak Header through " + valid8.xsdfile);
								//System.out.println(head_xml);
							}
							valid8.valid.validate(ms_head);
							b_hdr = true;
							if( m_Verbosity == 3 ) 
								System.out.println("--->Header Validated.");
						}
					}
				}
				else {
					if( !b_bod ) {
						// check if is right tns
						if (valid8.xsdfile.toLowerCase().indexOf(body_ret[1].toLowerCase()) != -1) {
							if( m_Verbosity == 3 ) {
								System.out.println("Validating Multispeak Body through " + valid8.xsdfile);
								//System.out.println(body_xml);
							}
							bFoundTNS = true;
							valid8.valid.validate(ms_body);
							b_bod = true;
							if( m_Verbosity == 3 ) 
								System.out.println("--->Body Validated by TargetNameSpace.");
						}
					}
				}
			} catch (Exception ex) {
				String str = ex.toString();
				System.out.println("--->JValid::exception validating: " + str);
				break;//body_in.reset();
			}
		}
		if (b_env && b_hdr && b_bod) {
			return JReturn.SUCCESS;
		} else {
			String err = "Failed to validate Body";
			if( !b_env )
				err = "Failed to validate Envelope";
			else if( !b_hdr )
				err = "Failed to validate Header";
			else if( !bFoundTNS )
				err = "Failed to Find TargetNameSpace";
			throw new Exception( err );
		}
	}

	//// fileToString
	public static String fileToString(File file)
	{
		try {
			if( file.exists() ) { 
				if( !file.isDirectory() ) { 
					byte[] encoded;
					encoded = Files.readAllBytes(file.toPath());
					return new String(encoded, StandardCharsets.UTF_8);
				}
				else{
					System.out.println("--->JValid::Exception fileToString: '" + file.getPath() + "' is a directory.");				
				}
			}
			else{
				System.out.println("--->JValid::Exception fileToString: '" + file.getPath() + "' does not exist.");				
			}
		}
		catch (Exception ex) {
			System.out.println("--->JValid::Exception fileToString: " + ex.toString());
			return null;
		}
		return null;
	}
	//// getFileExtension
    private static String getFileExtension(File file)
    {
       	return getFileExtension(file.getName());
    }
	//// getFileExtension
    private static String getFileExtension(String fileName)
    {
        if(fileName.lastIndexOf(".") != -1 && fileName.lastIndexOf(".") != 0)
        	return fileName.substring(fileName.lastIndexOf(".")+1);
        else 
        	return "";
    }
}
