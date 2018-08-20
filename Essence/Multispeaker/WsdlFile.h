//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlFile
//

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
const QString TAG_JSON_MIN = "min";
const QString TAG_JSON_MAX = "max";
const QString TAG_JSON_NAMESPACE = "namespace";
const QString TAG_JSON_PATTERN = "pattern";
const QString TAG_JSON_TYPE = "type";
const QString TAG_JSON_USE = "use";
const QString TAG_JSON_USE_REQUIRED = "required";
const QString STR_ATTRIBUTES = "Attributes";

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
  WsdlMethod(const QString& name, QObject* parent=0) : QObject(parent), Desc(""), Input(""), Name(name), Output(""), RequestHeader(""), ResponseHeader("") {}
  ~WsdlMethod() {}
};

//------------------------------------------------------------------------------
// Class SchemaInfo
//
class SchemaInfo
{
public:
  QHash<QString, QString> NamespaceFileNameLookup; 
  QString Path;
  QHash<QString, QString> PrefixNamespaceLookup;
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
// Class WsdlFile
//
class WsdlFile : public QObject
{
  Q_OBJECT
private:
  QString m_fileName; // Actual fileName
  QString m_hostName; // The WSDL Service Host Short Name , i.e. CB MRil
  QHash<QString, QDomDocument*> m_schemaDomDocs; // key is namespace...mem owned here
  QDomDocument m_wsdlDomDoc;
  SchemaInfo m_wsdlInfo;
  QHash<QString, WsdlMethod*> m_wsdlMethods; //key is ns:name

public:
  WsdlFile(const QString& hostName, const QString& fileName, QObject* parent=0);
  ~WsdlFile();

  QStringList EnabledMethodNames();
  const QList<WsdlMethod*> EnabledMethods();
  QString FileName() const {return m_fileName;}
  static QDomElement FindElementNodeById(QDomElement parentNode, qint64 id);
  QString HostName() {return m_hostName;}

  static QJsonDocument JsonDoc(const QByteArray& data);

  WsdlMethod* Method(const QString& methodName) {return m_wsdlMethods.value(methodName, 0);}
  QHash<QString, WsdlMethod*> Methods() {return m_wsdlMethods;}
  QDomDocument MethodTemplate(const QString& method);
  QDomDocument MethodTemplateRequest(const QString& method);
  QDomDocument MethodTemplateResponse(const QString& method);

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

  static QByteArray Xml(const QDomDocument& doc, int indent=2, bool doRemoveInfo=true);
  static QByteArray XmlSoap(const QString& hostName, const QString& methodName, const QDomDocument& doc, int indent=2);

private:
  void Clear();
  QDomDocument* DomDocByNameSpace(const QString& ns, const SchemaInfo& info, QString& path);

  static void Filter(QDomElement node, bool removeUnchecked=false, bool removeInfo=false);
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