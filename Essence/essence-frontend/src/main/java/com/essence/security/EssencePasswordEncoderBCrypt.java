/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.security;

import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

public class EssencePasswordEncoderBCrypt {
	static public void main(String[] args ) {
		if (args == null || args.length != 1) {
			System.out.println("Please use: EssencePasswordEncoderBCrypt password");
			System.exit(1);
		}
		BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
		System.out.println("Encoded password is: " + encoder.encode(args[0]));
	}

}
