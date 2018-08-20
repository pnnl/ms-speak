/*
Copyright (C) 2014-2016, National Rural Electric Cooperative Association and Cigital, Inc
*/
package com.essence.action;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.logging.Logger;

import org.apache.log4j.xml.DOMConfigurator;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.http.converter.json.MappingJacksonHttpMessageConverter;
import org.springframework.web.client.RestTemplate;

import com.essence.persistence.DAOUtil;
import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.google.gson.JsonElement;

@SuppressWarnings("unused")
public class SDNControllerNBI {
	public static final Logger log = Logger.getLogger(SDNControllerNBI.class.getName()); 
	
	String REST_HOST_URL = "http://127.0.0.1:8080";
	
	public static void main(String[] args) {
		//DOMConfigurator.configure("log4j.xml");

		SDNControllerNBI api = DAOUtil.getSDNControllerNBI();
		/*
		System.out.println(api.get(REST_HOST+"/wm/topology/switchclusters/json"));
		List<String> devices = api.getDevices();
		for (int i=0; i<devices.size(); i++)
			System.out.println("IP=" + devices.get(i));
		List<Device> deviceList = api.getAllDevices();
		for (int i=0; i<deviceList.size(); i++)
			deviceList.get(i).print();
			*/
		/*
		api.enableFirewall(false);
		System.out.println("Is firewall on? " + api.isFirewallOn());
		List<SDNRule> rules = api.getAllRules();
		for (SDNRule r : rules)
			System.out.println(r.getPrintString());
			*/
		//System.out.println("deleting all firewall rules");
		//api.deleteAllRules();
		System.out.println("Is firewall on? " + api.isFirewallOn());
		System.out.println("after deletion, result from querying all rules:");
		List<SDNRule> rules = api.getAllRules();
		for (SDNRule r : rules)
			System.out.println(r.getPrintString());
		System.out.println("Turn off firewall? " + api.enableFirewall(false));
		
//		System.out.println("Remove rule 437518049 result: " + api.deleteRule(437518049));
	}
	
	public boolean isFirewallOn() {
		String result = get(REST_HOST_URL + "/wm/firewall/module/status/json");
		if (result == null)
			return false;
		
		Gson gson = new Gson();
		JSONFirewallStatusResult resultObj = gson.fromJson(result, JSONFirewallStatusResult.class);
		//System.out.println("result = " + result);
		//System.out.println("resultObj = " + resultObj.getResult());
		if (resultObj.getResult() != null && resultObj.getResult().contains("firewall disabled"))
			return false;
		else
			return true;
	}
	
	public Map<String, List<String>> getAllSwitches() {
		String json = get(REST_HOST_URL + "/wm/topology/switchclusters/json");
		Map<String, List<String>> sc = new HashMap<String, List<String>>(); 
		if (json == null)
			return sc;
		
		JsonParser parser = new JsonParser();
		JsonElement je = parser.parse(json);
		if (je != null) {
			JsonObject jo = je.getAsJsonObject();
			if (jo != null) {
				Set<Map.Entry<String,JsonElement>> set = jo.entrySet();
				Iterator<Map.Entry<String,JsonElement>> it = set.iterator();
				while (it.hasNext()) {
					Map.Entry<String,JsonElement> obj = it.next();
					String key = obj.getKey();
					List<String> list = new ArrayList<String>(); 
					JsonElement value = obj.getValue();
					JsonArray ja = value.getAsJsonArray();
					for (int i=0; i<ja.size(); i++) {
						list.add(ja.get(i).getAsString());
					}
					sc.put(key, list);
				}
			}
		}
		return sc;
	}
	
	// old not working anymore
	public List<String> getDevices2() {
		String json = get(REST_HOST_URL + "/wm/devicemanager/device/all/json");
		List<String> devices = new ArrayList<String>();
		if (json == null)
			return devices;
		
		System.out.println("from getDevice2:\n"+json);
		int idx = json.indexOf("ipv4");
		while (idx > -1) {
			String s = json.substring(idx+8, idx+18);
			if (s != null && s.contains("172"))
				devices.add(s);
			json = json.substring(idx+19);
			idx = json.indexOf("ipv4");
		}
		return devices;
	}

	//TODO - parse the json properly into objects
	public List<String> getDevices() {
		String json = get(REST_HOST_URL + "/wm/device/");
		List<String> devices = new ArrayList<String>();
		if (json == null)
			return devices;
		
		System.out.println(json);
		int idx = json.indexOf("ipv4");
		while (idx > -1) {
			String s = json.substring(idx+8, idx+18);
			if (s != null && s.contains("172"))
				devices.add(s);
			json = json.substring(idx+19);
			idx = json.indexOf("ipv4");
		}
		return devices;
	}

	//TODO - parse the json properly into objects
	public List<Device> getAllDevices() {
		String json = get(REST_HOST_URL + "/wm/device/");
		/*
		List<String> devices = new ArrayList<String>();
		System.out.println(json);
		int idx = json.indexOf("ipv4");
		while (idx > -1) {
			String s = json.substring(idx+8, idx+18);
			if (s != null && s.contains("172"))
				devices.add(s);
			json = json.substring(idx+19);
			idx = json.indexOf("ipv4");
		}
		return devices;
		*/
//		String json = get(REST_HOST + "/wm/firewall/rules/json");
		List<Device> list = new ArrayList<Device>(); 
		if (json == null)
			return list;
		
		JsonParser parser = new JsonParser();
		JsonArray array = parser.parse(json).getAsJsonArray();
		Gson gson = new Gson();
		for ( int i=0; i<array.size(); i++) {
			Device device = gson.fromJson(array.get(i), Device.class);
			list.add(device);
		}
		
		return list;
	}

	public List<SDNRule> getAllRules() {
		String json = get(REST_HOST_URL + "/wm/firewall/rules/json");
		List<SDNRule> list = new ArrayList<SDNRule>(); 
		if (json == null)
			return list;
		
		JsonParser parser = new JsonParser();
		JsonArray array = parser.parse(json).getAsJsonArray();
		Gson gson = new Gson();
		for ( int i=0; i<array.size(); i++) {
			SDNRule rule = gson.fromJson(array.get(i), SDNRule.class);
			list.add(rule);
		}
		
		return list;
	}
	
	private String get(String urlStr) {
		HttpURLConnection conn = null;
		try {

			URL url = new URL(urlStr);
			conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("GET");
			conn.setRequestProperty("Accept", "application/json");

			if (conn == null) {
				//throw new RuntimeException("Failed : cannot connect to server");
				log.warning("Failed : cannot connect to server");
				return null;
			}

			if (conn.getResponseCode() != 200) {
				//throw new RuntimeException("Failed : HTTP error code : " + conn.getResponseCode());
				log.warning("Failed : HTTP error code : " + conn.getResponseCode());
				return null;
			}

			BufferedReader br = new BufferedReader(new InputStreamReader(
					(conn.getInputStream())));

			String output;
			while ((output = br.readLine()) != null) {
				return output;
			}
			
		} catch (MalformedURLException e) {
			log.warning(e.getMessage());
			return null;
//			return e.getMessage();
		} catch (IOException e) {
			log.warning(e.getMessage());
			return null;
//			return e.getMessage();			
		} finally {
			if (conn != null)
				conn.disconnect();
		}
		return null;
	}
	
	public String enableFirewall(boolean on) {
		HttpURLConnection conn = null;
		try {
			String urlString = REST_HOST_URL + "/wm/firewall/module/enable/json";
			if (on == false)
				urlString = REST_HOST_URL + "/wm/firewall/module/disable/json";

			URL url = new URL(urlString);
			conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("GET");
			conn.setRequestProperty("Accept", "application/json");

			if (conn.getResponseCode() != 200) {
				throw new RuntimeException("Failed : HTTP error code : " + conn.getResponseCode());
			}

			BufferedReader br = new BufferedReader(new InputStreamReader(
					(conn.getInputStream())));

			String output;
			while ((output = br.readLine()) != null) {
				return output;
			}
			
		} catch (MalformedURLException e) {

			return e.getMessage();
		} catch (IOException e) {

			return e.getMessage();
			
		} finally {
			conn.disconnect();
		}
		return null;
	}

	public String enableFirewallTraffic4Switch (String bigSwitch) {
		HttpURLConnection conn = null;
		try {
			URL url = new URL(REST_HOST_URL + "/wm/firewall/rules/json");
			conn = (HttpURLConnection) url.openConnection();
			conn.setDoOutput(true);
			conn.setRequestMethod("POST");
			conn.setRequestProperty("Content-Type", "application/json");
			String input = "{\"switchid\": \"" + bigSwitch + "\"}";

			OutputStream os = conn.getOutputStream();
			os.write(input.getBytes());
			os.flush();
			BufferedReader br = new BufferedReader(new InputStreamReader(
					(conn.getInputStream())));

			String output;
			while ((output = br.readLine()) != null) {
				return output;
			}
			
		} catch (MalformedURLException e) {

			return e.getMessage();
		} catch (IOException e) {

			return e.getMessage();
			
		} finally {
			conn.disconnect();
		}
		return null;
	}

	public String blockTrafficBetweenHosts (String hostIp1, String hostIp2) {
		HttpURLConnection conn = null;
		try {
			URL url = new URL(REST_HOST_URL + "/wm/firewall/rules/json");
			conn = (HttpURLConnection) url.openConnection();
			conn.setDoOutput(true);
			conn.setRequestMethod("POST");
			conn.setRequestProperty("Content-Type", "application/json");
			/*"field":"value" pairs below in any order and combination: 
			"switchid":"<xx:xx:xx:xx:xx:xx:xx:xx>", "src-inport":"<short>",  
			"src-mac": "<xx:xx:xx:xx:xx:xx>", "dst-mac": "<xx:xx:xx:xx:xx:xx>",  
			"dl-type": "<ARP or IPv4>", "src-ip": "<A.B.C.D/M>", "dst-ip": "<A.B.C.D/M>",  
			"nw-proto": "<TCP or UDP or ICMP>", "tp-src": "<short>", "tp-dst": "<short>",  
			"priority": "<int>", "action": "<ALLOW or DENY>" 
			Note: specifying src-ip/dst-ip without specifying dl-type as ARP, or specifying any IP-based nw-proto will automatically set dl-type to match IPv4.
			*/ 
			String input = "{\"src-ip\":\"" + hostIp1 + "\"," + "\"dst-ip\":\"" + hostIp2 + "\"," + "\"action\":\"DENY\"}";
			//System.out.println("post rule input=" + input);

			OutputStream os = conn.getOutputStream();
			os.write(input.getBytes());
			os.flush();
			BufferedReader br = new BufferedReader(new InputStreamReader(
					(conn.getInputStream())));

			String output;
			while ((output = br.readLine()) != null) {
				log.info(output);
			}
			
			return input;
			
		} catch (MalformedURLException e) {
			log.warning(e.getMessage());
			return null;
		} catch (IOException e) {
			log.severe(e.getMessage());
			return null;
		} finally {
			conn.disconnect();
		}
	}

	public String blockTrafficAtDest (String toDestHostIp) {
		HttpURLConnection conn = null;
		try {
			URL url = new URL(REST_HOST_URL + "/wm/firewall/rules/json");
			conn = (HttpURLConnection) url.openConnection();
			conn.setDoOutput(true);
			conn.setRequestMethod("POST");
			conn.setRequestProperty("Content-Type", "application/json");
			/*"field":"value" pairs below in any order and combination: 
			"switchid":"<xx:xx:xx:xx:xx:xx:xx:xx>", "src-inport":"<short>",  
			"src-mac": "<xx:xx:xx:xx:xx:xx>", "dst-mac": "<xx:xx:xx:xx:xx:xx>",  
			"dl-type": "<ARP or IPv4>", "src-ip": "<A.B.C.D/M>", "dst-ip": "<A.B.C.D/M>",  
			"nw-proto": "<TCP or UDP or ICMP>", "tp-src": "<short>", "tp-dst": "<short>",  
			"priority": "<int>", "action": "<ALLOW or DENY>" 
			Note: specifying src-ip/dst-ip without specifying dl-type as ARP, or specifying any IP-based nw-proto will automatically set dl-type to match IPv4.
			*/ 
			String input = "{\"dst-ip\":\"" + toDestHostIp + "\"," + "\"action\":\"DENY\"}";
			//System.out.println("post rule input=" + input);

			OutputStream os = conn.getOutputStream();
			os.write(input.getBytes());
			os.flush();
			BufferedReader br = new BufferedReader(new InputStreamReader(
					(conn.getInputStream())));

			String output;
			while ((output = br.readLine()) != null) {
				log.info(output);
			}
			
			return input;
			
		} catch (MalformedURLException e) {
			log.warning(e.getMessage());
			return null;
		} catch (IOException e) {
			log.severe(e.getMessage());
			return null;
		} finally {
			conn.disconnect();
		}
	}

	public String blockTrafficAtSource (String fromHostIp) {
		HttpURLConnection conn = null;
		try {
			URL url = new URL(REST_HOST_URL + "/wm/firewall/rules/json");
			conn = (HttpURLConnection) url.openConnection();
			conn.setDoOutput(true);
			conn.setRequestMethod("POST");
			conn.setRequestProperty("Content-Type", "application/json");
			/*"field":"value" pairs below in any order and combination: 
			"switchid":"<xx:xx:xx:xx:xx:xx:xx:xx>", "src-inport":"<short>",  
			"src-mac": "<xx:xx:xx:xx:xx:xx>", "dst-mac": "<xx:xx:xx:xx:xx:xx>",  
			"dl-type": "<ARP or IPv4>", "src-ip": "<A.B.C.D/M>", "dst-ip": "<A.B.C.D/M>",  
			"nw-proto": "<TCP or UDP or ICMP>", "tp-src": "<short>", "tp-dst": "<short>",  
			"priority": "<int>", "action": "<ALLOW or DENY>" 
			Note: specifying src-ip/dst-ip without specifying dl-type as ARP, or specifying any IP-based nw-proto will automatically set dl-type to match IPv4.
			*/ 
			String input = "{\"src-ip\":\"" + fromHostIp + "\"," + "\"action\":\"DENY\"}";
			//System.out.println("post rule input=" + input);

			OutputStream os = conn.getOutputStream();
			os.write(input.getBytes());
			os.flush();
			BufferedReader br = new BufferedReader(new InputStreamReader(
					(conn.getInputStream())));

			String output;
			while ((output = br.readLine()) != null) {
				log.info(output);
			}
			
			return input;
			
		} catch (MalformedURLException e) {
			log.warning(e.getMessage());
			return null;
		} catch (IOException e) {
			log.severe(e.getMessage());
			return null;
		} finally {
			conn.disconnect();
		}
	}

	public void deleteAllRules() {
		List<SDNRule> rules = getAllRules();
		for (SDNRule r : rules) 
			System.out.println("deleting rule id = " + r.getRuleid() + ": " + deleteRule(r.getRuleid()));
	}
	
	public String deleteRule (int ruleid) {
			/*
			 *  curl -X DELETE -d '{"ruleid": "-148286744"}' http://10.11.1.49:8080/wm/firewall/rules/json
			 */
			String input = "{\"ruleid\": \"" + ruleid + "\"}";
			String output = null;
			HttpDeleteWithBodySender sender = new HttpDeleteWithBodySender();
			try {
				output = sender.bodyWithDeleteRequest(REST_HOST_URL + "/wm/firewall/rules/json", input);
			} catch (Exception e) {
				e.printStackTrace();
			}
			return output;
	}

	public String getREST_HOST_URL() {
		return REST_HOST_URL;
	}

	public void setREST_HOST_URL(String rEST_HOST_URL) {
		REST_HOST_URL = rEST_HOST_URL;
	}

}
