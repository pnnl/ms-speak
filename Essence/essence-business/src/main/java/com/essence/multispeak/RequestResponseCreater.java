/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.multispeak;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.io.Writer;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

import org.apache.xmlbeans.XmlException;

import com.eviware.soapui.impl.wsdl.WsdlInterface;
import com.eviware.soapui.impl.wsdl.WsdlOperation;
import com.eviware.soapui.impl.wsdl.WsdlProject;
import com.eviware.soapui.impl.wsdl.support.wsdl.WsdlImporter;
import com.eviware.soapui.support.SoapUIException;

public class RequestResponseCreater {
	static private Logger logger = Logger.getLogger(RequestResponseCreater.class.getName());

	private WsdlProject project;

	public static void main(String args[]) {
		// For GetAssetsByAssetFields in AM
		// new RequestResponseCreater("C:\\Users\\pning\\Documents\\NRECA\\reading and research\\v5\\MultiSpeakV503RCEndpoints-WSDLfiles\\EndPoints\\AM_Server\\AM_Server-test.wsdl");
		
		// For PowerMonitorNotification in NOT
		//new RequestResponseCreater("C:\\Users\\pning\\Documents\\NRECA\\reading and research\\v5\\MultiSpeakV503RCEndpoints-WSDLfiles\\EndPoints\\NOT_Server\\NOT_Server-test.wsdl");
		
		// For MOD
		// GetParentConnectivity / GetUplineConnectivity / GetDownlineConnectivity / GetAllConnectivity

		if (args == null || args.length != 2) {
			System.out.println("Please use: java com.essence.multispeak.RequestResponseCreater wsdl_file_or_endpoints_dir_name_with_path output_dir_no_end_slash");
			System.exit(1);
		}
		
		List<String> wsdlFiles = getListOfWSDLs(args[0]);
		for (String wsdl : wsdlFiles)
			new RequestResponseCreater(wsdl, args[1]); //"C:\\Users\\pning\\Documents\\NRECA\\reading and research\\v5\\MultiSpeakV503RCEndpoints-WSDLfiles\\EndPoints\\MOD_Server\\MOD_Server-test.wsdl");
		System.exit(0);
	}

	static public List<String> getListOfWSDLs(String wsdlFileOrDir) {
		//String root = "C:\\Users\\pning\\Documents\\NRECA\\reading and research\\v5\\MultiSpeakV503RCEndpoints-WSDLfiles\\EndPoints";
		List<String> wsdlFileNames = new ArrayList<String>();
		File rootFile = new File(wsdlFileOrDir);
		
		if (rootFile.isFile()) {
			wsdlFileNames.add(wsdlFileOrDir);
		} else if (rootFile.isDirectory()) {
			File[] subDirs = rootFile.listFiles();
			for (int i=0; i<subDirs.length; i++) {
				try {
					System.out.println((i+1) + "- absPath=" + subDirs[i].getAbsolutePath() + "\tcanPath" + subDirs[i].getCanonicalPath() + "\tpath=" + subDirs[i].getPath() + "\tname=" + subDirs[i].getName());
					
					System.out.println("wsdl: " + getWSDLFile(subDirs[i]));
					if (getWSDLFile(subDirs[i]) != null)
						wsdlFileNames.add(subDirs[i].getAbsolutePath() + "\\" + getWSDLFile(subDirs[i]));
				} catch (IOException ex) {
					System.out.println("ERROR: " + ex.getMessage());
				}
			}
		}
		return wsdlFileNames;
	}

	// get first wsdl file in the directory, assuming there is only one
	static private String getWSDLFile(File dir) {
		if (dir == null || !dir.isDirectory())
			return null;
		File[] files = dir.listFiles();
		for (int i=0; i<files.length; i++)
			if (files[i].getName().equals(dir.getName()+".wsdl"))
				return files[i].getName();
		return null;
	}
	
	public RequestResponseCreater(String wsdlURL, String outputDir) {
		try {
			this.project = new WsdlProject();
			WsdlInterface[] wsdlInterfaces = WsdlImporter.importWsdl(project, wsdlURL);
			for (WsdlInterface wsdl : wsdlInterfaces) {
				createRequestsResponses(wsdl, outputDir);
			}
		} catch (XmlException e) {
			logger.severe("XML parsing error occurred during WSDL import: "
					+ e.getMessage());
		} catch (IOException e) {
			logger.severe("IO error occurred during WSDL import: "
					+ e.getMessage());
		} catch (SoapUIException e) {
			logger.severe("An error occurred in SoapUI during WSDL import: "
					+ e.getMessage());
			e.printStackTrace();
		} catch (Exception e) {
			e.printStackTrace();
			logger.severe("An unknown error occurred during WSDL import: "
					+ e.getMessage());
		}
	}

	public void createRequestsResponses(WsdlInterface wsdl, String outDir) {
		Writer writer = null;
		try {
			WsdlOperation[] wsdlOperations = getOperations(wsdl);
			for (WsdlOperation operation : wsdlOperations) {
				String request = operation.createRequest(true);
				String filename = outDir + "/" + operation.getName() + ".xml";
				writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filename), "utf-8"));
				writer.write(request);
				writer.flush();
				writer.close();
				
				String response = operation.createResponse(true);
				filename = outDir + "/" + operation.getName() + "Response.xml";
				writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filename), "utf-8"));
				writer.write(response);
				writer.flush();
				writer.close();
			}
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			try {
				if (writer != null)
					writer.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}

	public WsdlOperation[] getOperations(WsdlInterface wsdl) {
		WsdlOperation[] operations = new WsdlOperation[wsdl.getOperationCount()];
		for (int i=0; i < operations.length; i++)
			operations[i] = wsdl.getOperationAt(i);
		return operations;
	}
}
