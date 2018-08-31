<!-- ********* OA Endpoint Message Templates ************** -->
<xsl:stylesheet version="2.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:tns="http://www.multispeak.org/Version_3.0"
	xmlns:p1="http://www.multispeak.org/V5.0/wsdl/OA_Server"
	xmlns:p2="http://www.multispeak.org/V5.0/commonArrays"
	xmlns:p3="http://www.multispeak.org/V5.0/commonTypes"
	xmlns:p4="http://www.multispeak.org/V5.0"
	>
	<!-- ********* v3 input source Templates ****************** -->
	<xsl:template match="p1:GetOutageLocationStatusesByOutageLocations"
		xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		exclude-result-prefixes="p1 p2 p3 p4 tns">
		<p1:GetOutageLocationStatusesByOutageLocations>
			<xsl:attribute name="xmlns:xsi">
				<xsl:value-of select="tns:GetOutageEventStatusByOutageLocation/@xmlns:xsi"/>
			</xsl:attribute>
			<xsl:attribute name="xsi:schemaLocation">
				<xsl:value-of select="tns:GetOutageEventStatusByOutageLocation/@xsi:schemaLocation"/>
			</xsl:attribute>
			<p1:ArrayOfOutageLocationReferable>
				<p2:outageLocationReferable>
					<p3:extensions>
						<xsl:for-each select="tns:GetOutageEventStatusByOutageLocation/tns:location/tns:extensions/any_element">
							<any_element>
								<xsl:value-of select="."/>
							</any_element>
						</xsl:for-each>
					</p3:extensions>
					<p3:extensionsList>
						<xsl:for-each select="tns:GetOutageEventStatusByOutageLocation/tns:location/tns:extensionsList/tns:extensionsItem">
							<p3:extensionsItem/>
						</xsl:for-each>
					</p3:extensionsList>
					<p4:serviceInformation>
						<p4:meterID>
							<xsl:attribute name="utility">
								<xsl:value-of select="tns:GetOutageEventStatusByOutageLocation/tns:location/@utility"/>
							</xsl:attribute>
							<xsl:attribute name="any_attribute">
								<xsl:value-of select="tns:GetOutageEventStatusByOutageLocation/tns:location/@any_attribute"/>
							</xsl:attribute>
						</p4:meterID>
					</p4:serviceInformation>
					<p4:telephoneNumber>
						<p3:areaCode>
							<xsl:value-of select="tns:GetOutageEventStatusByOutageLocation/tns:location/tns:areaCode"/>
						</p3:areaCode>
					</p4:telephoneNumber>
				</p2:outageLocationReferable>
			</p1:ArrayOfOutageLocationReferable>
		</p1:GetOutageLocationStatusesByOutageLocations>
	</xsl:template>

	<!-- ********* v5 input source Templates ****************** -->
		
</xsl:stylesheet>
