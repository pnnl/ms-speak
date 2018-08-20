<html>
<head><title>CancelDemandReset</title></head>
<script language="javascript">
// Technical debt: Instead of this being a 'magic number',
//                 we could get this from the user's input
//                 and increment it by one each time a row is added.
var meterID = 1000;

function InsertRow() {
	var table = document.getElementById('thetable');

	var row = table.insertRow(3);

	var cell1 = row.insertCell(0);
	var cell2 = row.insertCell(1);
	var cell3 = row.insertCell(2);

	meterID = meterID + 1;

	// cell1.innerHTML = 'Meter ' + meterID + ' ID:';
	cell1.innerHTML = 'Meter ID:';
	cell2.innerHTML = '<input type="text" name="meter' + meterID + '" value="' + meterID + '" />';
	cell3.innerHTML = '<input type="button" value="Remove" onClick="DeleteRow(this)" />';

	cell1.style.textAlign = "right";
}

function DeleteRow(button) {
   // var i = r.parentNode.parentNode.rowIndex;
   var row = button.parentNode.parentNode;
   // document.getElementById("thetable").deleteRow(i);
   row.parentNode.removeChild(row);
}

// Technical debt: This won't work because we're actually going to 'webClient.php'
//                 and that page redirects us back to this page when it is done
//                 doing its work.  (Stateless)
/*
function Log() {
   var table = document.getElementById('Log');
   var row = table.insertRow(1);
   cell1.innerHTML = "Packet sent!";
}
*/
</script>
<?php
 // Get the last transaction id used from a file
 $fh = fopen('transactionNumber.txt', 'r+') or die($php_errormsg);

 // Make a new transaction id by incrementing the old transaction id by 1
 $transactionID = (int)fread($fh, filesize('transactionNumber.txt')) + 1;

 // Close the file
 fclose($fh);

?>
<body>
<h2><a href="/">MultiSpeak Endpoints</a> | <a href="/MR/">MR EndPoint Functions</a> | CancelDemandReset</h2>
<form id="theform" name="theform" method="POST" action="webClient.php?ServerIP=<?php if(isset($_GET['ServerIP'])) { echo $_GET['ServerIP']; } else { echo "10.0.0.2"; }?>">
<table id="thetable" name="thetable" border="1">
   <tr bgcolor="CCCCCC"><td colspan="3">Input Parameters</td></tr>
   <tr><td align="right">Transaction ID:</td><td><input type="text" name="transactionID" value="<?php echo $transactionID; ?>"/></td><td>&nbsp;</td></tr>
   <tr><td>&nbsp;</td><td align="center"><input type="button" value="Add Meter" onClick="InsertRow()" /></td><td>&nbsp;</td></tr>
   <tr><td align="right">Meter ID:</td><td><input type="text" name="meter1" value="1000" /></td><td><input type="button" value="Remove" onClick="DeleteRow(this)" /></td></tr>

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
