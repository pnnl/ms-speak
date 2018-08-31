<?xml version="1.0"?>
<xsl:stylesheet 
	version="2.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
	xmlns:pnnl="http://www.pnnl.gov/xslt/conversions/version" 
	xmlns:p2="http://www.multispeak.org/V5.0/ws/request"
	xmlns:p3="http://www.multispeak.org/V5.0/commonTypes"
	xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<xsl:output method="xml" indent="yes"/>

	<!--		
	 Function for parsing version string as '3.0' '3.0.1' '3.0.1.234'
	‘Maj.Min’ or ‘Maj.Min.Build’ or ‘Maj.Min.Build.Branch’.  
	-->

	<xsl:function name="pnnl:parseVersion" as="xs:string">
		<xsl:param name="versionAsString"/>
		<xsl:param name="position"/>
		<xsl:variable name="tokens" select="tokenize(normalize-space($versionAsString), '\.')"/>
		<xsl:value-of select="normalize-space($tokens[$position])"/>
	</xsl:function>

	<xsl:function name="pnnl:parseMajorVersion" as="xs:string">
		<xsl:param name="versionAsString"/>
		<xsl:value-of select="pnnl:parseVersion($versionAsString, 1)"/>
	</xsl:function>
	<xsl:function name="pnnl:parseMinorVersion" as="xs:string">
		<xsl:param name="versionAsString" />
		<xsl:value-of select="pnnl:parseVersion($versionAsString, 2)"/>
	</xsl:function>
	<xsl:function name="pnnl:parseBuildVersion" as="xs:string">
		<xsl:param name="versionAsString" />
		<xsl:value-of select="pnnl:parseVersion($versionAsString, 3)"/>
	</xsl:function>
	<xsl:function name="pnnl:parseBranchVersion" as="xs:string">
		<xsl:param name="versionAsString" />
		<xsl:value-of select="pnnl:parseVersion($versionAsString, 4)"/>
	</xsl:function>

	<!-- tests: this match conflicts with the one in the xslt file
	<xsl:template match="/">
		<test_results>
			<xsl:for-each select="tests/test">
				<p2:MultiSpeakVersion>
					<p3:MajorVersion><xsl:value-of select="pnnl:parseMajorVersion(.)"/></p3:MajorVersion>
					<p3:MinorVersion><xsl:value-of select="pnnl:parseMinorVersion(.)"/></p3:MinorVersion>
					<p3:Build><xsl:value-of select="pnnl:parseBuildVersion(.)"/></p3:Build>
					<p3:Branch><xsl:value-of select="pnnl:parseBranchVersion(.)"/></p3:Branch>
					<p3:BuildString>Release</p3:BuildString>
				</p2:MultiSpeakVersion>
			</xsl:for-each>
		</test_results>
	</xsl:template>
	-->
</xsl:stylesheet><!-- Stylus Studio meta-information - (c) 2004-2009. Progress Software Corporation. All rights reserved.

<metaInformation>
	<scenarios>
		<scenario default="yes" name="Scenario1" userelativepaths="yes" externalpreview="no" url="tests.xml" htmlbaseurl="" outputurl="" processortype="saxon8" useresolver="yes" profilemode="0" profiledepth="" profilelength="" urlprofilexml=""
		          commandline="" additionalpath="" additionalclasspath="" postprocessortype="none" postprocesscommandline="" postprocessadditionalpath="" postprocessgeneratedext="" validateoutput="no" validator="internal" customvalidator="">
			<advancedProp name="bSchemaAware" value="true"/>
			<advancedProp name="xsltVersion" value="2.0"/>
			<advancedProp name="schemaCache" value="||"/>
			<advancedProp name="iWhitespace" value="0"/>
			<advancedProp name="bWarnings" value="true"/>
			<advancedProp name="bXml11" value="false"/>
			<advancedProp name="bUseDTD" value="false"/>
			<advancedProp name="bXsltOneIsOkay" value="true"/>
			<advancedProp name="bTinyTree" value="true"/>
			<advancedProp name="bGenerateByteCode" value="true"/>
			<advancedProp name="bExtensions" value="true"/>
			<advancedProp name="iValidation" value="0"/>
			<advancedProp name="iErrorHandling" value="fatal"/>
			<advancedProp name="sInitialTemplate" value=""/>
			<advancedProp name="sInitialMode" value=""/>
		</scenario>
	</scenarios>
	<MapperMetaTag>
		<MapperInfo srcSchemaPathIsRelative="yes" srcSchemaInterpretAsXML="no" destSchemaPath="" destSchemaRoot="" destSchemaPathIsRelative="yes" destSchemaInterpretAsXML="no"/>
		<MapperBlockPosition></MapperBlockPosition>
		<TemplateContext></TemplateContext>
		<MapperFilter side="source"></MapperFilter>
	</MapperMetaTag>
</metaInformation>
-->
