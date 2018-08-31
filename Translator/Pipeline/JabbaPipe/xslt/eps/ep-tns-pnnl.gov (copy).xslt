<!-- ********* TNS Endpoint Message Templates ************* -->
<xsl:stylesheet version="2.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tns="http://www.multispeak.org/Version_3.0" 
	xmlns:p1="http://www.multispeak.org/V5.0/wsdl/CB_Server"
	xmlns:p2="http://www.multispeak.org/V5.0/ws/request" 
	xmlns:p3="http://www.multispeak.org/V5.0/commonTypes"
	>
  
	<!-- QUESTION:  HOW TO DETERMINE WHAT TYPE OF V5 PingURLRequest to transform
				    a V3 PingURL to (i.e., what should be the value of p1 ?) -->

	<!-- ********* v3 input source Templates ****************** -->
	<xsl:template match="tns:PingURL"
		exclude-result-prefixes="p1 p2 p3 tns">
		<p1:PingURL>v5PingURLRequest</p1:PingURL>
	</xsl:template>
	
	<xsl:template match="tns:GetLatestReadings">
		<p1:GetLatestMeterReadings>v5GetLatestMeterReadings</p1:GetLatestMeterReadings>
		<p1:lastReceived>
			<xsl:value-of select="//@lastReceived"/>
		</p1:lastReceived>
	</xsl:template>
	
	<!-- ********* v5 input source Templates ****************** -->

</xsl:stylesheet>
