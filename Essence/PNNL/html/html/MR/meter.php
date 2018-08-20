<?php
require_once('guid.php');

class Meter
{
   // Properties
   private $meterName = '';				// Dynamic
   private $serviceType = 'Electric';
   private $objectServiceType = 'Electric';
   private $objectGUID = '';				// Dynamic
   private $communicationAddress = '';			// Dynamic
   private $communicationPort = '8899';
   private $utility = 'Rural Electric Cooperative';
   private $registeredName = '';			// Dynamic
   private $systemName = '';				// Dynamic

   // Methods

   // Cunstructor
   function __construct($_meterName, $_communicationAddress) {
      $this->meterName = $_meterName;
      $this->objectGUID = guid();
      $this->communicationAddress = $_communicationAddress;
      $this->registeredName = $this->meterName;
      $this->systemName = $this->meterName;
   }

   // Just for debugging...
   public function DisplayValues() {
      echo "Meter name: $this->meterName\n";
      echo "Service type: $this->serviceType\n";
      echo "Object service type: $this->objectServiceType\n";
      echo "Object GUID: $this->objectGUID\n";
      echo "Communication address: $this->communicationAddress\n";
      echo "Communication port: $this->communicationPort\n";
      echo "Utility: $this->utility\n";
      echo "Registered name: $this->registeredName\n";
      echo "System name: $this->systemName\n";
   }

}
?>
