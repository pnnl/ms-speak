<?php
   error_reporting(E_ALL ^ E_NOTICE);

   require_once 'SOAP/Server.php';

   $soap = new SOAP_Server;
   $service = new ServiceClass();

   $soap->addObjectMap($service, 'urn:php-hoshmand-soapservice');

   if (isset($_SERVER['REQUEST_METHOD']) && $_SERVER['REQUEST_METHOD'] == 'POST') {
       $soap->service($HTTP_RAW_POST_DATA);
   } else {
      require_once 'SOAP/Disco.php';
      $disco = new SOAP_DISCO_SERVER($soap, 'DiscoServer');
      if (isset($_SERVER['QUERY_STRING']) && strpos($_SERVER['QUERY_STRING'], 'wsdl') === 0) {
         header('Content-type: text/xml');
         echo $disco->getWSDL();
      }
   }

   class ServiceClass {
      var $__dispatch_map = array();

      function ServiceClass() {
         // Map Methods
         //

         $this->__dispatch_map['PowerMonitorsNotification'] = array(
            'in' => array(
               'ArrayOfPowerMonitor' => 'powerMonitor',
               'TransactionID' => 'string'),
            'out' => array(
               'ResponseURL' => 'anyURI')
         );

      }

      function __dispatch($method) {
         if(isset($this->__dispatch_map[$method])) {
            return $this->__dispatch_map[$method];
         } else {
            return null;
         }
      }

      // Methods
      //

      function PowerMonitorsNotification($powerMonitor, $transactionID) {
            return "http://www.nowhere.com/receiveResponse.php?action=update";
      }
   }
?>
