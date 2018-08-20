package com.essence.security;

import org.springframework.security.authentication.encoding.ShaPasswordEncoder;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

public class PasswordEncoderTest {
	static public void main(String[] args ) {
		testBCrypt();
	}

    @SuppressWarnings("unused")
	static private void testSha() {
		ShaPasswordEncoder encoder = new ShaPasswordEncoder();
		String hash = encoder.encodePassword("test1", "test1"); // pwd, salt
		System.out.println("test1:" + hash);
		System.out.println("test2:" + encoder.encodePassword("test2", "test2"));
		
		ShaPasswordEncoder encoder1 = new ShaPasswordEncoder(256);
		String hash1 = encoder1.encodePassword("test1", "test1"); // pwd, salt
		System.out.println("test1-256:" + hash1);
	}
	
	/*
	 * http://stackoverflow.com/questions/6832445/how-can-bcrypt-have-built-in-salts
	 * 
	 * $2a$12$LYKaTlqPsACr2MElcKSXguzosaY9m.vQWvowG683HttDXlP8X.N56
	 * 
2a identifies the bcrypt algorithm version that was used.
10 is the cost factor; 2^10 iterations of the key derivation function are used (which is not enough, 
by the way. I'd recommend a cost of 12 or more.)
vI8aWBnW3fID.ZQ4/zo1G.  q1lRps.9cGLcZEiGDMVr5yUP1KUOYTa is the salt and the cipher text, concatenated and encoded in a 
modified Base-64. The first 22 characters decode to a 16-byte value for the salt. The remaining characters are cipher text to be compared for authentication.
$ are used as delimiters for the header section of the hash.
2+2+3+22+31=60

http://stackoverflow.com/questions/8521251/spring-securitypassword-encoding-in-db-and-in-applicationconext
<authentication-manager alias="authenticationManager">
   <authentication-provider>
    <password-encoder ref="encoder"/>
    <jdbc-user-service data-source-ref="dataSource"
       users-by-username-query="
          select username,password, enabled 
          from principal where username=?" 
       authorities-by-username-query="
          select p.username, a.authority from principal p, authority a
          where p.id = a.principal_id and p.username=?" 
    />
   </authentication-provider>
</authentication-manager> 

  <beans:bean id="encoder" class="org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder"/>
  
	 */
	static private void testBCrypt() {
		BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
		System.out.println("10-test1234:" + encoder.encode("test1234"));
		System.out.println("10-test1234:" + encoder.encode("test1234"));
		System.out.println("10-test1234:" + encoder.encode("test1234"));
		System.out.println("10-test1234:" + encoder.encode("test1234"));
		
		BCryptPasswordEncoder encoder1 = new BCryptPasswordEncoder(12);
		System.out.println("12-test1234:" + encoder1.encode("test1234"));
	}

}
