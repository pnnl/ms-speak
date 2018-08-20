/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.security;

import org.springframework.security.authentication.encoding.ShaPasswordEncoder;

public class EssencePasswordEncoderSHA {
	static public void main(String[] args ) {
		if (args == null || args.length != 2) {
			System.out.println("Please use: EssencePasswordEncoderSHA username password");
			System.exit(1);
		}
		ShaPasswordEncoder encoder = new ShaPasswordEncoder(256);
		String hash = encoder.encodePassword(args[1], args[0]); // pwd, salt
		System.out.println("Encoded password for " + args[0] + "/" + args[1] + " is: " + hash);
	}
}
