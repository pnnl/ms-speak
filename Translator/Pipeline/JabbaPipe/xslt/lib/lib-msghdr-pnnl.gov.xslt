<xsl:stylesheet version="2.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:env="http://www.w3.org/2003/05/soap-envelope"
    xmlns:tns="http://www.multispeak.org/Version_3.0" 
	xmlns:pnnl="http://www.pnnl.gov/xslt/conversions/version" 
	xmlns:p2="http://www.multispeak.org/V5.0/ws/request" 
	xmlns:p3="http://www.multispeak.org/V5.0/commonTypes"
	exclude-result-prefixes="tns">
	<xsl:import href="../eps/ep-tns-pnnl.gov.xslt"/>
	<xsl:import href="../eps/ep-mr-pnnl.gov.xslt"/>
	<xsl:import href="../eps/ep-cb-pnnl.gov.xslt"/>
	<xsl:include href="lib-version-pnnl.gov.xslt"/>

	<!--		
	 template for selecting v3/v5 Request/Response Msg Headers 
	-->
	<xsl:template match="env:header">
		<!--<xsl:variable name="hdrStr" select="local-name(//env:header/*[1])"/> -->
		<!--<xsl:text>hdrStr is: </xsl:text> -->
		<!--<xsl:value-of select="$hdrStr"/> -->
		<xsl:apply-templates select="//env:header/*[1]" />
	</xsl:template>

	<!--		
	 templates for v3/v5 Message Headers 
	-->
	<xsl:template match="tns:MultiSpeakMsgHeader">
		<p2:MultiSpeakRequestMsgHeader DefaultRegisteredName="DefaultRegisteredName" DefaultSystemName="System234" DefaultUtility="Bonneville Power Admin" DefaultCurrencyCode="USD" Context="Context1">
			<xsl:attribute name="TimeStamp">
				<!--<xsl:value-of select="env:Envelope/env:header/tns:MultiSpeakMsgHeader/@TimeStamp"/>-->
				<xsl:value-of select="//@TimeStamp"/>
			</xsl:attribute>
			<xsl:attribute name="MessageID">
				<xsl:value-of select="//@MessageID"/>
			</xsl:attribute>
			<xsl:attribute name="MessageCreatedTimeStamp">
				<xsl:value-of select="//@LastSent"/>
			</xsl:attribute>
			<xsl:attribute name="RegistrationID">
				<xsl:value-of select="//@RegistrationID"/>
			</xsl:attribute>
			<xsl:attribute name="any_attribute">
				<xsl:value-of select="//@any_attribute"/>
			</xsl:attribute>
			<p2:MultiSpeakVersion>
				<p3:MajorVersion>
					<xsl:value-of select="pnnl:parseMajorVersion(//@Version)"/>
				</p3:MajorVersion>
				<p3:MinorVersion>
					<xsl:value-of select="pnnl:parseMinorVersion(//@Version)"/>
				</p3:MinorVersion>
				<p3:Build>
					<xsl:value-of select="pnnl:parseBuildVersion(//@Version)"/>
				</p3:Build>
				<p3:Branch>
					<xsl:value-of select="pnnl:parseBranchVersion(//@Version)"/>
				</p3:Branch>
				<p3:BuildString>
					<xsl:value-of select="//@BuildString"/>
				</p3:BuildString>
			</p2:MultiSpeakVersion>
			<p2:Caller>
				<p3:AppName>
					<xsl:value-of select="//@AppName"/>
				</p3:AppName>
				<p3:AppVersion>
					<xsl:value-of select="//@AppVersion"/>
				</p3:AppVersion>
				<p3:Company>
					<xsl:value-of select="//@Company"/>
				</p3:Company>
				<p3:AuditID>
					<xsl:value-of select="//@AuditID"/>
				</p3:AuditID>
				<p3:AuditPassword>
					<xsl:value-of select="//@Pwd"/>
				</p3:AuditPassword>
				<p3:SystemID>SysID002</p3:SystemID>
				<p3:Password>
					<xsl:value-of select="//@Pwd"/>
				</p3:Password>
				<xsl:value-of select="//@UserID"/>
			</p2:Caller>
			<p2:CodedNames>
				<p3:codedName codedNameType="cNameT">
					<p3:codedValue>P</p3:codedValue>
					<p3:namePart>nameP</p3:namePart>
					<p3:description>Part of Name</p3:description>
				</p3:codedName>
			</p2:CodedNames>
			<p2:CoordinateSystemInformation>
				<p3:CSUnits otherKind="inches">
					<xsl:value-of select="//@CSUnits"/>USSurveyFeet
				</p3:CSUnits>
				<p3:CSAuthorities>
					<p3:CSAuthority>
						<p3:CSAuthorityName otherKind="otherSPCS">
							<xsl:value-of select="substring-before(//@CoordinateSystem,'-')"/>
						</p3:CSAuthorityName>
						<p3:CoordinateSystemAuthorityCode>
							<xsl:value-of select="substring-after(//@CoordinateSystem,'-')"/>
						</p3:CoordinateSystemAuthorityCode>
						<p3:Datum>
							<xsl:value-of select="//@Datum"/>
						</p3:Datum>
					</p3:CSAuthority>
				</p3:CSAuthorities>
			</p2:CoordinateSystemInformation>
			<p2:DataSetState>
				<p3:PublishDataSetState>
					<p3:DataSetID>DataSetID001</p3:DataSetID>
					<p3:PreviousDataSetID>DataSetId000</p3:PreviousDataSetID>
				</p3:PublishDataSetState>
				<p3:RequestDataSetState>
					<p3:DataSetID>
						<xsl:value-of select="//@SessionID"/>
					</p3:DataSetID>
					<p3:PreviousDataSetID>
						<xsl:value-of select="//@PreviousSessionID"/>
					</p3:PreviousDataSetID>
				</p3:RequestDataSetState>
			</p2:DataSetState>
			<p2:DoNotReply>
				<p3:registrationID>00000000-0000-0000-0000-000000000000</p3:registrationID>
				<p3:registrationID>00000000-0000-0000-0000-000000000001</p3:registrationID>
				<p3:registrationID>00000000-0000-0000-0000-000000000002</p3:registrationID>
			</p2:DoNotReply>
		</p2:MultiSpeakRequestMsgHeader>
	</xsl:template>

	<xsl:template match="p2:MultiSpeakRequestMsgHeader"
		xmlns:p2="http://www.multispeak.org/V5.0/ws/response">
		<h1>This MultiSpeakRequestMsgHeader Template is still under Construction!</h1>
	</xsl:template>

	<xsl:template match="p2:MultiSpeakResponseMsgHeader"
		xmlns:p2="http://www.multispeak.org/V5.0/ws/response"
		exclude-result-prefixes="pnnl p2 p3 tns">
		<tns:MultiSpeakMsgHeader PreviousSessionID="PrevSessID001" RegistrationID="RegistrationID001">
			<xsl:attribute name="Version">
				<xsl:value-of select="concat(//p2:MultiSpeakVersion/p3:MajorVersion,'.',//p2:MultiSpeakVersion/p3:MinorVersion,'.',//p2:MultiSpeakVersion/p3:Build,'.',//p2:MultiSpeakVersion/p3:Branch)"/>
			</xsl:attribute>
			<xsl:attribute name="UserID">
				<xsl:value-of select="//p2:Caller/p3:SystemID"/>
			</xsl:attribute>
			<xsl:attribute name="Pwd">
				<xsl:value-of select="//p2:Caller/p3:AuditPassword"/>
			</xsl:attribute>
			<xsl:attribute name="AppName">
				<xsl:value-of select="//p2:Caller/p3:AppName"/>
			</xsl:attribute>
			<xsl:attribute name="AppVersion">
				<xsl:value-of select="//p2:Caller/p3:AppVersion"/>
			</xsl:attribute>
			<xsl:attribute name="Company">
				<xsl:value-of select="//p2:Caller/p3:Company"/>
			</xsl:attribute>
			<xsl:attribute name="CSUnits">
				<xsl:value-of select="//p2:CoordinateSystemInformation/p3:CSUnits"/>
			</xsl:attribute>
			<xsl:attribute name="CoordinateSystem">
				<xsl:value-of select="concat(//p2:CoordinateSystemInformation/p3:CSAuthorities/p3:CSAuthority/p3:CSAuthorityName,'-',//p2:CoordinateSystemInformation/p3:CSAuthorities/p3:CSAuthority/p3:CoordinateSystemAuthorityCode)"/>
			</xsl:attribute>
			<xsl:attribute name="Datum">
				<xsl:value-of select="//p2:CoordinateSystemInformation/p3:CSAuthorities/p3:CSAuthority/p3:Datum"/>
			</xsl:attribute>
			<xsl:attribute name="SessionID">
				<xsl:value-of select="//p2:Result/p3:dataSetID"/>
			</xsl:attribute>
			<xsl:attribute name="ObjectsRemaining">
				<xsl:value-of select="//p2:Result/p3:objectsRemaining"/>
			</xsl:attribute>
			<xsl:attribute name="LastSent">
				<xsl:value-of select="//p2:Result/p3:lastSent"/>
			</xsl:attribute>
			<xsl:attribute name="AuditID">
				<xsl:value-of select="//p2:Caller/p3:AuditID"/>
			</xsl:attribute>
			<xsl:attribute name="MessageID">
				<xsl:value-of select="//@MessageID"/>
			</xsl:attribute>
			<xsl:attribute name="TimeStamp">
				<xsl:value-of select="//@TimeStamp"/>
			</xsl:attribute>
			<xsl:attribute name="BuildString">
				<xsl:value-of select="//p2:MultiSpeakVersion/p3:BuildString"/>
			</xsl:attribute>
			<xsl:attribute name="any_attribute">
				<xsl:value-of select="//@any_attribute"/>
			</xsl:attribute>
		</tns:MultiSpeakMsgHeader>
	</xsl:template>

	<!--		
	 template for selecting v3/v5 Request/Response Body Templates  
	-->
	<xsl:template name='matchBody'>
		<!-- access the prefix of the current node name by:
		<xsl:comment>Getting Name with Prefix:</xsl:comment>
		<xsl:variable name="preFixedName" select="name(//env:Body/*[1])" />
		<xsl:text>preFixedName is: </xsl:text>
		<xsl:value-of select="$preFixedName"/>
		<xsl:text>&#xd;&#xa;</xsl:text>
		 -->
		<xsl:apply-templates select="//env:Body/*[1]" />
	</xsl:template>
   		
</xsl:stylesheet>
<!-- Sample codes
	<xsl:variable name="bodyStr" select="local-name(//soap:Body/*[1])"/>
	<xsl:text>bodyStr is: </xsl:text>
	<xsl:value-of select="$bodyStr"/>
		<xsl:choose>
		<xsl:when test="$bodyStr = 'PingURL'">
			<h2>mooooooooooooo</h2>
		</xsl:when>
		<xsl:when test="$bodyStr = 'PingURLResponse'">
			<h2>booooooooooooo</h2>
		</xsl:when>
		<xsl:otherwise>
			<h2>dooooooooooooo</h2>
		</xsl:otherwise>
	</xsl:choose>
-->
<!-- Stylus Studio meta-information - (c) 2004-2009. Progress Software Corporation. All rights reserved.

<metaInformation>
	<scenarios/>
	<MapperMetaTag>
		<MapperInfo srcSchemaPathIsRelative="yes" srcSchemaInterpretAsXML="no" destSchemaPath="" destSchemaRoot="" destSchemaPathIsRelative="yes" destSchemaInterpretAsXML="no"/>
		<MapperBlockPosition>
			<template match="env:header"></template>
			<template name="matchBody"></template>
		</MapperBlockPosition>
		<TemplateContext></TemplateContext>
		<MapperFilter side="source"></MapperFilter>
	</MapperMetaTag>
</metaInformation>
-->
