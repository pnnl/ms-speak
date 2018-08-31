import java.io.*;
import java.net.*;
import java.security.*;
import java.util.*;
import javax.net.*;
import javax.net.ssl.*;


public class JSecureListen implements Runnable
{
  /**
   * The port we will listen on
   */
  private int port;

  /**
   * The port not ssl we send to
   */
  private int forwardPort;

  /**
   * KeyStore for storing our public/private key pair
   */
  private KeyStore clientKeyStore;

  /**
   * KeyStore for storing the server's public key
   */
  private KeyStore serverKeyStore;

  /**
   * Used to generate a SocketFactory
   */
  private SSLContext sslContext;

  /**
   * Passphrase for accessing our authentication keystore
   */
  static private final String passphrase = "serverpw";

  /**
   * A source of secure random numbers
   */
  static private SecureRandom secureRandom;

  /**
   * Create a Server that listens on the given port.
   * Start the background listening thread
   */
  public JSecureListen( int port ) {
    this.port = port;

    new Thread( this ).start();
  }


  /**
   * Background thread: accept new connections
   */

  public void run() {
    try {
      setupClientKeyStore();
      setupServerKeystore();
      setupSSLContext();

      SSLServerSocketFactory sf = sslContext.getServerSocketFactory();
      SSLServerSocket ss = (SSLServerSocket)sf.createServerSocket( port );

      // Require client authorization
      //ss.setNeedClientAuth( true );
      ss.setNeedClientAuth( false );

      System.out.println( "Listening on port "+port+"..." );
      while (true) {
        Socket socket = ss.accept();
        System.out.println( "Got connection from "+socket );
		JConnectionProc cp = new JConnectionProc(socket);
		(new Thread(cp)).start();

        //ConnectionProcessor cp = new ConnectionProcessor( this, socket );
        //connections.add( cp );
      }
    } catch( GeneralSecurityException gse ) {
      gse.printStackTrace();
    } catch( IOException ie ) {
      ie.printStackTrace();
    }
  }

  private void setupClientKeyStore() throws GeneralSecurityException, IOException {
    clientKeyStore = KeyStore.getInstance( "JKS" );
    clientKeyStore.load( new FileInputStream( "client.public" ),
                       "public".toCharArray() );
  }

  private void setupServerKeystore() throws GeneralSecurityException, IOException {
    serverKeyStore = KeyStore.getInstance( "JKS" );
    serverKeyStore.load( new FileInputStream( "server.private" ),
                        passphrase.toCharArray() );
  }

  private void setupSSLContext() throws GeneralSecurityException, IOException {
    TrustManagerFactory tmf = TrustManagerFactory.getInstance( "SunX509" );
    tmf.init( clientKeyStore );

    KeyManagerFactory kmf = KeyManagerFactory.getInstance( "SunX509" );
    kmf.init( serverKeyStore, passphrase.toCharArray() );

    sslContext = SSLContext.getInstance( "TLS" );
    sslContext.init( kmf.getKeyManagers(),
                     tmf.getTrustManagers(),
                     secureRandom );
  }


}


