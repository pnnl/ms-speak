<!-- ********* CB Endpoint Message Templates ************** -->
<xsl:stylesheet version="2.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tns="http://www.multispeak.org/Version_3.0" 
	xmlns:p1="http://www.multispeak.org/V5.0/wsdl/CB_Server"
	xmlns:p2="http://www.multispeak.org/V5.0/ws/request" 
	xmlns:p3="http://www.multispeak.org/V5.0/commonTypes" >
  
	<!-- ********* v3 input source Templates ****************** -->

	<!-- ********* v5 input source Templates ****************** -->
	<xsl:template match="p1:PingURLResponse"
		xmlns:p2="http://www.multispeak.org/V5.0/ws/response"
		exclude-result-prefixes="p1 p2 p3 tns">
		<tns:PingURLResponse>v3PingURLResponse<tns:PingURLResult>
				<tns:errorObject>
					<xsl:attribute name="objectID">
						<xsl:value-of select="//p2:Result/p3:errorObjects/p3:errorObject/@referenceID"/>
					</xsl:attribute>
					<xsl:attribute name="errorString">
						<xsl:value-of select="//p2:Result/p3:errorObjects/p3:errorObject/p3:displayString"/>
					</xsl:attribute>
					<xsl:attribute name="nounType">
						<xsl:value-of select="//p2:Result/p3:errorObjects/p3:errorObject/@nounType"/>
					</xsl:attribute>
					<xsl:attribute name="eventTime">
						<xsl:value-of select="//p2:Result/p3:errorObjects/p3:errorObject/p3:eventTime"/>
					</xsl:attribute>
				</tns:errorObject>
			</tns:PingURLResult>
		</tns:PingURLResponse>
	</xsl:template>
		
</xsl:stylesheet>
