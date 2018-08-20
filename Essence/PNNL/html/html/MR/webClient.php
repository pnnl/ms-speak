<?php
   error_reporting(E_ALL ^ E_NOTICE);

   // Create a SOAP client
   require_once 'SOAP/Client.php';
   $url = "http://" . $_GET["ServerIP"] . "/MR/webService.php?wsdl";
   $soap = new SOAP_WSDL($url);
   $proxy = $soap->getProxy();

   // It is easy to use a file to store state information
   //
   // Get the last transaction id used from a file
   $fh = fopen('transactionNumber.txt', 'r+') or die($php_errormsg);

   // SOAP message input parameters


   // INPUT PARAMETER 1: Transaction ID
   $transactionID = 0;
   // See if a transaction id was given to us from a wrapper
   if ($_POST['transactionID']) {
      $transactionID = $_POST['transactionID'];
   } else {
      // If not, make a new transaction id by incrementing the old transaction id by 1
      $transactionID = (int)fread($fh, filesize('transactionNumber.txt')) + 1;
   }

   // The MultiSpeak specification expects the transaction id to be a string
   $transactionID = (string)$transactionID;

   // Store the new transaction id in a file
   rewind($fh);
   fwrite($fh, $transactionID);

   // Close the file
   fclose($fh);

   // INPUT PARAMETER 2: Array of meterID
   $demandResetCancel = array();

   foreach($_POST as $name => $value) {
      // echo '<p>Name is "' . $name . '" and value is " ' . $value . '"</p>';	// INFO
      if(strpos(strtolower($name), 'meter') !== false) {
         $demandResetCancel[$name] = $value;
      }
   }

   // Send a SOAP message request
   if ($_POST['sendCount'] == '0') {
      // Send the message 'n' times
      $k = (int)$_POST['n'];
      for($i=1; $i <= $k; $i++) {
         $result = $proxy->CancelDemandReset($demandResetCancel, $transactionID);
         sleep(1);  // Wait 1s before resending the message
      }
   // This is a BAD idea, because there is no way to get back in and stop it.
   // TODO: If we still want to do this, use a control flag (file?) that can
   //       be tested (true/false).
   /*
   } else if ($_POST['sendCount'] == '-1') {
      while(true) {
         $result = $proxy->CancelDemandReset($demandResetCancel, $transactionID);
         sleep(1);
      }
   */
   } else {
      // Send the message once
         $result = $proxy->CancelDemandReset($demandResetCancel, $transactionID);
   }

   // Output something
   //
   // PRODUCTION: Do not send any output so we can do a header redirect back to the wrapper
   // if (PEAR::isError($result)) {
   //    echo $result->getMessage();
   // } else {
   //    echo "Sent!";
   // }

   // Redirect to the wrapper
   header('Location: cancelDemandReset.php');
?>
