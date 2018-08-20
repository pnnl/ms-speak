<?php require_once('../support/guid.php'); ?>

<html>
<head><title>PowerMonitorsNotification</title></head>
<script language="javascript">
// Technical debt: Instead of this being a 'magic number',
//                 we could get this from the user's input
//                 and increment it by one each time a row is added.
var powerMonitorID = 1;

// TODO:
//       Test XML output in WireShark

function InsertRows() {
   powerMonitorID = powerMonitorID + 1;

   var table = document.getElementById('thetable');

   // Row 10
   var row = table.insertRow(3);
   var cell1 = row.insertCell(0);
   var cell2 = row.insertCell(1);

   cell1.innerHTML = 'Material Management Assembly ID:';
   cell2.innerHTML = '<input type="text" id="powerMonitor' + powerMonitorID + '-MaterialManagementAssemblyID" name="powerMonitor' + powerMonitorID + '-MaterialManagementAssemblyID" value="' +
      document.getElementById('powerMonitor1-MaterialManagementAssemblyID').value + '" />';

   cell1.style.textAlign = "right";
   cell2.colSpan = 2;

   // Row 9
   var row = table.insertRow(3);
   var cell1 = row.insertCell(0);
   var cell2 = row.insertCell(1);

   cell1.innerHTML = 'Acknowledged Date:';
   cell2.innerHTML = '<input type="text" id="powerMonitor' + powerMonitorID + '-AcknowledgedDate" name="powerMonitor' + powerMonitorID + '-AcknowledgedDate" value="' +
      document.getElementById('powerMonitor1-AcknowledgedDate').value + '" />';

   cell1.style.textAlign = "right";
   cell2.colSpan = 2;

   // Row 8
   var row = table.insertRow(3);
   var cell1 = row.insertCell(0);
   var cell2 = row.insertCell(1);

   cell1.innerHTML = 'Acknowledged By:';
   cell2.innerHTML = '<input type="text" id="powerMonitor' + powerMonitorID + '-AcknowledgedBy" name="powerMonitor' + powerMonitorID + '-AcknowledgedBy" value="' +
      document.getElementById('powerMonitor1-AcknowledgedBy').value + '" + />';

   cell1.style.textAlign = "right";
   cell2.colSpan = 2;

   // Row 7
   var row = table.insertRow(3);
   var cell1 = row.insertCell(0);
   var cell2 = row.insertCell(1);

   cell1.innerHTML = 'Is Acknowledged:';
   cell2.innerHTML = '<input type="text" id="powerMonitor' + powerMonitorID + '-IsAcknowledged" name="powerMonitor' + powerMonitorID + '-IsAcknowledged" value="' +
      document.getElementById('powerMonitor1-IsAcknowledged').value + '" />';

   cell1.style.textAlign = "right";
   cell2.colSpan = 2;

   // Row 6
   var row = table.insertRow(3);
   var cell1 = row.insertCell(0);
   var cell2 = row.insertCell(1);

   cell1.innerHTML = 'Voltage:';
   cell2.innerHTML = '<input type="text" id="powerMonitor' + powerMonitorID + '-Voltage" name="powerMonitor' + powerMonitorID + '-Voltage" value="' +
      document.getElementById('powerMonitor1-Voltage').value + '" />';

   cell1.style.textAlign = "right";
   cell2.colSpan = 2;

   // Row 5
   var row = table.insertRow(3);
   var cell1 = row.insertCell(0);
   var cell2 = row.insertCell(1);

   cell1.innerHTML = 'Event Code:';
   cell2.innerHTML = '<input type="text" id="powerMonitor' + powerMonitorID + '-EventCode" name="powerMonitor' + powerMonitorID + '-EventCode" value="' +
      document.getElementById('powerMonitor1-EventCode').value + '" />';

   cell1.style.textAlign = "right";
   cell2.colSpan = 2;

   // Row 4
   var row = table.insertRow(3);
   var cell1 = row.insertCell(0);
   var cell2 = row.insertCell(1);

   cell1.innerHTML = 'Record Number:';
   cell2.innerHTML = '<input type="text" id="powerMonitor' + powerMonitorID + '-RecordNumber" name="powerMonitor' + powerMonitorID + '-RecordNumber" value="' +
      document.getElementById('powerMonitor1-RecordNumber').value + '" />';

   cell1.style.textAlign = "right";
   cell2.colSpan = 2;

   // Row 3
   var row = table.insertRow(3);
   var cell1 = row.insertCell(0);
   var cell2 = row.insertCell(1);

   cell1.innerHTML = 'Telephone Number:';
   cell2.innerHTML = '<input type="text" id="powerMonitor' + powerMonitorID + '-TelephoneNumber" name="powerMonitor' + powerMonitorID + '-TelephoneNumber" value="' +
      document.getElementById('powerMonitor1-TelephoneNumber').value + '" />';

   cell1.style.textAlign = "right";
   cell2.colSpan = 2;

   // Row 2
   var row = table.insertRow(3);
   var cell1 = row.insertCell(0);
   var cell2 = row.insertCell(1);

   cell1.innerHTML = 'Call Time:';
   cell2.innerHTML = '<input type="text" id="powerMonitor' + powerMonitorID + '-CallTime" name="powerMonitor' + powerMonitorID + '-CallTime" value="' +
      document.getElementById('powerMonitor1-CallTime').value + '" />';

   cell1.style.textAlign = "right";
   cell2.colSpan = 2;

   // Row 1
   var row = table.insertRow(3);
   var cell1 = row.insertCell(0);
   var cell2 = row.insertCell(1);
   var cell3 = row.insertCell(2);

   cell1.innerHTML = 'Power Monitor ' + powerMonitorID + ':';
   cell2.innerHTML = '&nbsp;';
   cell3.innerHTML = '<input type="button" value="Remove" onClick="DeleteRows(this)" />';

   cell1.style.textAlign = "right";
   cell1.style.backgroundColor = "#99FF99";
   cell2.style.backgroundColor = "#99FF99";
   cell3.style.backgroundColor = "#99FF99";
}


function DeleteRows(element) {
   var tr = element;

   while (tr != null && tr.nodeName.toLowerCase() != 'tr') {
      tr = tr.parentNode;

      if (tr == null) {
         return;
      }

      var ord = tr.sectionRowIndex;
      var tab = document.getElementById('thetable');

      for (var i = ord+9; i >= ord; i--) {
         if (i >= 0 && i < tab.rows.length) {
            tab.deleteRow(i);
         }
      }
   }
}
</script>

<?php
// Transaction ID
//
// Get the last transaction id used from a file
$fh = fopen('transactionNumber.txt', 'r+') or die($php_errormsg);
// Make a new transaction id by incrementing the old transaction id by 1
$transactionID = (int)fread($fh, filesize('transactionNumber.txt')) + 1;
// Close the file
fclose($fh);

// Record Number
//
// Get the last record number used from a file
$fh = fopen('recordNumber.txt', 'r+') or die($php_errormsg);
// Make a new record number by incrementing the old record number by 1
$recordNumber = (int)fread($fh, filesize('recordNumber.txt')) + 1;
// Close the file
fclose($fh);
?>

<body>
<h2><a href="/">MultiSpeak Endpoints</a> | <a href="/NOT/">NOT EndPoint Functions</a> | PowerMonitorsNotification</h2>
<form id="theform" name="theform" method="POST" action="SOAPRequest.php?ServerIP=<?php if(isset($_GET['ServerIP'])) { echo $_GET['ServerIP']; } else { echo "10.0.0.2"; }?>">
<table id="thetable" name="thetable" border="1">
   <tr bgcolor="CCCCCC"><td colspan="3">Input Parameters</td></tr>
   <tr><td align="right">Transaction ID:</td><td><input type="text" name="transactionID" value="<?php echo $transactionID; ?>"/></td><td>&nbsp;</td></tr>
   <tr><td>&nbsp;</td><td align="center"><input type="button" value="Add Power Monitor" onClick="InsertRows()" /></td><td>&nbsp;</td></tr>
   <tr bgcolor="99FF99"><td align="right">Power Monitor 1:</td><td>&nbsp;</td><td><input type="button" value="Remove" onClick="DeleteRow(this)" /></td></tr>
   <tr><td align="right">Call Time:</td><td colspan="2"><input type="text" id="powerMonitor1-CallTime" name="powerMonitor1-CallTime" value="<?php echo date('c'); ?>" /></td></tr>
   <tr><td align="right">Telephone Number:</td><td colspan="2"><input type="text" id="powerMonitor1-TelephoneNumber" name="powerMonitor1-TelephoneNumber" value="(123) 867-5309" /></td></tr>
   <tr><td align="right">Record Number:</td><td colspan="2"><input type="text" id="powerMonitor1-RecordNumber" name="powerMonitor1-RecordNumber" value="<?php echo $recordNumber; ?>" /></td></tr>
   <tr><td align="right">Event Code:</td><td colspan="2">
      <select id="powerMonitor1-EventCode" name="powerMonitor1-EventCode">
         <option value="Unknown">Unknown</option>
         <option value="LowBattery">Low Battery</option>
         <option value="Event1">Event 1</option>
         <option value="Event2">Event 2</option>
         <option value="Event3">Event 3</option>
         <option value="LockOut">Lock Out</option>
         <option value="PowerRestored">Power Restored</option>
         <option value="UndeterminedOn">Undetermined On</option>
         <option value="UndeterminedOff">Undetermined Off</option>
         <option value="BrownOut">Brown Out</option>
         <option value="HighVoltage">High Voltage</option>
         <option value="NormalVoltage" selected>Normal Voltage</option>
         <option value="Other">Other</option>
      </select>
   </td></tr>
   <tr><td align="right">Voltage:</td><td colspan="2"><input type="text" id="powerMonitor1-Voltage" name="powerMonitor1-Voltage" value="240.0" /></td></tr>
   <tr><td align="right" valign="top">Is Acknowledged:</td><td colspan="2">
      <input type="radio" id="powerMonitor1-IsAcknowledged" name="powerMonitor1-IsAcknowledged" value="False" />False<br>
      <input type="radio" id="powerMonitor1-IsAcknowledged" name="powerMonitor1-IsAcknowledged" value="True" checked/>True
   </td></tr>
   <tr><td align="right">Acknowleded By:</td><td colspan="2"><input type="text" id="powerMonitor1-AcknowledgedBy" name="powerMonitor1-AcknowledgedBy" value="Waterhouse, Randy" /></td></tr>
   <tr><td align="right">Acknowleded Date:</td><td colspan="2"><input type="text" id="powerMonitor1-AcknowledgedDate" name="powerMonitor1-AcknowledgedDate" value="<?php echo date('c'); ?>" /></td></tr>
   <tr><td align="right">Material Management Assembly ID:</td><td colspan="2"><input type="text" id="powerMonitor1-MaterialManagementAssemblyID" name="powerMonitor1-MaterialManagementAssemblyID" value="<?php echo guid(); ?>" /></td></tr>

   <tr bgcolor="CCCCCC"><td colspan="3">Message Options</td></tr>
   <tr><td>&nbsp;</td><td colspan="2"><input type="radio" name="sendCount" value="1" checked="checked" />Send once</td></tr>
   <tr><td>&nbsp;</td><td colspan="2"><input type="radio" name="sendCount" value="0" />Send <input name="n" type="text" size="5" value="n" /> times</td></tr>
   <!--<tr><td>&nbsp;</td><td colspan><input type="radio" name="sendCount" value="-1" />Send continuously</td><td align="center"><input type="button" value="Stop" /></td></tr>-->
   <tr><td>&nbsp;</td><td colspan="2" align="center"><input type="submit" value="Start" /></td></tr>
</table>
</form>

<!--
<table id="log" name="log" border="1">
<tr><th>Log</th></tr>
</table>
-->
</body>
</html>
