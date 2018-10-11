
import java.io.InputStream;
import java.io.ByteArrayInputStream;
import java.io.StringWriter;
import java.nio.charset.StandardCharsets;
import java.util.Iterator;

import javax.xml.soap.MessageFactory;
import javax.xml.soap.SOAPMessage;
import javax.xml.soap.SOAPEnvelope;
import javax.xml.soap.SOAPHeader;
import javax.xml.soap.SOAPBody;
import javax.xml.soap.SOAPBodyElement;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.TransformerFactory;

import org.w3c.dom.NodeList;
import org.w3c.dom.Document;
import org.w3c.dom.Node;

//convert body to string
public class JParseSOAP {

	private int m_Verbosity;
	// constructors
	public JParseSOAP(int Verbosity) {
		m_Verbosity = Verbosity;
	}
	
	public String[] soap_body(String xmlfromwire) {
        String retvals[] = new String[2];
        retvals[0] = "";
        retvals[1] =  "error";
        boolean bFoundTns=false;
        boolean bGotTns=false;

		SOAPMessage wire;

		InputStream in = new ByteArrayInputStream(xmlfromwire.getBytes(StandardCharsets.UTF_8));
		try {
			in.reset();
			wire = MessageFactory.newInstance().createMessage(null, in);
			SOAPEnvelope envelope = wire.getSOAPPart().getEnvelope();
			SOAPHeader header = envelope.getHeader();
			header.detachNode();
			
			// wire.writeTo(System.out);
			SOAPBody soapBody = wire.getSOAPBody();
			
			@SuppressWarnings("rawtypes")
			Iterator itr=soapBody.getChildElements();
			while (itr.hasNext()) {
			    Node node=(Node)itr.next();		    
			    if (node.getNodeType()==Node.ELEMENT_NODE) {
		            SOAPBodyElement element = (SOAPBodyElement)node;
			        //Element ele=(Element)node;
			        //System.out.println(ele.getNodeName() + " = " + ele.getTextContent());// tns:InitiateConnectDisconnect = tns:InitiateConnectDisconnect =
					Iterator<?> nameSpace = element.getNamespacePrefixes();
					while ( nameSpace.hasNext() )
					{
						String prefix = (String)nameSpace.next(); 
						String tns = element.getNamespaceURI( prefix ); // "http://www.multispeak.org/V5.0/wsdl/CD_Server"
						// NOTE: the prefix is not required to 'tns', could be anything, so probably better to match on URI
						if( prefix.equals("tns") ) { // tns stands for 'TargetNameSpace'
							bGotTns = true;
						}
						// TODO: the wsdl path could be passed down from MultiSpeaker....
						else if( tns.toLowerCase().indexOf("www.multispeak.org/V5.0/wsdl/".toLowerCase()) != -1){
							bGotTns = true;
						}
						if( bGotTns ){ 
							int idx = tns.lastIndexOf("/");
					        if( idx != -1 ){
					        	retvals[1] = tns.substring(idx+1);
					        	bFoundTns = true;
					        	break;
					        }
						}
					}			        
			    } else if (node.getNodeType()==Node.TEXT_NODE) {
			        //do nothing here most likely, as the response nearly never has mixed content type
			        //this is just for your reference
			    }
			    if( bGotTns )
			    	break;
			}
			if( bFoundTns ){
				// 9.15.18, remove 'standalone'
				Document doc = soapBody.extractContentAsDocument();
				doc.setXmlStandalone(true);
				DOMSource source = new DOMSource(doc);
				//DOMSource source = new DOMSource(BodyElem.extractContentAsDocument());
				StringWriter stringResult = new StringWriter();
				TransformerFactory.newInstance().newTransformer().transform(source, new StreamResult(stringResult));
				if( m_Verbosity > 3 ) {
					System.out.println("--->JParseSOAP::Body: " + stringResult.toString());
				}
				retvals[0] = stringResult.toString();
			}
			else{
				throw new Exception( "Failed to Extract TargetNameSpace." );
			}
		} catch (Exception ex) {
			System.out.println("--->JParseSOAP::exception: " + ex.toString());
		}

		return retvals;
	}

	public String[] soap_head(String xmlfromwire) {
		SOAPMessage wire;
        String retvals[] = new String[2];
        retvals[0] = "";
        retvals[1] =  "error";
 
		InputStream in = new ByteArrayInputStream(xmlfromwire.getBytes(StandardCharsets.UTF_8));
		try {
			in.reset();
			wire = MessageFactory.newInstance().createMessage(null, in);
			SOAPEnvelope envelope = wire.getSOAPPart().getEnvelope();
			SOAPHeader header = envelope.getHeader();
			header.detachNode();
			
	        NodeList nl = header.getChildNodes();
	        int numnodes = nl.getLength();
	        for(int i = 0; i < numnodes; i++) {
	        	Node node = nl.item(i);
	        	short nt=node.getNodeType(); 
	        	if( nt != Node.ELEMENT_NODE ) {// TEXT_NODE	3
	        		continue;
	        	}
	        	String LocalName = node.getLocalName();
	        	if( LocalName == null ) {
	        		continue;
	        	}

	        	if( LocalName.equals("MultiSpeakRequestMsgHeader") ||
	        		LocalName.equals("MultiSpeakResponseMsgHeader") ){        		
					DOMSource source = new DOMSource(node);
					StringWriter stringResult = new StringWriter();
					TransformerFactory.newInstance().newTransformer().transform(source, new StreamResult(stringResult));
					if( m_Verbosity > 3 ) {
						System.out.println("--->JParseSOAP::Header" + stringResult.toString());
					}
					if( LocalName.equals("MultiSpeakRequestMsgHeader") )
						retvals[1] = "Request";
					else	
						retvals[1] = "Response";
			        retvals[0] = stringResult.toString();
					break;
		        }
	        }

		} catch (Exception ex) {
			System.out.println("--->JParseSOAP::exception: " + ex.toString());
			System.out.println(xmlfromwire);
		}

		return retvals;
	}
}
