
import java.io.InputStream;
import java.io.ByteArrayInputStream;
import java.nio.charset.StandardCharsets;
import javax.xml.soap.MessageFactory;
import javax.xml.soap.SOAPMessage;
import javax.xml.soap.SOAPBody;
import javax.xml.soap.SOAPHeader;
import javax.xml.soap.SOAPEnvelope;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.TransformerFactory;
import java.io.StringWriter;
//import java.nio.charset.Charset;
//import javax.xml.soap.MimeHeaders;
//import java.util.Iterator;
//convert body to string

public class JParseSOAP {

	public String soap_me(String xmlfromwire) {
		SOAPMessage wire;
		String message = new String();
		InputStream in = new ByteArrayInputStream(
				xmlfromwire.getBytes(StandardCharsets.UTF_8));
		try {
			in.reset();
			// MessageFactory factory = MessageFactory.newInstance();
			wire = MessageFactory.newInstance().createMessage(null, in);
			SOAPEnvelope env = wire.getSOAPPart().getEnvelope();
			SOAPHeader head = env.getHeader();
			head.detachNode();
			// SOAPBody sb = env.getBody();
			SOAPBody sb = wire.getSOAPBody();
			// wire.writeTo(System.out);

			SOAPBody element = sb;
			DOMSource source = new DOMSource(element.extractContentAsDocument());
			StringWriter stringResult = new StringWriter();
			TransformerFactory.newInstance().newTransformer()
					.transform(source, new StreamResult(stringResult));
			message = stringResult.toString();

		} catch (Exception ex) {
			System.out.println("exception: " + ex.toString());
		}

		return message;
	}

}
