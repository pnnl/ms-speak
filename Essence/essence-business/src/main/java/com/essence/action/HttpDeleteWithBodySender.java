/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.action;

import java.net.URI;

import org.apache.http.client.methods.HttpEntityEnclosingRequestBase;
import org.apache.http.client.methods.HttpUriRequest;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
import org.springframework.web.client.RestTemplate;

public class HttpDeleteWithBodySender {

	RestTemplate restTemplate = new RestTemplate();

	public static class HttpEntityEnclosingDeleteRequest extends HttpEntityEnclosingRequestBase {

	    public HttpEntityEnclosingDeleteRequest(final java.net.URI uri) {
	        super();
	        setURI(uri);
	    }

	    @Override
	    public String getMethod() {
	        return "DELETE";
	    }
	}

	public String bodyWithDeleteRequest(String url, String deleteBody) throws Exception {
	    restTemplate.setRequestFactory(new HttpComponentsClientHttpRequestFactory() {
	        @Override
	        protected HttpUriRequest createHttpUriRequest(HttpMethod httpMethod, URI uri) {
	            if (HttpMethod.DELETE == httpMethod) {
	                return new HttpEntityEnclosingDeleteRequest(uri);
	            }
	            return super.createHttpUriRequest(httpMethod, uri);
	        }
	    });

	    ResponseEntity<String> exchange = restTemplate.exchange(
	            url,
	            HttpMethod.DELETE,
	            new HttpEntity<String>(deleteBody),
	            String.class);
	    return exchange.toString();
	} 
}
