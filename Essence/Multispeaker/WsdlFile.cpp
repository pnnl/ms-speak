//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlFile
//

#include <QDebug>
#include <QDomDocument>
#include <QFile>
#include <QFileInfo>
#include <QJsonArray>
#include <QJsonDocument>
#include <QJsonParseError>
#include <QJsonObject>
#include <QSettings>
#include <QTimer>

#include "WsdlFile.h"

const QString SUFFIX_WSDL = "wsdl";
const QString SUFFIX_XSD = "xsd";

const QString TAG_ANNOTATION = "annotation";
const QString TAG_ANY = "any";
const QString TAG_ANY_ATTRIBUTE = "anyAttribute";
const QString TAG_ANY_TYPE = "anyType";
const QString TAG_ATTRIBUTE = "attribute";
const QString TAG_BASE = "base";
const QString TAG_BINDING = "binding";
const QString TAG_CHOICE = "choice";
const QString TAG_COMPLEX_CONTENT = "complexContent";
const QString TAG_COMPLEX_TYPE = "complexType";
const QString TAG_DEFAULT = "default";
const QString TAG_DEFINITIONS = "definitions";
const QString TAG_DOCUMENTATION = "documentation";
const QString TAG_ENVELOPE = "Envelope";
const QString TAG_ELEMENT = "element";
const QString TAG_ENUMERATION = "enumeration";
const QString TAG_EXTENSION = "extension";
const QString TAG_HEADER = "header";
const QString TAG_IMPORT = "import";
const QString TAG_INCLUDE = "include";
const QString TAG_INPUT = "input";
const QString TAG_MAX_OCC = "maxOccurs";
const QString TAG_MAX_OCCURS_UNBOUNDED = "unbounded";
const QString TAG_MESSAGE = "message";
const QString TAG_MIN_OCC = "minOccurs";
const QString TAG_NAME = "name";
const QString TAG_NAMESPACE = "namespace";
const QString TAG_PART = "part";
const QString TAG_PATTERN = "pattern";
const QString TAG_PORT_TYPE = "portType";
const QString TAG_OPERATION = "operation";
const QString TAG_OUTPUT = "output";
const QString TAG_REF = "ref";
const QString TAG_RESTRICTION = "restriction";
const QString TAG_SCHEMA_LOCATION = "schemaLocation";
const QString TAG_SIMPLE_TYPE = "simpleType";
const QString TAG_SIMPLE_CONTENT = "simpleContent";
const QString TAG_SCHEMA = "schema";
const QString TAG_SEQUENCE = "sequence";
const QString TAG_STRING = "string";
const QString TAG_SOAP_BODY = "Body";
const QString TAG_SOAP_HEADER = "Header";
const QString TAG_TARGET_NAMESPACE = "targetNamespace";
const QString TAG_TYPE = "type";
const QString TAG_TYPES = "types";
const QString TAG_USE = "use";
const QString TAG_VALUE = "value";

const QString STR_REQUEST = "Request";
const QString STR_RESPONSE= "Response";
const QString STR_SCHEMA_NS_XMLSOAP_ORG_SCHEMA = "http://schemas.xmlsoap.org/wsdl/";
const QString STR_SCHEMA_NS_XMLSOAP_ORG_SOAP_ENVELOPE = "http://schemas.xmlsoap.org/soap/envelope/";
const QString STR_SCHEMA_NS_XMLSOAP_ORG_WSDL = "http://schemas.xmlsoap.org/wsdl/";
const QString STR_SCHEMA_NS_XMLSOAP_ORG_WSDL_SOAP = "http://schemas.xmlsoap.org/wsdl/soap/";
const QString STR_SCHEMA_NS_W3_ORG_2001_XMLSCHEMA = "http://www.w3.org/2001/XMLSchema";
const QString STR_SCHEMA_NS_W3_ORG_2001_XMLSCHEMA_INSTANCE = "http://www.w3.org/2001/XMLSchema-instance";

const QString STR_TARGET_NAMESPACE = "targetNamespace";
const QString STR_XMLNS = "xmlns";
const QString STR_XSD = "xsd";
const QString STR_XSI = "xsi";

// These local variables are necessary to give each element in the parsed dom a unique id in the __ID__ attribute
qint64 ID_COUNTER = 0;

//------------------------------------------------------------------------------
// WsdlFile
//
WsdlFile::WsdlFile(const QString& hostName, const QString& fileName, QObject* parent)
  : QObject(parent),
  m_fileName(fileName),
  m_hostName(hostName),
  m_wsdlDomDoc("wsdl"),
  m_wsdlInfo(QFileInfo(fileName).path())
{
  ID_COUNTER = QSettings().value(SK_ID_COUNTER, 0).toLongLong(); // Get the latest value written after the last parse
  ParseFileName(fileName);
}
//------------------------------------------------------------------------------
// ~WsdlFile
//
WsdlFile::~WsdlFile()
{
  Clear();
}
//------------------------------------------------------------------------------
// EnabledMethodNames
//
QStringList WsdlFile::EnabledMethodNames()
{
  QStringList methodNames;

  // Get enable / disable methods from json file
  QFile file(JsonFileName());
  if (!file.open(QIODevice::ReadOnly))
    return methodNames;

  QJsonDocument jsonDoc = JsonDoc(file.readAll());
  file.close();
  QJsonObject obj = jsonDoc.object();

  // Assumed that methods are disabled until physically set by user and placed in json file
  // Only place the true values in 
  for (QJsonObject::const_iterator it = obj.constBegin(); it != obj.constEnd(); ++it)
  {
    if (it.value().toBool())
      methodNames << it.key();
  }
  return methodNames;
}
//------------------------------------------------------------------------------
// EnabledMethods
//
const QList<WsdlMethod*> WsdlFile::EnabledMethods()
{
  QList<WsdlMethod*> methods;

  // Get enable / disable methods from json file
  QFile file(JsonFileName());
  if (!file.open(QIODevice::ReadOnly))
    return methods;

  QJsonDocument jsonDoc = JsonDoc(file.readAll());
  file.close();
  QJsonObject obj = jsonDoc.object();

  // Assumed that methods are disabled until physically set by user and placed in json file
  // Only place the true values in 
  for (QJsonObject::const_iterator it = obj.constBegin(); it != obj.constEnd(); ++it)
  {
    if (it.value().toBool())
    {
      if (m_wsdlMethods.contains(it.key()))
        methods << m_wsdlMethods.value(it.key());
    }
  }
  return methods;
}
//------------------------------------------------------------------------------
// JsonDoc
//
QJsonDocument WsdlFile::JsonDoc(const QByteArray& data)
{
  QJsonDocument jsonDoc;
  if (!data.isEmpty())
  {
    QJsonParseError err;
    jsonDoc = QJsonDocument::fromJson(data, &err);
    if (err.error != QJsonParseError::NoError)
      qDebug() << err.errorString();
  }
  return jsonDoc;
}
//------------------------------------------------------------------------------
// MethodTemplate
//
QDomDocument WsdlFile::MethodTemplate(const QString& method)
{
  QDomDocument doc;
  QString fileName = WsInfo().WsdlMethodTemplateFileName(m_hostName, method);
  if (!QFileInfo(fileName).exists())
  {
    if (WsdlMethod* wm = m_wsdlMethods.value(method, 0))
    {
      QList<QDomDocument> list;
      list.append(Parse(wm->RequestHeader));
      list.append(Parse(wm->Input));
      list.append(Parse(wm->ResponseHeader));
      list.append(Parse(wm->Output));
      doc = Join(method, list);
      SaveMethodTemplate(method, doc);
    }
    return doc;
  }
  else
  {
    QFile file(fileName);
    if (!file.open(QIODevice::ReadOnly))
    {
      qDebug() << file.error() << file.errorString();
      return doc;
    }
    QString errMsg;
    int errorLine;
    int errorColumn;
    if (!doc.setContent(&file, &errMsg, &errorLine, &errorColumn))
      qDebug() << "Error--Unable to set Content of DOM file" << endl << errMsg << errorLine << errorColumn;
    file.close();
    return doc;
  }
}
//------------------------------------------------------------------------------
// MethodTemplateRequest
//
QDomDocument WsdlFile::MethodTemplateRequest(const QString& method)
{
  QDomDocument doc;
  QDomElement templateRoot = MethodTemplate(method).documentElement();
  QDomElement root = doc.createElement(STR_REQUEST);
  doc.appendChild(root);

  QDomElement templateNode = templateRoot.firstChildElement();
  QDomElement node = templateNode.cloneNode().toElement(); // Header
  Filter(node, true, false);
  root.appendChild(node);

  node = templateNode.nextSibling().cloneNode().toElement(); // Body
  Filter(node, true, false);
  root.appendChild(node);

  return doc;
}
//------------------------------------------------------------------------------
// MethodTemplateResponse
//
QDomDocument WsdlFile::MethodTemplateResponse(const QString& method)
{
  QDomDocument doc;
  QDomElement templateRoot = MethodTemplate(method).documentElement();
  QDomElement root = doc.createElement(STR_RESPONSE);
  doc.appendChild(root);

  QDomElement templateNode = templateRoot.firstChildElement(); // REQ Header
  templateNode = templateNode.nextSiblingElement(); // REQ Body

  templateNode = templateNode.nextSiblingElement(); // RES Header
  QDomElement node = templateNode.cloneNode().toElement();
  Filter(node, true, false);
  root.appendChild(node);

  templateNode = templateNode.nextSiblingElement(); // RES Body
  node = templateNode.cloneNode().toElement();
  Filter(node, true, false);
  root.appendChild(node);

  return doc;
}
//------------------------------------------------------------------------------
// Parse
//
QDomDocument WsdlFile::Parse(const QString& methodType)
{
  QDomDocument xml;
  QDomElement root = xml.createElement(methodType);
  SetDomElementId(root);
  xml.appendChild(root);

  if (methodType.contains(":"))
  {
    // Get Correct dom file for this namespace
    QString ns = methodType.split(":").first();
    QString type = methodType.split(":").last();
    root.setTagName(type);
    QString path = m_wsdlInfo.Path;
    QDomDocument* doc = DomDocByNameSpace(m_wsdlInfo.PrefixNamespaceLookup.value(ns), m_wsdlInfo, path);
    Q_ASSERT(doc);
    SchemaInfo info(path);
    ParseSchemaInfo(doc, info);

    // Search the elements under the schema element looking for this type
    QDomElement docElem = doc->documentElement();
    //qDebug() << "DocElem TagName: " << docElem.tagName();
    QDomElement elementNode;
    if (docElem.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_SCHEMA))
      elementNode = ParseSchemaForElement(docElem, type, info); // this is most likely a schema
    else
    {
      // There can be 1 or more schema elements in the wsdl
      QDomNodeList list = docElem.elementsByTagName(SchemaTag(info.XmlSchemaPrefix, TAG_SCHEMA));
      //qDebug() << type << list.count();
      for (int i = 0; i < list.count(); ++i)
      {
        QDomElement schemaNode = list.at(i).toElement();
        //qDebug() << "Schema Tag:" << schemaNode.tagName();
        elementNode = ParseSchemaForElement(schemaNode, type, info); // this is most likely a schema
        if (!elementNode.isNull())
          break; // found it
      }
    }
    // Found the Element Node with the name we are looking for
    if (!elementNode.isNull())
    {
      ParseElement(elementNode, root, info, true);
    }
  }
  else 
  {
    Q_ASSERT(false); // Need to implement????
  }
  QSettings().setValue(SK_ID_COUNTER, ID_COUNTER);
  return xml;
}
//------------------------------------------------------------------------------
// SaveMethodTemplate
//
void WsdlFile::SaveMethodTemplate(const QString& method, const QDomDocument& doc)
{
  QString fileName = WsInfo().WsdlMethodTemplateFileName(m_hostName, method);

  QFile file(fileName);
  if (!file.open(QIODevice::WriteOnly))
    qDebug() << file.error() << file.errorString();

  QByteArray bytes = doc.toByteArray(2);
  file.write(bytes);
  if (file.error() != QFileDevice::NoError)
    qDebug() << "ERROR:" << file.error() << file.errorString();

  file.close();
}
//------------------------------------------------------------------------------
// SetMethodEnabled
//
void WsdlFile::SetMethodEnabled(const QString& method, bool isChecked)
{
  // Write enable / disable methods to json file
  QFile file(JsonFileName());
  QByteArray data;
  if (file.open(QIODevice::ReadOnly))
  {
    data = file.readAll();
    qDebug() <<  "Error" << QString("Error Reading Json File, %1").arg(file.fileName()) << file.errorString();
  }
  file.close();
  QJsonParseError err;
  QJsonDocument jsonDoc = QJsonDocument::fromJson(data, &err);
  if (err.error != QJsonParseError::NoError)
  {
    qDebug() << err.errorString();
  }
  QJsonObject obj = jsonDoc.object();
  obj.insert(method, QJsonValue(isChecked));
  jsonDoc.setObject(obj);
  if (file.open(QIODevice::WriteOnly))
  {
    if (file.write(jsonDoc.toJson()) == -1)
      qDebug() <<  "Error" << QString("Error Writing Json File, %1").arg(file.fileName()) << file.errorString();
  }
  file.close();
  QTimer::singleShot(0, this, SLOT(OnWsdlMethodUpdate())); // Give the UI a chance to catch up
}
//------------------------------------------------------------------------------
// WriteJsonAttrEnumInfo
//
void WsdlFile::WriteJsonAttrEnumInfo(QDomElement node, const QString& attrName, const QString& key, QJsonValue val)
{
  QJsonDocument jsonInfo = JsonDoc(node.attribute(TAG_JSON_ATTR).toLatin1());
  QJsonObject jsonObj = jsonInfo.object();
  QJsonObject jsonAttrObj = jsonInfo.object().find(attrName).value().toObject();

  QJsonObject jsonEnumObj = jsonAttrObj.find(TAG_JSON_ENUM).value().toObject();
  jsonEnumObj.insert(key, val);
  jsonAttrObj.insert(TAG_JSON_ENUM, jsonEnumObj);

  jsonObj.insert(attrName, jsonAttrObj);
  jsonInfo.setObject(jsonObj);
  node.setAttribute(TAG_JSON_ATTR, QString(jsonInfo.toJson(QJsonDocument::Compact)));
}
//------------------------------------------------------------------------------
// WriteJsonAttrInfo
//
void WsdlFile::WriteJsonAttrInfo(QDomElement node, const QString& attrName, const QString& key, QJsonValue val)
{
  Q_ASSERT(key != TAG_JSON_ENUM); // Handle this in another function
  QJsonDocument jsonInfo = JsonDoc(node.attribute(TAG_JSON_ATTR).toLatin1());
  QJsonObject jsonObj = jsonInfo.object();
  QJsonObject jsonAttrObj = jsonInfo.object().find(attrName).value().toObject();

  if (key == TAG_JSON_DESC)
  {
    QString desc = val.toString() + jsonAttrObj.value(TAG_JSON_DESC).toString(); 
    jsonAttrObj.insert(key, QJsonValue(desc));
  }
  else
    jsonAttrObj.insert(key, val);

  jsonObj.insert(attrName, jsonAttrObj);
  jsonInfo.setObject(jsonObj);
  node.setAttribute(TAG_JSON_ATTR, QString(jsonInfo.toJson(QJsonDocument::Compact)));
}
//------------------------------------------------------------------------------
// WriteJsonAttrInfo
//
void WsdlFile::WriteJsonAttrInfo(QDomElement node, const QString& attrName, QHash<QString, QJsonValue> values)
{
  QJsonDocument jsonInfo = JsonDoc(node.attribute(TAG_JSON_ATTR).toLatin1());
  QJsonObject jsonObj = jsonInfo.object();
  QJsonObject jsonAttrObj = jsonInfo.object().find(attrName).value().toObject();

  foreach (QString key, values.keys())
  {
    Q_ASSERT(key != TAG_JSON_ENUM); // Handle this in another function
    if (key == TAG_JSON_DESC)
    {
      QString desc = values.value(key).toString() + jsonAttrObj.value(TAG_JSON_DESC).toString(); 
      jsonAttrObj.insert(key, QJsonValue(desc));
    }
    else
      jsonAttrObj.insert(key, values.value(key));
  }

  jsonObj.insert(attrName, jsonAttrObj);
  jsonInfo.setObject(jsonObj);
  node.setAttribute(TAG_JSON_ATTR, QString(jsonInfo.toJson(QJsonDocument::Compact)));
}
//------------------------------------------------------------------------------
// WriteJsonEnumInfo
//
void WsdlFile::WriteJsonEnumInfo(QDomElement node, const QString& key, QJsonValue val)
{
  QJsonDocument jsonInfo = JsonDoc(node.attribute(TAG_JSON_INFO).toLatin1());
  QJsonObject jsonObj = jsonInfo.object();
  QJsonObject jsonEnumObj = jsonObj.find(TAG_JSON_ENUM).value().toObject();
  jsonEnumObj.insert(key, val);
  jsonObj.insert(TAG_JSON_ENUM, jsonEnumObj);
  jsonInfo.setObject(jsonObj);
  node.setAttribute(TAG_JSON_INFO, QString(jsonInfo.toJson(QJsonDocument::Compact)));
}
//------------------------------------------------------------------------------
// WriteJsonInfo
//
void WsdlFile::WriteJsonInfo(QDomElement node, const QString& key, QJsonValue val)
{
  Q_ASSERT(key != TAG_JSON_ENUM); // Handle this in another function WriteJsonEnumInfo
  QJsonDocument jsonInfo = JsonDoc(node.attribute(TAG_JSON_INFO).toLatin1());
  QJsonObject jsonObj = jsonInfo.object();

  // If there already is a desc...that means a type desc so just prepend this new desc
  if (key == TAG_JSON_DESC)
  {
    QString desc = val.toString() + jsonObj.value(TAG_JSON_DESC).toString(); 
    jsonObj.insert(key, QJsonValue(desc));
  }
  else
    jsonObj.insert(key, val);
  jsonInfo.setObject(jsonObj);
  node.setAttribute(TAG_JSON_INFO, QString(jsonInfo.toJson(QJsonDocument::Compact)));
}
//------------------------------------------------------------------------------
// WriteJsonInfo
//
void WsdlFile::WriteJsonInfo(QDomElement node, QHash<QString, QJsonValue> values)
{
  QJsonDocument jsonInfo = JsonDoc(node.attribute(TAG_JSON_INFO).toLatin1());
  QJsonObject jsonObj = jsonInfo.object();
  foreach (QString key, values.keys())
  {
    Q_ASSERT(key != TAG_JSON_ENUM); // Handle this in another function
    if (key == TAG_JSON_DESC)
    {
      QString desc = values.value(key).toString() + jsonObj.value(TAG_JSON_DESC).toString(); 
      jsonObj.insert(key, QJsonValue(desc));
    }
    else
      jsonObj.insert(key, values.value(key));
  }
  jsonInfo.setObject(jsonObj);
  node.setAttribute(TAG_JSON_INFO, QString(jsonInfo.toJson(QJsonDocument::Compact)));
}
//------------------------------------------------------------------------------
// Xml
//
QByteArray WsdlFile::Xml(const QDomDocument& doc, int indent, bool doRemoveInfo)
{
  QDomDocument xml;
  QDomElement docRoot = doc.documentElement();
  QDomElement root = xml.createElement(docRoot.tagName());
  xml.appendChild(root);

  QDomElement docNode = docRoot.firstChildElement();
  while (!docNode.isNull())
  {
    QDomElement node = docNode.cloneNode().toElement();
    root.appendChild(node); // Append the child before filter otherwise node will not be filtered correctly if unchecked
    Filter(node, true, doRemoveInfo);
    docNode = docNode.nextSiblingElement();
  }

  return xml.toByteArray(indent);
}
//------------------------------------------------------------------------------
// XmlSoap
//
QByteArray WsdlFile::XmlSoap(const QString& hostName, const QString& methodName, const QDomDocument& doc, int indent)
{
  QDomElement docRoot = doc.documentElement();
  QDomElement docHeaderNode = docRoot.firstChildElement();
  QDomElement docBodyNode = docHeaderNode.nextSiblingElement();

  QDomElement soapHeaderContentsNode = docHeaderNode.cloneNode().toElement();
  QDomElement soapBodyContentsNode = docBodyNode.cloneNode().toElement();

  Filter(soapHeaderContentsNode, true, true);
  Filter(soapBodyContentsNode, true, true);

  QDomDocument xml;
  QDomElement soapRoot = xml.createElement(SchemaTag(STR_SOAP, TAG_ENVELOPE));
  soapRoot.setAttribute(SchemaTag(STR_XMLNS, STR_SOAP), STR_SCHEMA_NS_XMLSOAP_ORG_SOAP_ENVELOPE);
  soapRoot.setAttribute(SchemaTag(STR_XMLNS, STR_XSI), STR_SCHEMA_NS_W3_ORG_2001_XMLSCHEMA_INSTANCE);
  soapRoot.setAttribute(SchemaTag(STR_XMLNS, STR_XSD), STR_SCHEMA_NS_W3_ORG_2001_XMLSCHEMA);
  xml.appendChild(soapRoot);

  QDomElement soapHeaderNode = xml.createElement(SchemaTag(STR_SOAP, TAG_SOAP_HEADER));
  soapRoot.appendChild(soapHeaderNode);
  soapHeaderNode.appendChild(soapHeaderContentsNode);

  QDomElement soapBodyNode = xml.createElement(SchemaTag(STR_SOAP, TAG_SOAP_BODY));
  soapRoot.appendChild(soapBodyNode);
  soapBodyNode.appendChild(soapBodyContentsNode);

  QByteArray bytes;
  if (docRoot.tagName() == STR_REQUEST)
    bytes.append(QString("SOAPAction: %1/%2\n").arg(hostName, methodName).toLatin1());

  bytes.append("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n");   

  bytes.append(xml.toByteArray(indent));
  return bytes;
}
//------------------------------------------------------------------------------
// Clear
//
void WsdlFile::Clear()
{
  qDeleteAll(m_schemaDomDocs);
  qDeleteAll(m_wsdlMethods);
}
//------------------------------------------------------------------------------
// Filter
//
// Will physically alter the dom node based on the flags
//
void WsdlFile::Filter(QDomElement node, bool removeUnchecked, bool removeInfo)
{
  QJsonDocument jsonInfoDoc = WsdlFile::JsonDoc(node.attributeNode(TAG_JSON_INFO).value().toLatin1());
  if (removeUnchecked && !jsonInfoDoc.object().find(TAG_JSON_IS_USER_CHECKED).value().toBool())
  {
    QDomNode parentNode = node.parentNode();
    node.parentNode().removeChild(node); // Remove Node and we are done
  }
  else if (removeUnchecked) // Remove the unchecked attributes from json
  {
    // Remove the unchecked Attr Nodes
    QDomAttr attrJsonNode = node.attributeNode(TAG_JSON_ATTR);
    QStringList uncheckedAttrList;
    if (!attrJsonNode.isNull())
    {
      QJsonDocument jsonInfo = JsonDoc(node.attribute(TAG_JSON_ATTR).toLatin1());
      QJsonObject jsonObj = jsonInfo.object();

      foreach (const QString key, jsonObj.keys())
      {
        QJsonObject jsonAttrObj = jsonInfo.object().find(key).value().toObject();
        if (!jsonAttrObj.find(TAG_JSON_IS_USER_CHECKED).value().toBool())
        {
          jsonObj.remove(key);
          uncheckedAttrList << key;
        }
      }
      jsonInfo.setObject(jsonObj);
      node.setAttribute(TAG_JSON_ATTR, QString(jsonInfo.toJson(QJsonDocument::Compact)));
      foreach (const QString key, uncheckedAttrList)
        node.removeAttribute(key);
    }
    // Do Children
    QDomElement childNode = node.firstChildElement();
    while (!childNode.isNull())
    {
      QDomElement siblingNode = childNode.nextSiblingElement(); // Get Sibling before recursive call to RemoveInfo can possibly remove childNode
      Filter(childNode, removeUnchecked, removeInfo);
      childNode = siblingNode;
    }
  }
  if (removeInfo)
  {
    node.removeAttribute(TAG_JSON_ATTR);
    node.removeAttribute(TAG_JSON_INFO);
    node.removeAttribute(TAG_JSON_ID);
  }
}
//------------------------------------------------------------------------------
// FindElementNodeById
//
QDomElement WsdlFile::FindElementNodeById(QDomElement parentNode, qint64 id)
{
  QDomElement foundNode;
  if (id == parentNode.attribute(TAG_JSON_ID).toLongLong())
    foundNode = parentNode;
  else
  {
    QDomElement child = parentNode.firstChildElement();
    while (!child.isNull())
    {
      foundNode = FindElementNodeById(child, id);
      if (!foundNode.isNull())
        break;
      child = child.nextSiblingElement();
    }
  }
  return foundNode;
}
//------------------------------------------------------------------------------
// DomDocByNameSpace
//
//  Return
//    path - the actual path of the DomDocument returned
//
QDomDocument* WsdlFile::DomDocByNameSpace(const QString& ns, const SchemaInfo& info, QString& path)
{
  if (ns == info.TargetNamespace && info.NamespaceFileNameLookup.count() == 0)
    return &m_wsdlDomDoc; // Use this File

  if (!m_schemaDomDocs.contains(ns))
  {
    QString fileName = info.NamespaceFileNameLookup.value(ns, "");
    Q_ASSERT(!fileName.isEmpty());

    fileName = info.Path + "/" + fileName;
    
    QFileInfo fileInfo(fileName);
    if (!fileInfo.exists())
    {
      qDebug() << "Error" << QString("%1 Does not Exist!").arg(fileName);
      return 0;
    }

    QFile file(fileName);
    QDomDocument* doc = new QDomDocument(ns);
    if (!doc->setContent(&file))
    {
      qDebug() << "Error--Unable to set Content of DOM file";
      return 0;
    }
    file.close();
    m_schemaDomDocs.insert(ns, doc);
    path.clear();
    path.insert(0, QFileInfo(fileName).path());
  }
  return m_schemaDomDocs.value(ns, 0);
}
//------------------------------------------------------------------------------
// FindType
//
//  info is the src 
//  xsdInfo is the new info for the doc where the typeName was found
//  Returns the QDomElement for the schema (complex or simple type in the xsd schema doc)
//
QDomElement WsdlFile::FindType(const QString& typeName, const QDomDocument* doc, const SchemaInfo& info, SchemaInfo& xsdInfo)
{
  QStringList typeParts = typeName.split(":");
  if (typeParts.count() != 1)
  {
    // Need to go look in another namespace for this type
    Q_ASSERT(typeParts.count() == 2);
    if (typeParts.count() != 2)
      qDebug() << "ERROR Bad Type" << typeParts;
    QString ns = info.PrefixNamespaceLookup.value(typeParts.first());
    QString type = typeParts.last();

    // Find Dom and Element based on ns and type
    QString path = info.Path;
    Q_ASSERT(DomDocByNameSpace(ns, info, path));
    if (QDomDocument* xsd = DomDocByNameSpace(ns, info, path))
    {
      // Set the xsdInfo path to be based on info's represention of it
      xsdInfo.Path = QFileInfo(info.Path + "/" + info.NamespaceFileNameLookup.value(ns)).path();
      ParseSchemaInfo(xsd, xsdInfo);
      return FindType(type, xsd, xsdInfo); 
    }
  }
  else // Type is defined in this namespace
  {
    return FindType(typeName, doc, info); 
  }
  Q_ASSERT(false);
  return QDomElement();
}
//------------------------------------------------------------------------------
// FindType
//
//  Returns the QDomElement for the schema complex or simple type in the xsd schema doc
//
QDomElement WsdlFile::FindType(const QString& typeName, const QDomDocument* xsd, const SchemaInfo& info)
{
  QDomElement element;
  QDomNodeList list = xsd->elementsByTagName(SchemaTag(info.XmlSchemaPrefix, TAG_COMPLEX_TYPE));
  for (int i = 0; i < list.count(); ++i)
  {
    QDomNode node = list.at(i);
    //qDebug() << node.toElement().tagName() << node.toElement().attribute(TAG_NAME);
    if (node.hasAttributes() && node.toElement().attribute(TAG_NAME) == typeName)
    { 
      //qDebug() << "FindType Complex" << typeName << info.TargetNamespace;
      element = node.toElement();
      break;
    }
  }
  if (!element.isNull())
    return element;

  list = xsd->elementsByTagName(SchemaTag(info.XmlSchemaPrefix, TAG_SIMPLE_TYPE));
  for (int i = 0; i < list.count(); ++i)
  {
    QDomNode node = list.at(i);
    //qDebug() << node.toElement().tagName() << node.toElement().attribute(TAG_NAME);
    if (node.hasAttributes() && node.toElement().attribute(TAG_NAME) == typeName)
    { 
      //qDebug() << "FindType Simple" << typeName << info.TargetNamespace;
      element = node.toElement();
      break;
    }
  }
  if (!element.isNull())
    return element;

  // Must be an element
  QDomElement schemaNode = xsd->documentElement();
  Q_ASSERT(schemaNode.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_SCHEMA));
  if (schemaNode.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_SCHEMA))
    element = ParseSchemaForElement(schemaNode, typeName, info);

  if (!element.isNull())
    return element;

  qDebug() << "ERROR: Type Not Found" << info.TargetNamespace << typeName;
  return element;
}
//------------------------------------------------------------------------------
// IsXsdPrimitiveType
//
bool WsdlFile::IsXsdPrimitiveType(const QString& type, const SchemaInfo& info) 
{
  if (info.XmlSchemaPrefix.isEmpty() && !type.contains(":"))
    return true;
  else
  {
    if (type.contains(":") && type.split(":").first() == info.XmlSchemaPrefix)
      return true;
    else
      return false;
  }
}
//------------------------------------------------------------------------------
// Join
//
QDomDocument WsdlFile::Join(const QString& rootNodeName, QList<QDomDocument> list)
{
  QDomDocument doc;
  QDomElement root = doc.createElement(rootNodeName);
  doc.appendChild(root);
  qDebug() << QString(doc.toByteArray(2));
  for (int i = 0; i < list.count(); ++i)
    root.appendChild(list.at(i).documentElement().cloneNode());

  qDebug() << QString(doc.toByteArray(2));
  return doc;
}
//------------------------------------------------------------------------------
// ParseAnnotation
//
void WsdlFile::ParseAnnotation(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info, bool isAttr, const QString& attrName)
{
  //qDebug() << "ParseAnnotation" << srcNode.tagName() << srcNode.attribute(TAG_NAME) << info.TargetNamespace << "DST" << dstNode.tagName(); 
  QDomElement srcNodeChild = srcNode.firstChild().toElement(); // Assume that there is a child element tag documentation
  if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_DOCUMENTATION))
  {
    if (isAttr)
      WriteJsonAttrInfo(dstNode, attrName, TAG_JSON_DESC, QJsonValue(srcNodeChild.text()));
    else
      WriteJsonInfo(dstNode, TAG_JSON_DESC, QJsonValue(srcNodeChild.text()));
  }
  else
  {
    qDebug() << "Unknown TAG" << srcNodeChild.tagName();
    Q_ASSERT(false);
  }
}
//------------------------------------------------------------------------------
// ParseAny
//
void WsdlFile::ParseAny(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info)
{
  //qDebug() << "ParseAny" << srcNode.tagName() << srcNode.attribute(TAG_NAME) << srcNode.attribute(TAG_TYPE) << info.TargetNamespace << "DST" << dstNode.tagName();
  QString ns = srcNode.attribute(TAG_NAMESPACE);
  QString max = srcNode.attribute(TAG_MAX_OCC);
  QString min = srcNode.attribute(TAG_MIN_OCC);

  QDomElement dstElement = dstNode.ownerDocument().createElement(TAG_ANY);
  SetDomElementId(dstElement);
  dstNode.appendChild(dstElement);
  
  QHash<QString, QJsonValue> jsonValues;
  if (!ns.isEmpty())
    jsonValues.insert(TAG_JSON_NAMESPACE, QJsonValue(ns));
  if (!min.isEmpty()) 
    jsonValues.insert(TAG_JSON_MIN, QJsonValue(min));
  if (!max.isEmpty()) 
  {
    if (max == TAG_MAX_OCCURS_UNBOUNDED)
      WriteJsonInfo(dstNode, TAG_JSON_IS_ARRAY_CONTAINER, QJsonValue(true));
    jsonValues.insert(TAG_JSON_MAX, QJsonValue(max));
  }
  jsonValues.insert(TAG_JSON_IS_USER_CHECKED, QJsonValue(false));

  WriteJsonInfo(dstElement, jsonValues);

  // Check for Annotation for this element
  QDomElement srcNodeChild = srcNode.firstChildElement();
  while (!srcNodeChild.isNull())
  {
    if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ANNOTATION))
    {
      ParseAnnotation(srcNodeChild, dstElement, info);
    }
    else 
    {
      qDebug() << "Unknown TAG" << srcNodeChild.tagName();
      Q_ASSERT(false);
    }
    srcNodeChild = srcNodeChild.nextSiblingElement();
  }

  // If this element does not have child nodes then it must need a text element for the value 
  if (!dstElement.hasChildNodes())
    dstElement.appendChild(dstNode.ownerDocument().createTextNode("?"));
}
//------------------------------------------------------------------------------
// ParseAnyAttribute
//
void WsdlFile::ParseAnyAttribute(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info)
{
  //qDebug() << "ParseAnyAttribute" << srcNode.tagName() << srcNode.attribute(TAG_NAME) << srcNode.attribute(TAG_TYPE) << info.TargetNamespace << "DST" << dstNode.tagName();
  QString ns = srcNode.attribute(TAG_NAMESPACE);

  dstNode.setAttribute(TAG_ANY_ATTRIBUTE, "?"); // Put a place holder in as a value for this attribute.

  QHash<QString, QJsonValue> jsonValues;
  jsonValues.insert(TAG_JSON_NAMESPACE, QJsonValue(ns));
  jsonValues.insert(TAG_JSON_IS_USER_CHECKED, QJsonValue(false));
  
  WriteJsonAttrInfo(dstNode, TAG_ANY_ATTRIBUTE, jsonValues);

  // Handle any annotation
  QDomElement srcNodeChild = srcNode.firstChildElement();
  while (!srcNodeChild.isNull())
  {
    if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ANNOTATION))
    {
      QDomElement srcNodeChildChild = srcNodeChild.firstChild().toElement(); // Assume that there is a child element tag documentation
      if (srcNodeChildChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_DOCUMENTATION))
        WriteJsonAttrInfo(dstNode, ns, TAG_JSON_DESC, QJsonValue(srcNodeChildChild.text()));
    }
    else
    {
      qDebug() << "Unknown TAG" << srcNodeChild.tagName();
      Q_ASSERT(false);
    }
    srcNodeChild = srcNodeChild.nextSiblingElement();
  }
}
//------------------------------------------------------------------------------
// ParseAttribute
//
void WsdlFile::ParseAttribute(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info)
{
  //qDebug() << "ParseAttribute" << srcNode.tagName() << srcNode.attribute(TAG_NAME) << srcNode.attribute(TAG_TYPE) << info.TargetNamespace << "DST" << dstNode.tagName();
  QString name = srcNode.attribute(TAG_NAME);
  QString type = srcNode.attribute(TAG_TYPE);
  QString use = srcNode.attribute(TAG_USE);
  QString def = srcNode.attribute(TAG_DEFAULT);

  dstNode.setAttribute(name, "?"); // Put a place holder in as a value for this attribute.

  QHash<QString, QJsonValue> jsonValues;
  jsonValues.insert(TAG_JSON_TYPE, QJsonValue(type));
  if (!use.isEmpty())
  {
    jsonValues.insert(TAG_JSON_USE, QJsonValue(use));
    if (use == TAG_JSON_USE_REQUIRED)
      jsonValues.insert(TAG_JSON_IS_USER_CHECKED, QJsonValue(true));
    else
      jsonValues.insert(TAG_JSON_IS_USER_CHECKED, QJsonValue(false));
  }

  if (!def.isEmpty())
    jsonValues.insert(TAG_JSON_DEFAULT, QJsonValue(def));
  
  WriteJsonAttrInfo(dstNode, name, jsonValues);

  // If this type is not a primitive xml xsd type then find and parse the complex type
  if (!IsXsdPrimitiveType(type, info))
  {
    SchemaInfo xsdInfo(info);
    QDomDocument doc = srcNode.ownerDocument();
    QDomElement typeElement = FindType(type, &doc, info, xsdInfo);
    Q_ASSERT(!typeElement.isNull());
    ParseComplexType(typeElement, dstNode, xsdInfo, true, name);
  }

  // Handle any annotation
  QDomElement srcNodeChild = srcNode.firstChildElement();
  while (!srcNodeChild.isNull())
  {
    if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ANNOTATION))
    {
      QDomElement srcNodeChildChild = srcNodeChild.firstChild().toElement(); // Assume that there is a child element tag documentation
      if (srcNodeChildChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_DOCUMENTATION))
        WriteJsonAttrInfo(dstNode, name, TAG_JSON_DESC, QJsonValue(srcNodeChildChild.text()));
    }
    else
    {
      qDebug() << "Unknown TAG" << srcNodeChild.tagName();
      Q_ASSERT(false);
    }
    srcNodeChild = srcNodeChild.nextSiblingElement();
  }
}
//------------------------------------------------------------------------------
// ParseChoice
//
void WsdlFile::ParseChoice(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info)
{
  //qDebug() << "ParseChoice" << srcNode.tagName() << srcNode.attribute(TAG_NAME) << info.TargetNamespace << "DST" << dstNode.tagName();

  WriteJsonInfo(dstNode, TAG_JSON_CHOICE, QJsonValue(true));

  QDomElement srcNodeChild = srcNode.firstChildElement();
  while (!srcNodeChild.isNull())
  {
    if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ELEMENT))
      ParseElement(srcNodeChild, dstNode, info);
    else
    {
      qDebug() << "Unknown TAG" << srcNodeChild.tagName();
      Q_ASSERT(false);
    }
    srcNodeChild = srcNodeChild.nextSiblingElement();
  }
}
//------------------------------------------------------------------------------
// ParseComplexContent
//
void WsdlFile::ParseComplexContent(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info)
{
  //qDebug() << "ParseComplexContent" << srcNode.tagName() << srcNode.attribute(TAG_NAME) << info.TargetNamespace << "DST" << dstNode.tagName();
  QDomElement srcNodeChild = srcNode.firstChildElement();
  while (!srcNodeChild.isNull())
  {
    if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_EXTENSION))
      ParseExtension(srcNodeChild, dstNode, info);
    else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_RESTRICTION))
      ParseRestriction(srcNodeChild, dstNode, info);
    else
    {
      qDebug() << "Unknown TAG" << srcNodeChild.tagName();
      Q_ASSERT(false);
    }
    srcNodeChild = srcNodeChild.nextSiblingElement();
  }
}
//------------------------------------------------------------------------------
// ParseComplexType
//
void WsdlFile::ParseComplexType(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info, bool isAttr, const QString& attrName)
{
  //qDebug() << "ParseComplexType" << srcNode.tagName() << srcNode.attribute(TAG_NAME) << info.TargetNamespace << "DST" << dstNode.tagName();
  //if (srcNode.attribute(TAG_NAME) == "PointType")
  //  int i = 0;
  QDomElement srcNodeChild = srcNode.firstChildElement();
  while (!srcNodeChild.isNull())
  {
    if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ANNOTATION))
      ParseAnnotation(srcNodeChild, dstNode, info, isAttr, attrName);
    else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_SEQUENCE))
      ParseSequence(srcNodeChild, dstNode, info); // Skip to next level
    else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_RESTRICTION))
      ParseRestriction(srcNodeChild, dstNode, info, isAttr, attrName);
    else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_CHOICE))
      ParseChoice(srcNodeChild, dstNode, info);
    else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_COMPLEX_CONTENT))
      ParseComplexContent(srcNodeChild, dstNode, info);
    else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ELEMENT))
      ParseElement(srcNodeChild, dstNode, info);
    else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_SIMPLE_CONTENT))
      ParseSimpleContent(srcNodeChild, dstNode, info);
    else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ATTRIBUTE))
      ParseAttribute(srcNodeChild, dstNode, info);
    else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ANY_ATTRIBUTE))
      ParseAnyAttribute(srcNodeChild, dstNode, info);
    else
    {
      qDebug() << "Unknown TAG" << srcNodeChild.tagName();
      Q_ASSERT(false);
    }
    srcNodeChild = srcNodeChild.nextSiblingElement();
  }
}
//------------------------------------------------------------------------------
// ParseElement
//
void WsdlFile::ParseElement(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info, bool isRoot)
{
  //qDebug() << "ParseElement" << srcNode.tagName() << srcNode.attribute(TAG_NAME) << srcNode.attribute(TAG_TYPE) << info.TargetNamespace << "DST" << dstNode.tagName();
  QString name = srcNode.attribute(TAG_NAME);
  QString type = srcNode.attribute(TAG_TYPE);
  QString max = srcNode.attribute(TAG_MAX_OCC);
  QString min = srcNode.attribute(TAG_MIN_OCC);
  QString ref = srcNode.attribute(TAG_REF);

  QDomElement dstElement;
  if (isRoot)
    dstElement = dstNode;
  else
  {
    dstElement = dstNode.ownerDocument().createElement((!name.isEmpty()) ? name : ref);
    SetDomElementId(dstElement);
    dstNode.appendChild(dstElement);
  }

  if (!name.isEmpty())
  {
    QHash<QString, QJsonValue> jsonValues;
    if (!type.isEmpty())
      jsonValues.insert(TAG_JSON_TYPE, QJsonValue(type));
    if (!min.isEmpty()) 
      jsonValues.insert(TAG_JSON_MIN, QJsonValue(min));
    if (!max.isEmpty()) 
    {
      if (max == TAG_MAX_OCCURS_UNBOUNDED)
        WriteJsonInfo(dstNode, TAG_JSON_IS_ARRAY_CONTAINER, QJsonValue(true));
      jsonValues.insert(TAG_JSON_MAX, QJsonValue(max));
    }
    if (isRoot)
      jsonValues.insert(TAG_JSON_IS_USER_CHECKED, QJsonValue(true));
    else if (!min.isEmpty() && min.toInt() == 0)
      jsonValues.insert(TAG_JSON_IS_USER_CHECKED, QJsonValue(false));
    else
      jsonValues.insert(TAG_JSON_IS_USER_CHECKED, QJsonValue(true));

    WriteJsonInfo(dstElement, jsonValues);
  }

  if (type.isEmpty() && ref.isEmpty())
  {
    // Need to further drill down this element to find the complex type of this element
    QDomElement complexTypeNode = srcNode.firstChildElement();
    if (complexTypeNode.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_COMPLEX_TYPE))
      ParseComplexType(complexTypeNode, dstElement, info);
    else if (complexTypeNode.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_SIMPLE_TYPE))
      ParseComplexType(complexTypeNode, dstElement, info);
    else
    {
      qDebug() << "Unknown TAG" << complexTypeNode.tagName();
      Q_ASSERT(false);
    }
  }
  else if (!IsXsdPrimitiveType((!type.isEmpty()) ? type : ref, info))
  {
    // Find and parse the complex type
    SchemaInfo xsdInfo(info);
    QDomDocument doc = srcNode.ownerDocument();
    QDomElement typeElement = FindType((!type.isEmpty()) ? type : ref, &doc, info, xsdInfo);
    Q_ASSERT(!typeElement.isNull());
    if (typeElement.tagName() == TAG_ELEMENT)
      ParseElement(typeElement, dstElement, xsdInfo);
    else
      ParseComplexType(typeElement, dstElement, xsdInfo);
  }

  // Check for Annotation for this element
  QDomElement srcNodeChild = srcNode.firstChildElement();
  while (!srcNodeChild.isNull())
  {
    if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ANNOTATION))
      ParseAnnotation(srcNodeChild, dstElement, info);
    srcNodeChild = srcNodeChild.nextSiblingElement();
  }

  // If this element does not have child nodes then it must need a text element for the value 
  if (!dstElement.hasChildNodes() && !name.isEmpty()) // see not above abour ref
  {
    Q_ASSERT(!dstNode.isNull());
    Q_ASSERT(!dstElement.isNull());
    dstElement.appendChild(dstNode.ownerDocument().createTextNode("?"));
  }
}
//------------------------------------------------------------------------------
// ParseEnumeration
//
void WsdlFile::ParseEnumeration(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info, bool isAttr, const QString& attrName)
{
  ////qDebug() << "ParseEnumeration" << srcNode.tagName() << srcNode.attribute(TAG_VALUE) << info.TargetNamespace << "DST" << dstNode.tagName();
  QString value = srcNode.attribute(TAG_VALUE);
  QString desc = "";

  // Check for Annotation for this enum
  QDomElement srcNodeChild = srcNode.firstChild().toElement();
  if (!srcNodeChild.isNull() && srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ANNOTATION))
  {
    QDomElement docElement = srcNodeChild.firstChild().toElement(); // Assume that there is a child element tag documentation
    if (docElement.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_DOCUMENTATION))
    {
      desc = docElement.text();
    }
    else
    {
      qDebug() << "Unknown TAG" << srcNodeChild.tagName();
      Q_ASSERT(false);
    }
  }

  if (isAttr)
    WriteJsonAttrEnumInfo(dstNode, attrName, value, QJsonValue(desc));
  else
    WriteJsonEnumInfo(dstNode, value, QJsonValue(desc));
}
//------------------------------------------------------------------------------
// ParseExtension
//
void WsdlFile::ParseExtension(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info)
{
  //qDebug() << "ParseExtension" << srcNode.tagName() << srcNode.attribute(TAG_BASE) << info.TargetNamespace << "DST" << dstNode.tagName();
  QString base = srcNode.attribute(TAG_BASE);

  // If this type is not a primitive xml xsd type then find and parse the complex type
  if (base == TAG_ANY_TYPE)
    base = SchemaTag(info.XmlSchemaPrefix, TAG_STRING);
  else if (!IsXsdPrimitiveType(base, info))
  {
    SchemaInfo xsdInfo(info);
    QDomDocument doc = srcNode.ownerDocument();
    QDomElement typeElement = FindType(base, &doc, info, xsdInfo);
    Q_ASSERT(!typeElement.isNull());
    ParseComplexType(typeElement, dstNode, xsdInfo);
  }

  QDomElement srcNodeChild = srcNode.firstChildElement();
  while (!srcNodeChild.isNull())
  {
    if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_SEQUENCE))
      ParseSequence(srcNodeChild, dstNode, info);
    else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ATTRIBUTE))
      ParseAttribute(srcNodeChild, dstNode, info);
    else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_CHOICE))
      ParseChoice(srcNodeChild, dstNode, info);
    else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ANY_ATTRIBUTE))
      ParseAnyAttribute(srcNodeChild, dstNode, info);
    else
    {
      qDebug() << "Unknown TAG" << srcNodeChild.tagName();
      Q_ASSERT(false);
    }
    srcNodeChild = srcNodeChild.nextSiblingElement();
  }
}
//------------------------------------------------------------------------------
// ParseFileName
//
void WsdlFile::ParseFileName(const QString& fileName) 
{
  QFileInfo info(fileName);
  if (!info.exists() || info.suffix().toLower() != STR_WSDL)
  {
    qDebug() << "Error" << QString("%1 Does not Exist!").arg(fileName);
    return;
  }

  QFile file(fileName);
  if (!m_wsdlDomDoc.setContent(&file))
  {
    qDebug() << "Error--Unable to set Content of DOM file";
    return;
  }
  file.close();

  ParseSchemaInfo(&m_wsdlDomDoc, m_wsdlInfo);
  QDomElement docElem = m_wsdlDomDoc.documentElement();

  QDomNode portTypeNode = docElem.namedItem(SchemaTag(m_wsdlInfo.WsdlPrefix, TAG_PORT_TYPE));
  if (portTypeNode.isNull())
  {
    qDebug() << "ERROR: " << SchemaTag(m_wsdlInfo.WsdlPrefix, TAG_PORT_TYPE) << "NOT FOUND";
    return;
  }

  QDomElement opNode = portTypeNode.firstChildElement();
  while (!opNode.isNull())
  {
    if (opNode.tagName() == SchemaTag(m_wsdlInfo.WsdlPrefix, TAG_OPERATION))
      ParsePortTypeOp(opNode);
    else
    {
      qDebug() << "Unknown TAG" << opNode.tagName();
      Q_ASSERT(false);
    }
    opNode = opNode.nextSiblingElement();
  }
}
//------------------------------------------------------------------------------
// ParseNamespaceInfo
//
void WsdlFile::ParseNamespaceInfo(QDomElement& node, SchemaInfo& info)
{
  // Parse the attributes to get the namespaces
  QDomNamedNodeMap attrMap = node.attributes();
  info.XmlSchemaPrefix = "";
  for (int i = 0; i < attrMap.count(); ++i)
  {
    QDomAttr at = attrMap.item(i).toAttr();
    if (at.isNull())
      continue;

    if (at.value() == STR_SCHEMA_NS_W3_ORG_2001_XMLSCHEMA)
    {
      info.XmlSchemaPrefix = at.name().right(at.name().size() - STR_XMLNS.size() - 1);
      if (info.XmlSchemaPrefix.count()) 
      {
        if (info.XmlSchemaPrefix == STR_XMLNS) 
          info.XmlSchemaPrefix.clear();
      }
    }
    else if (at.name().contains(STR_XMLNS))
      info.PrefixNamespaceLookup.insert(at.name().split(":").last(), at.value());
    else if (at.name() == STR_TARGET_NAMESPACE)
      info.TargetNamespace = at.value();
    else if (at.name() == STR_SCHEMA_NS_XMLSOAP_ORG_WSDL)
      info.WsdlPrefix = at.value();
    else if (at.name() == STR_SCHEMA_NS_XMLSOAP_ORG_WSDL_SOAP)
      info.SoapPrefix = at.value();
  }
}
//------------------------------------------------------------------------------
// ParsePattern
//
void WsdlFile::ParsePattern(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info, bool isAttr, const QString& attrName)
{
  Q_UNUSED(info);
  //qDebug() << "ParsePattern" << srcNode.tagName() << srcNode.attribute(TAG_VALUE) << info.TargetNamespace << "DST" << dstNode.tagName();
  QString value = srcNode.attribute(TAG_VALUE);

  if (isAttr)
    WriteJsonAttrInfo(dstNode, attrName, TAG_JSON_PATTERN, value);
  else
    WriteJsonInfo(dstNode, TAG_JSON_PATTERN, value);
}
//------------------------------------------------------------------------------
// ParsePortTypeOp
//
void WsdlFile::ParsePortTypeOp(const QDomElement& srcNode)
{
  //qDebug() << "ParsePortTypeOp" << srcNode.tagName() << srcNode.attribute(TAG_NAME);
  QString name = srcNode.attribute(TAG_NAME);
  if (!m_wsdlMethods.contains(name))
  {
    WsdlMethod* m = new WsdlMethod(name);
    QDomElement child = srcNode.firstChildElement();
    while (!child.isNull())
    {
      if (child.tagName() == SchemaTag(STR_WSDL, TAG_DOCUMENTATION))
        m->Desc = child.text();
      else if (child.tagName() == SchemaTag(STR_WSDL, TAG_INPUT))
        m->Input = child.attribute(TAG_MESSAGE);
      else if (child.tagName() == SchemaTag(STR_WSDL, TAG_OUTPUT))
        m->Output = child.attribute(TAG_MESSAGE);
      else
      {
        qDebug() << "Unknown TAG" << child.tagName();
        Q_ASSERT(false);
      }
      child = child.nextSiblingElement();
    }
    // Parse for the types of based on the bindings and types defined in messages
    m->Input = ParseSoapMessageType(m->Input);
    m->Output = ParseSoapMessageType(m->Output);
    m->RequestHeader = ParseSoapHeaderInOutType(name, TAG_INPUT);
    m->ResponseHeader = ParseSoapHeaderInOutType(name, TAG_OUTPUT);
    m_wsdlMethods.insert(name, m);
  }
}
//------------------------------------------------------------------------------
// ParseRestriction
//
void WsdlFile::ParseRestriction(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info, bool isAttr, const QString& attrName)
{
  //qDebug() << "ParseRestriction" << srcNode.tagName() << srcNode.attribute(TAG_BASE) << info.TargetNamespace << "DST" << dstNode.tagName();
  QString base = srcNode.attribute(TAG_BASE);

  if (isAttr)
    WriteJsonAttrInfo(dstNode, attrName, TAG_JSON_TYPE, base);
  else
    WriteJsonInfo(dstNode, TAG_JSON_TYPE, base);

  if (base == TAG_ANY_TYPE)
    base = SchemaTag(info.XmlSchemaPrefix, TAG_STRING);

  if (IsXsdPrimitiveType(base, info))
  {
    // Primitive Type
    QDomElement srcNodeChild = srcNode.firstChildElement();
    while (!srcNodeChild.isNull())
    {
      if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ENUMERATION))
        ParseEnumeration(srcNodeChild, dstNode, info, isAttr, attrName);
      else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_PATTERN))
        ParsePattern(srcNodeChild, dstNode, info, isAttr, attrName);
      else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ATTRIBUTE))
        ParseAttribute(srcNodeChild, dstNode, info);
      srcNodeChild = srcNodeChild.nextSiblingElement();
    }
  }
  else
  {
    qDebug() << "TODO ParseRestriction for non primitive type";
    Q_ASSERT(false);
  }
}
//------------------------------------------------------------------------------
// ParseSchemaForElement
//
QDomElement WsdlFile::ParseSchemaForElement(const QDomElement& schemaNode, const QString& elementName, const SchemaInfo& info)
{
  Q_UNUSED(info);
  QDomElement elementNode = schemaNode.firstChildElement();
  while (!elementNode.isNull())
  {
    //qDebug() << "Element:" << elementNode.tagName() << elementNode.attribute(TAG_NAME);
    if (elementNode.attribute(TAG_NAME) == elementName)
      return elementNode;
    elementNode = elementNode.nextSiblingElement();
  }
  return QDomElement();
}
//------------------------------------------------------------------------------
// ParseSchemaInfo
//
void WsdlFile::ParseSchemaInfo(const QDomElement& schema, SchemaInfo& info)
{
  //qDebug() << "ParseSchemaInfo" << schema.tagName();
  QString ns = schema.attribute(TAG_TARGET_NAMESPACE);
  QString loc("");
  if (info.TargetNamespace.isEmpty())
    info.TargetNamespace = ns;

  QDomNodeList list = schema.elementsByTagName(SchemaTag(info.XmlSchemaPrefix, TAG_IMPORT));
  for (int i = 0; i < list.count(); ++i)
  {
    QDomElement importNode = list.at(i).toElement();
    Q_ASSERT(!importNode.isNull());
    if (!importNode.isNull())
    {
      ns = importNode.attribute(TAG_NAMESPACE);
      loc = importNode.attribute(TAG_SCHEMA_LOCATION);
    }
    if (!ns.isEmpty() && !loc.isEmpty())
      info.NamespaceFileNameLookup.insert(ns, loc);
  }

  list = schema.elementsByTagName(SchemaTag(info.XmlSchemaPrefix, TAG_INCLUDE));
  for (int i = 0; i < list.count(); ++i)
  {
    QDomElement includeNode = list.at(i).toElement();
    Q_ASSERT(!includeNode.isNull());
    if (!includeNode.isNull())
    {
      ns = schema.attribute(TAG_TARGET_NAMESPACE);
      loc = includeNode.attribute(TAG_SCHEMA_LOCATION);
    }
    if (!ns.isEmpty() && !loc.isEmpty())
      info.NamespaceFileNameLookup.insert(ns, loc);
  }

  // Set the TargetNamespace Prefix if it exists
  foreach (const QString key, info.PrefixNamespaceLookup.keys())
  {
    if (info.PrefixNamespaceLookup.value(key, "") == info.TargetNamespace)
    {
      info.TargetNamespacePrefix = key;
      break;
    }
  }
}
//------------------------------------------------------------------------------
// ParseSchemaInfo
//
void WsdlFile::ParseSchemaInfo(QDomDocument* doc, SchemaInfo& info)
{
  QDomElement root = doc->documentElement();
  Q_ASSERT(!root.isNull());
  if (root.isNull())
    return;

  ParseNamespaceInfo(root, info);

  // Need to clear the info's NamespaceFileNameLookup because info is most likely copied and MIGHT have residual bad paths
  info.NamespaceFileNameLookup.clear();
  if (root.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_SCHEMA))
    ParseSchemaInfo(root, info);
  else
  {
    // This must be a wsdl so get the schema Nodes
    QDomElement typesNode = root.firstChildElement();
    Q_ASSERT(!typesNode.isNull() && typesNode.tagName() == SchemaTag(info.WsdlPrefix, TAG_TYPES));
    if (!typesNode.isNull())
    {
      QDomElement schemaNode = typesNode.firstChildElement();
      while (!schemaNode.isNull())
      {
        ParseSchemaInfo(schemaNode, info);
        schemaNode = schemaNode.nextSiblingElement();
      }
    }
  }
}
//------------------------------------------------------------------------------
// ParseSequence
//
void WsdlFile::ParseSequence(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info)
{
  //qDebug() << "ParseSequence" << srcNode.tagName() << srcNode.attribute(TAG_NAME) << info.TargetNamespace << "DST" << dstNode.tagName();
  QDomElement srcNodeChild = srcNode.firstChildElement();
  while (!srcNodeChild.isNull())
  {
    if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ELEMENT))
      ParseElement(srcNodeChild, dstNode, info);
    else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_CHOICE))
      ParseChoice(srcNodeChild, dstNode, info);
    else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ANY))
      ParseAny(srcNodeChild, dstNode, info);
    else
    {
      Q_ASSERT(false);
      qDebug() << "Unknown TAG" << srcNodeChild.tagName();
    }
    srcNodeChild = srcNodeChild.nextSiblingElement();
  }
}
//------------------------------------------------------------------------------
// ParseSimpleContent
//
void WsdlFile::ParseSimpleContent(const QDomElement& srcNode, QDomElement& dstNode, const SchemaInfo& info)
{
  //qDebug() << "ParseSimpleContent" << srcNode.tagName() << srcNode.attribute(TAG_NAME) << info.TargetNamespace << "DST" << dstNode.tagName();
  QDomElement srcNodeChild = srcNode.firstChildElement();
  while (!srcNodeChild.isNull())
  {
    if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_EXTENSION))
      ParseExtension(srcNodeChild, dstNode, info);
    //else if (srcNodeChild.tagName() == SchemaTag(info.XmlSchemaPrefix, TAG_ELEMENT))
    //  ParseElement(srcNodeChild, dstNode, info);
    else
    {
      Q_ASSERT(false);
      qDebug() << "Unknown TAG" << srcNodeChild.tagName();
    }
    srcNodeChild = srcNodeChild.nextSiblingElement();
  }
}
//------------------------------------------------------------------------------
// ParseSoapHeaderInOutType
//
QString WsdlFile::ParseSoapHeaderInOutType(const QString& method, const QString& inputOutputTag)
{
  QString element;
  QString message;

  QDomElement docElem = m_wsdlDomDoc.documentElement();

  // Read the Binding for this method to get the message
  QDomElement bindingNode = docElem.namedItem(SchemaTag(m_wsdlInfo.WsdlPrefix, TAG_BINDING)).toElement();
  if (!bindingNode.isNull())
  {
    QDomNodeList list = bindingNode.elementsByTagName(SchemaTag(m_wsdlInfo.WsdlPrefix, TAG_OPERATION));
    for (int i = 0; i < list.count(); ++i)
    {
      QDomElement op = list.at(i).toElement();
      if (!op.isNull())
      {
        if (op.attribute(TAG_NAME) == method)
        {
          QDomElement inOut = op.firstChildElement(SchemaTag(m_wsdlInfo.WsdlPrefix, inputOutputTag));
          if (!inOut.isNull())
          {
            QDomElement header = inOut.firstChildElement(SchemaTag(m_wsdlInfo.SoapPrefix, TAG_HEADER));
            if (!header.isNull())
            {
              message = header.attribute(TAG_MESSAGE);
              break;
            }
          }
        }
      }
    }
  }
  // Found the mesasge name...so now find the message type
  if (message.contains(":"))
    message = message.split(":").last();
  if (!message.isEmpty())
  {
    QDomNodeList list = docElem.elementsByTagName(SchemaTag(m_wsdlInfo.WsdlPrefix, TAG_MESSAGE));
    for (int i = 0; i < list.count(); ++i)
    {
      QDomElement messageNode = list.at(i).toElement();
      if (!messageNode.isNull())
      {
        if (messageNode.attribute(TAG_NAME) == message)
        {
          element = messageNode.firstChildElement(SchemaTag(m_wsdlInfo.WsdlPrefix, TAG_PART)).attribute(TAG_ELEMENT);
          break; // found it so get out
        }
      }
    }
  }
  return element;
}
//------------------------------------------------------------------------------
// ParseSoapMessageType
//
QString WsdlFile::ParseSoapMessageType(const QString& message)
{
  // Find the Message type based on the Message Name
  QString type;
  QString msg = message;
  QDomElement docElem = m_wsdlDomDoc.documentElement();
  if (msg.contains(":"))
    msg = msg.split(":").last();
  if (!msg.isEmpty())
  {
    QDomNodeList list = docElem.elementsByTagName(SchemaTag(m_wsdlInfo.WsdlPrefix, TAG_MESSAGE));
    for (int i = 0; i < list.count(); ++i)
    {
      QDomElement messageNode = list.at(i).toElement();
      if (!messageNode.isNull())
      {
        if (messageNode.attribute(TAG_NAME) == msg)
        {
          type = messageNode.firstChildElement(SchemaTag(m_wsdlInfo.WsdlPrefix, TAG_PART)).attribute(TAG_ELEMENT);
          break; // found it so get out
        }
      }
    }
  }
  return type;
}
//------------------------------------------------------------------------------
// SetDomElementId
//
void WsdlFile::SetDomElementId(QDomElement& node)
{
  node.setAttribute(TAG_JSON_ID, ID_COUNTER++);
}