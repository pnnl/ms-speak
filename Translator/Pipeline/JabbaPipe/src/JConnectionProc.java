
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;
import java.net.Socket;
import java.net.ServerSocket;


public class JConnectionProc implements Runnable
{


	Socket clientsock;


	public JConnectionProc(Socket ss) {
	  	  clientsock = ss;
	}

	  public void run()
	  {
	  	  PrintWriter out;
	  	  String inputLine;
	  	  //BufferedReader in;
	  	  InputStream in;
	  	  try {

	  	  out = new PrintWriter(clientsock.getOutputStream(), true);
	  	  //in  = new BufferedReader(new InputStreamReader(clientsock.getInputStream()));
	  	  in  = clientsock.getInputStream();

	  	  } catch (Exception ex) {

	  	      System.out.println("Failed input: " + ex.toString());
		       return;
	  	  }

                      Socket p80 = null;
	  	  try {
                      p80 = new Socket("localhost", 8080);
                      PrintWriter out80 = new PrintWriter(p80.getOutputStream(), true);
                      //BufferedReader in80  = new BufferedReader(new InputStreamReader(p80.getInputStream()));
                      InputStream in80  = p80.getInputStream();
		                ForwardResponse fr = new ForwardResponse(in80, out);
                (new Thread(fr)).start();

		byte[] bb = new byte[4096];
		int inputlen;
		      //while ((inputLine = in.readLine()) != null) {
		      while ((inputlen = in.read(bb)) > 0) {
			// send via port 80 socket.
			      inputLine = new String(bb, 0, inputlen);
		              System.out.println(inputLine);
		              out80.print( inputLine);
                              out80.flush();
		            }
		 } catch (Exception ex) {
		            System.out.println("Failed loop: " + ex.toString());
		            return;
	
        }
	   
	   if (p80 != null){
		try {
               p80.close();   
               clientsock.close();   
                 } catch (Exception ex) {
		    System.out.println("Failed: " + ex.toString());

                 }
            }   
	  } // end run()




public class ForwardResponse implements Runnable
{
	//BufferedReader in;
	InputStream in;
    PrintWriter out;
	char[] buff;

	public ForwardResponse(InputStream in_arg, PrintWriter out_arg)
	{
		in  = in_arg;
		out = out_arg;
		buff = new char[4096];

	}


	  public void run()
	  {
		int inputlen;
                byte buff[] = new byte[4096];
		try {
		//while (in.read(buff) > 0) 
		while ((inputlen = in.read(buff, 0, 4096)) > 0) 
		{

			System.out.println("ForwardResponse: " + new String(buff));
			out.print(new String(buff, 0, inputlen));
			out.flush();
		}
		} catch (Exception ex) {
			System.out.println("Forward response failed: "+ ex.toString());
		}
		out.flush();
		System.out.println("ForwardResponse Complete!");
	  }

}

}

