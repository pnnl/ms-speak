<?php
   error_reporting(E_ALL ^ E_NOTICE);

   // Create a SOAP client
   require_once 'SOAP/Client.php';
   $url = "http://" . $_GET["ServerIP"] . "/NOT/SOAPResponse.php?wsdl";
   $soap = new SOAP_WSDL($url);
   $proxy = $soap->getProxy();

   // It is easy to use a file to store state information
   //
   // Get the last transaction id used from a file
   $fh = fopen('transactionNumber.txt', 'r+') or die($php_errormsg);

   // SOAP message input parameters
   //
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

   // INPUT PARAMETER 2: Array of powerMonitor
   // TODO: Previously this was a 1d array
   //       now it is a 2d array, with 9 elements in each instance of 'powerMonitor'
   $powerMonitor = array();

   foreach($_POST as $name => $value) {
      // DEBUG INFO
      // echo '<p>Name is "' . $name . '" and value is " ' . $value . '"</p>';

      $intPowerMonitorID = 0;
      $strCurrentPowerMonitorID = "0";
      $intDelimiterIndex = 0;
      $intPowerMonitorIDLength = 0;
      $intPowerMonitorIDLastCharIndex = 0;

      if(strpos(strtolower($name), 'powermonitor') !== false) {
	 // NOTE: This uses more variables than necessary,
         // but I want to be clear about what's going on.
         //
         // Two-dimensional arrays need to associate multiple <input> values with a single array element
         // which may have an arbitrary sized index.  (E.G. |1| = 1, |10| = 2.)
         //
         // In this case, the name of each <input> starts with 'powerMonitor", then the associated index,
         // followed by the purpose of the <input> field, E.G. 'RecordNumber'.
         //
         // If the index is the same, we should add the <input> value to the current array element,
         // if the index is different, we should start a new array element.
         $intDelimiterIndex = strpos($name, '-');
         $intPowerMonitorIDLastCharIndex = $intDelimiterIndex - 1;
         $intPowerMonitorIDLength = $intPowerMonitorIDLastCharIndex - 11; // |powerMonitor| = 11 (zero-based)
         $strCurrentPowerMonitorID = substr($name, 12, $intPowerMonitorIDLength);

         // Check if we are updating an existing 'power monitor' or starting a new one
         if ((int)$strCurrentPowerMonitorID <> $intPowerMonitorID) {
            $intPowerMonitorID = (int)$strCurrentPowerMonitorID;
         }

         // DEBUG INFO
         // echo "<p>*** Delimiter Index *** = " . $intDelimiterIndex . "</p>";
         // echo "<p>*** Last Char ID Index *** = " . $intPowerMonitorIDLastCharIndex . "</p>";
         // echo "<p>*** ID Length *** = " . $intPowerMonitorIDLength . "</p>";
         // echo "<p>*** Current Power Monitor ID *** = " . $strCurrentPowerMonitorID . "</p>";
         // echo "<p>*** Power Monitor ID *** = " . $intPowerMonitorID . "</p>";

         $splitName = split("-", $name);
         $newName = $splitName[1];

         $powerMonitor[$intPowerMonitorID][$newName] = $value;
         // $powerMonitor["PowerMonitor"][$newName] = $value; // This obviously overwrites previous keys.
      }
   }

   // DEBUG INFO
   // print_r($powerMonitor);

   // Send a SOAP message request
   if ($_POST['sendCount'] == '0') {
      // Send the message 'n' times
      $k = (int)$_POST['n'];
      for($i=1; $i <= $k; $i++) {
         $result = $proxy->PowerMonitorsNotification($powerMonitor, $transactionID);
         sleep(1);  // Wait 1s before resending the message
      }
   } else {
      // Send the message once
         $result = $proxy->PowerMonitorsNotification($powerMonitor, $transactionID);
   }

   // Output something (DEBUG INFO)
   //
   // PRODUCTION: (This section is commented out.)
   // Do not send any output so we can do a header redirect back to the wrapper
   // if (PEAR::isError($result)) {
   //    echo $result->getMessage();
   // } else {
   //    echo "Sent!";
   // }

   // Redirect to the wrapper
   // PRODUCTION: (Uncomment)
   header('Location: powerMonitorsNotification.php');
?>
