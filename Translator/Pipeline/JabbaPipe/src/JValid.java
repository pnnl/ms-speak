
import java.io.File;
import java.io.InputStream;
import java.io.ByteArrayInputStream;
import java.util.ArrayList;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
//import com.saxonica.Validate;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.*;
import javax.xml.transform.Source;
import javax.xml.transform.stream.StreamSource;

  /**
  EXAMPLE:
        JValid JV = new JValid("v3/SchemaExtracted");

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


public class JValid {

	private class validatorcontainer {
		Validator valid;
		String xsdfile;
	}
	private ArrayList <Validator>A;
	private ArrayList <validatorcontainer>V;
	private File[] filereference;

	public JValid(String path) {
		A =  new ArrayList<Validator>();
		V = new ArrayList<validatorcontainer>();
		File[] xsds = get_xsd_files(path);
	}
 
	private File[] get_xsd_files (String path)
 	{
	    File folder = new File(path);
	    File[] listOfFiles = folder.listFiles();

	    for (int i = 0; i < listOfFiles.length; i++) {
      	        if (listOfFiles[i].isFile()) {
					System.out.println("File " + listOfFiles[i].getName());
                } else if (listOfFiles[i].isDirectory()) {
					System.out.println("Directory " + listOfFiles[i].getName());
                }
            }
            filereference = listOfFiles;
	    try {
			populateListWithValidators(listOfFiles);
	    } catch (Exception ex) {
			System.out.println("create validators: " +ex.toString());
	    }
	    return listOfFiles;
	}

	public JValid() {
    }

    // only use with default constructor
	public void init_xsds(String xsdpath) {
		   A =  new ArrayList<Validator>();
		   V = new ArrayList<validatorcontainer>();
		   File[] xsds = get_xsd_files(xsdpath);
	}
	
	private void populateListWithValidators(File[] listOfFiles) throws Exception
	{
		SchemaFactory factory = SchemaFactory.newInstance("http://www.w3.org/2001/XMLSchema");
		for (int i = 0; i < listOfFiles.length; i++) {
			//  File schemaLocation = new File("envelope.xml");
			Schema schema = factory.newSchema(listOfFiles[i]);
			Validator validator = schema.newValidator();
			A.add(validator);
			validatorcontainer vtmp= new validatorcontainer();
			vtmp.valid   = validator;
			vtmp.xsdfile = listOfFiles[i].getName();
			V.add(vtmp);
		}	
	}	

	// first attempt at validation
	private void validate(File target) throws Exception {
		Source source = new StreamSource(target);
		for (validatorcontainer validate: V) {
			//chm-System.out.println("validating: " + validate.xsdfile + "\n");
			try {
				validate.valid.validate(source);
			} catch (Exception ex) {
				// ignore soap:Envelope not declared in v3
				String str = ex.toString();
				//if (str.indexOf("soap:Envelope") < 0) {
				//chm-System.out.println("exception validating: " + str);
				//}
			}
		}
	}

	// bring in xml from memory string
	public boolean validate(String soap_xml) throws Exception {
		Exception valid_ex = new Exception();
		boolean b_env = false;
		boolean b_sch = false;

		JParseSOAP jsoap = new JParseSOAP();
		String target = jsoap.soap_me(soap_xml);

		InputStream in = new ByteArrayInputStream(target.getBytes(StandardCharsets.UTF_8));
		InputStream env_in = new ByteArrayInputStream(soap_xml.getBytes(StandardCharsets.UTF_8));

 		Source source     = new StreamSource(in);
 		Source source_env = new StreamSource(env_in);
		for (validatorcontainer validate: V) {
			//chm-System.out.println("validating: " + validate.xsdfile + "\n");
			try {
				in.reset();
				if (validate.xsdfile.indexOf("envelope") != -1) {
					validate.valid.validate(source_env);
					b_env = true;
				} else {
					validate.valid.validate(source);
					b_sch = true;
				}
			} catch (Exception ex) {
				// ignore soap:Envelope not declared in v3
				String str = ex.toString();
				//if (str.indexOf("soap:Envelope") < 0) {
				//chm-System.out.println("exception validating: " + str);
				valid_ex = ex;
				//}
			}
		}
		if (b_env && b_sch) {
		    return true;
		} else {
			throw valid_ex;
		}
	}

	//test function
	public static String fileToString(File file)
	{
		byte[] encoded;
	   
		try { 
			encoded = Files.readAllBytes(file.toPath());
		}
		catch (Exception ex) {
		  //chm-System.out.println("Exception fileToString: " + ex.toString());
		  return ex.toString();		
		}
 		 return new String(encoded, StandardCharsets.UTF_8);
	}
}
