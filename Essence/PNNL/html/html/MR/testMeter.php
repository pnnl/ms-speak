<?php
require_once('meter.php');

// Instantiate an instance of meter
$meter1 = new Meter('THX-1138', '10.0.1.1');	// (meterName, communicationAddress)

// Just for debugging
$meter1->displayValues();
?>
