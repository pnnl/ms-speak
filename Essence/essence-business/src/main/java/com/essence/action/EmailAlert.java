/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.action;
import java.util.*;

import javax.mail.*;
import javax.mail.internet.*;
// note: running this successfully requires 
// adding -Djava.net.preferIPv4Stack=true to the VM options
// Java 7 defaults to using IPv6 address which can cause a failure when sending

public class EmailAlert  {
	private String fromAddress = "essence@cigital.com";
	private String toAddress = "";
	private Properties properties;
	private String subject = "";
	
	public EmailAlert () {
		this.properties = System.getProperties();
		// set the SMTP server. 10.11.1.10 is internal cigital (whitebox)
		// use 192.168.2.105 for use on the essence machine
		// TODO: add some logic which chooses the correct address
		this.properties.setProperty("mail.smtp.host", "10.11.1.10");
	}
	   
	public void setDestinationAddress (String address) {
		this.toAddress = address;
	}
	
	public void setSubjectString (String subject) {
		this.subject = subject;
	}
	
	public void sendMessage (String body) {
		 Session session = Session.getDefaultInstance(properties);
		 
		 try{
	         // Create a default MimeMessage object.
	         MimeMessage message = new MimeMessage(session);

	         // Set From: header field of the header.
	         message.setFrom(new InternetAddress(fromAddress));

	         // Set To: header field of the header.
	         message.addRecipient(Message.RecipientType.TO,
	                                  new InternetAddress(toAddress));

	         // Set Subject: header field
	         message.setSubject(subject);

	         // Now set the actual message
	         message.setText(body);

	         // Send message
	         Transport.send(message);
	         System.out.println("Sent message successfully....");
	      	}catch (MessagingException mex) {
	         System.out.println("Email notification not sent successfully");
	      	}
	  }
	
	public static void main(String[] args) {
		System.out.println("test");
		EmailAlert a = new EmailAlert();
		a.setDestinationAddress("pning@cigital.com");
		a.setSubjectString("Alert Message from ESSENCE");
		a.sendMessage("A manual intervention is required\n A high severity endpoint rule has been violated");
	}
}

	     
