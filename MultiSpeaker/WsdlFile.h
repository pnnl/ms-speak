/*-------------------------------------------------------------------------------

  Multi-Speak - Secure Protocol Enterprise Access Kit(MS_SPEAK)
  Copyright © 2018, Battelle Memorial Institute
  All rights reserved.
  1.	Battelle Memorial Institute (hereinafter Battelle) hereby grants permission to any person or
		entity lawfully obtaining a copy of this software and associated documentation files
		(hereinafter “the Software”) to redistribute and use the Software in source and binary forms,
		with or without modification.  Such person or entity may use, copy, modify, merge, publish,
		distribute, sublicense, and/or sell copies of the Software, and may permit others to do so,
		subject to the following conditions:
		•	Redistributions of source code must retain the above copyright notice, this list of
			conditions and the following disclaimers.
		•	Redistributions in binary form must reproduce the above copyright notice, this list of
			conditions and the following disclaimer in the documentation and/or other materials
			provided with the distribution.
		•	Other than as used herein, neither the name Battelle Memorial Institute or Battelle may
			be used in any form whatsoever without the express written consent of Battelle.

  2.	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
		OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
		AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BATTELLE OR CONTRIBUTORS
		BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
		(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
		OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
		CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
		OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


  This material was prepared as an account of work sponsored by an agency of the United States Government.
  Neither the United States  Government nor the United States Department of Energy, nor Battelle, nor
  any of their employees, nor any jurisdiction or organization  that has cooperated in the development
  of these materials, makes any warranty, express or implied, or assumes any legal liability or
  responsibility for the accuracy, completeness, or usefulness or any information, apparatus, product,
  software, or process disclosed, or represents that its use would not infringe privately owned rights.
  Reference herein to any specific commercial product, process, or service by trade name, trademark,
  manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or
  favoring by the United States Government or any agency thereof, or Battelle Memorial Institute. The
  views and opinions of authors expressed herein do not necessarily state or reflect those of the
  United States Government or any agency thereof.
									 PACIFIC NORTHWEST NATIONAL LABORATORY
											    operated by
												  BATTELLE
											      for the
									  UNITED STATES DEPARTMENT OF ENERGY
									   under Contract DE-AC05-76RL01830


    This notice including this sentence must appear on any copies of this computer software.
*/
//-------------------------------------------------------------------------------
//	History
//		2017 - Created By: Lance Irvine.
//		2018 - Modified By: Carl Miller <carl.miller@pnnl.gov>
//-------------------------------------------------------------------------------
//
// Summary: WsdlFile.h
//-------------------------------------------------------------------------------

#ifndef WSDLFILE_H
#define WSDLFILE_H

#include <QDomDocument>
#include <QHash>
#include <QObject>

#include "Settings.h"
#include "WebServiceInfo.h"

class QDomDocument;

const QString STR_SOAP = "soap";
const QString STR_WSDL = "wsdl";

const QString TAG_JSON_ATTR = "__ATTR__";
const QString TAG_JSON_CHOICE = "choice";
const QString TAG_JSON_DEFAULT = "default";
const QString TAG_JSON_DESC = "desc";
const QString TAG_JSON_ENUM = "enum";
const QString TAG_JSON_ID = "__ID__";
const QString TAG_JSON_INFO = "__INFO__";
const QString TAG_JSON_IS_ARRAY_CONTAINER = "isArrayContainer";
const QString TAG_JSON_IS_USER_CHECKED = "isUserChecked";
const QString TAG_JSON_DONT_FILTER = "dontFilter";
const QString TAG_JSON_MIN = "min";
const QString TAG_JSON_MAX = "max";
const QString TAG_JSON_NAMESPACE = "namespace";
const QString TAG_JSON_NS = "__NS__";
const QString TAG_JSON_PATTERN = "pattern";
const QString TAG_JSON_TYPE = "type";
const QString TAG_JSON_USE = "use";
const QString STR_ATTRIBUTES = "Attributes";
/*
 * Required is different from optional. Optional means that the field does not need to be present in the XML.
 * You can have a field that is optional and required, meaning that if it is present in the XML then it must be filled in.
 *
 * In order to set a schema element as optional, you include the minOccurs="0" attribute. In order to set a schema element as
 * not required, you include the nillable="true" attribute.
 *
 * In order to set a schema attribute as optional, you do not need to add anything as attributes are optional by default;
 * but you might prefer to include the use="optional" attribute.  In order to set a schema attribute as not optional, you must
 * include the use="required" attribute. Attributes have no equivalent to the nillable attribute on elements. If you want an
 * attribute to be not required, you must specify the string data type. All other data types will require the attribute to have a value.
 */
const QString TAG_JSON_USE_REQUIRED = "required";
const QString TAG_JSON_USE_OPTIONAL = "optional";
class NamespaceInfo;
class TimelineEvent; 

//------------------------------------------------------------------------------
// Class SchemaInfo
//
class SchemaInfo
{
public:
  QHash<QString, QString> NamespaceFileNameLookup; // key is actual namespace...value is import filename for that namespace
  QString Path;
  QHash<QString, QString> PrefixNamespaceLookup; // key is namespace prefix...value is actual namespace
  QString SoapPrefix;
  QString TargetNamespace;
  QString TargetNamespacePrefix; // the prefix assoc with the TargetNamespace...usually blank
  QString WsdlPrefix;
  QString XmlSchemaPrefix; // The prefix assoc with the http://www.w3.org/2001/XMLSchema namespace

  SchemaInfo(const QString& path) : Path(path), SoapPrefix(STR_SOAP), TargetNamespace(""), TargetNamespacePrefix(""), WsdlPrefix(STR_WSDL), XmlSchemaPrefix("") {}
  SchemaInfo(const SchemaInfo& info)
    : NamespaceFileNameLookup(info.NamespaceFileNameLookup), Path(info.Path), PrefixNamespaceLookup(info.PrefixNamespaceLookup), 
    SoapPrefix(info.SoapPrefix), TargetNamespace(info.TargetNamespace), TargetNamespacePrefix(info.TargetNamespacePrefix), 
    WsdlPrefix(info.WsdlPrefix), XmlSchemaPrefix(info.XmlSchemaPrefix) {}
  ~SchemaInfo() {}
private:
  SchemaInfo& operator=(SchemaInfo& info) {return info;}
};

//------------------------------------------------------------------------------
// Class WsdlMethod
//
class WsdlMethod : public QObject
{
	Q_OBJECT
public:
	QString Desc;
	QString Input;
	QString Name;
	QString Output;
	QString RequestHeader;
	QString ResponseHeader;

public:
	WsdlMethod(const QString& name, QObject* parent=Q_NULLPTR) : QObject(parent), Desc(""), Input(""), Name(name), Output(""), RequestHeader(""), ResponseHeader("") {}
	~WsdlMethod() {}
};

//------------------------------------------------------------------------------
// Class WsdlFile
//
class WsdlFile : public QObject
{
	Q_OBJECT
private:
	QString m_fileName; // Actual fileName
	QString m_hostName; // The WSDL Service Host Short Name , i.e. CB MR
	QHash<QString, QDomDocument*> m_schemaDomDocs; // key is namespace...mem owned here
	QDomDocument m_wsdlDomDoc;
	SchemaInfo m_wsdlInfo;
	QHash<QString, WsdlMethod*> m_wsdlMethods; //key is ns:name

public:
	WsdlFile(const QString& hostName, const QString& fileName, QObject* parent=Q_NULLPTR);
	~WsdlFile();

	QStringList EnabledMethodNames();
	const QList<WsdlMethod*> EnabledMethods();
	QString FileName() const {return m_fileName;}
	static QDomElement FindElementNodeById(QDomElement parentNode, qint64 id);
	QString HostName() {return m_hostName;}

	static QJsonDocument JsonDoc(const QByteArray& data);

	WsdlMethod* Method(const QString& methodName) {return m_wsdlMethods.value(methodName, Q_NULLPTR);}
	QHash<QString, WsdlMethod*> Methods() {return m_wsdlMethods;}
	QDomDocument MethodTemplate(const QString& method);
	QDomDocument MethodTemplateRequest(const QString& method);
	QDomDocument MethodTemplateResponse(const QString& method);

	QString NamespaceByPrefix(const QString& prefix) const {return m_wsdlInfo.PrefixNamespaceLookup.value(prefix, "");}

	QDomDocument Parse(const QString& methodType);
	void SaveMethodTemplate(const QString& method, const QDomDocument& doc);
	static QString SchemaTag(const QString& prefix, const QString& tag) {return ((prefix.isEmpty()) ? tag : QString("%1:%2").arg(prefix, tag));}
	void SetMethodEnabled(const QString& method, bool isChecked);

	static void WriteJsonAttrEnumInfo(QDomElement node, const QString& attrName, const QString& key, QJsonValue val);
	static void WriteJsonAttrInfo(QDomElement node, const QString& attrName, const QString& key, QJsonValue val);
	static void WriteJsonAttrInfo(QDomElement node, const QString& attrName, QHash<QString, QJsonValue> values);
	static void WriteJsonEnumInfo(QDomElement node, const QString& key, QJsonValue val);
	static void WriteJsonInfo(QDomElement node, const QString& key, QJsonValue val);
	static void WriteJsonInfo(QDomElement node, QHash<QString, QJsonValue> values);
	static void WriteJsonNsInfo(QDomElement node, const NamespaceInfo& nsInfo);

	static QByteArray Xml(const QDomDocument& doc, int indent=2, bool doRemoveInfo=true);
	static QByteArray XmlSoap(const QDomDocument& doc, int indent=2);
	static QByteArray XmlSoap(const TimelineEvent& e, int indent, bool b);

private:
	void Clear();
	QDomDocument* DomDocByNameSpace(const QString& ns, const SchemaInfo& info, QString& path);

	static void Filter(QDomElement& node, bool removeUnchecked=false, bool removeInfo=false);
	QDomElement FindType(const QString& typeName, const QDomDocument* doc, const SchemaInfo& info, SchemaInfo& xsdInfo);
	QDomElement FindType(const QString& typeName, const QDomDocument* xsd, const SchemaInfo& info);

	bool IsXsdPrimitiveType(const QString& type, const SchemaInfo& info);

	QDomDocument Join(const QString& rootNodeName, QList<QDomDocument> list);

	QString JsonFileName() {return WsInfo().WsdlMethodListJsonFileName(m_hostName);}

	void ParseAnnotation(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info, bool isAttr=false, const QString& attrName=QString());
	void ParseAny(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info);
	void ParseAnyAttribute(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info);
	void ParseAttribute(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info);
	void ParseChoice(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info);
	void ParseComplexContent(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info);
	void ParseComplexType(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info, bool isAttr=false, const QString& attrName=QString());
	void ParseElement(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info, bool isRoot=false);
	void ParseEnumeration(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info, bool isAttr=false, const QString& attrName=QString());
	void ParseExtension(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info);
	void ParseFileName(const QString& fileName);
	void ParseNamespaceInfo(QDomElement& node, SchemaInfo& info);
	void ParsePattern(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info, bool isAttr=false, const QString& attrName=QString());
	void ParsePortTypeOp(const QDomElement& srcNode);
	void ParseRestriction(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info, bool isAttr=false, const QString& attrName=QString());
	void ParseSchemaInfo(QDomDocument* doc, SchemaInfo& info);
	void ParseSchemaInfo(const QDomElement& schema, SchemaInfo& info);
	QDomElement ParseSchemaForElement(const QDomElement& schemaNode, const QString& elementName, const SchemaInfo& info);
	void ParseSequence(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info);
	void ParseSimpleContent(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info);
	QString ParseSoapHeaderInOutType(const QString& method, const QString& inputOutputTag);
	QString ParseSoapMessageType(const QString& message);

	void SetDomElementId(QDomElement& node);

signals:
	void WsdlFileChanged(const QString& hostName);

private slots:
	void OnWsdlMethodUpdate() {emit WsdlFileChanged(m_hostName);}
};

#endif // WSDLFILE_H
