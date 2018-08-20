//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlMethodView
//

#include <QDebug>
#include <QFileDialog>
#include <QJsonDocument>
#include <QJsonObject>
#include <QSettings>

#include "Settings.h"
#include "WsdlFile.h"
#include "WsdlMethodView.h"

const int ID_ROLE = Qt::UserRole + 2;
const int IS_VALUE_ROLE = Qt::UserRole + 3;
const int ATTR_NAME_ROLE = Qt::UserRole + 4;

//------------------------------------------------------------------------------
// WsdlMethodView
//
WsdlMethodView::WsdlMethodView(QWidget* parent)
  : QWidget(parent)
{
  ui.setupUi(this);
  ui.TreeHeader->SetTitle("Editor", 10);
  ui.XmlHeader->SetTitle("Xml", 10);
  ui.TreeView->setModel(&m_model);

  connect(ui.TreeHeader, SIGNAL(InfoToggled()), this, SLOT(OnInfoToggled()));
  connect(ui.TreeHeader, SIGNAL(SaveClicked()), this, SLOT(OnSaveClicked()));
  connect(ui.XmlHeader, SIGNAL(ExportClicked()), this, SLOT(OnXmlExport()));

  connect(&m_model, SIGNAL(itemChanged(QStandardItem*)), this, SLOT(OnXmlItemChanged(QStandardItem*)));
}
//------------------------------------------------------------------------------
// ~WsdlMethodView
//
WsdlMethodView::~WsdlMethodView()
{
}
//------------------------------------------------------------------------------
// Init
//
void WsdlMethodView::Init(const QString& host, const QString& method, QDomDocument doc)
{
  m_host = host;
  m_method = method;
  m_doc = doc;
  CreateTreeView(doc);
}
//------------------------------------------------------------------------------
// CreateTreeView
//
void WsdlMethodView::CreateTreeView(const QDomDocument& doc)
{
  qDebug() << "InfoBtn IsChecked:" << DoShowInfo();

  m_model.clear();
  ui.XmlView->clear();
  QApplication::processEvents();
  m_model.setHorizontalHeaderLabels(QStringList() << "Name" << "Value");

  QDomElement root = doc.documentElement();
  QStandardItem* rootItem = new QStandardItem(root.tagName());
  int row = 0;
  QDomElement node = root.firstChildElement();
  qDebug() << node.tagName();
  while (!node.isNull())
  {
    QStandardItem* item = new QStandardItem(node.tagName());
    rootItem->setChild(row++, item);
    StuffItem(node, item);
    node = node.nextSiblingElement();
  }

  m_model.appendRow(rootItem);

  // Expand what seems appropriate
  if (rootItem)
    ExpandItem(rootItem);

  ui.TreeView->resizeColumnToContents(0);
  XmlUpdate();
}
//------------------------------------------------------------------------------
// ExpandItem
//
void WsdlMethodView::ExpandItem(QStandardItem* item)
{
  if (item->data(Qt::DisplayRole).toString() == TAG_JSON_ATTR || item->data(Qt::DisplayRole).toString() == TAG_JSON_INFO)
    ui.TreeView->collapse(item->index());
  else
    ui.TreeView->expand(item->index());

  int row = 0;
  while (QStandardItem* child = item->child(row++))
    ExpandItem(child);
}
//------------------------------------------------------------------------------
// StuffItem
//
void WsdlMethodView::StuffItem(QDomElement node, QStandardItem* item)
{
   QFont boldFont = item->font();
   boldFont.setBold(true);

  QJsonDocument jsonInfoDoc = WsdlFile::JsonDoc(node.attributeNode(TAG_JSON_INFO).value().toLatin1());

  // Element
  item->setEditable(false);
  item->setData(node.tagName(), Qt::DisplayRole);
  item->setData(node.attribute(TAG_JSON_ID), ID_ROLE);

  // Set Font to Bold if min is 1 i.e. it is required
  QString min = jsonInfoDoc.object().find(TAG_JSON_MIN).value().toString();
  if (min == "1" || min.isEmpty())
    item->setFont(boldFont);
  
  if (node.hasChildNodes() && !node.isNull() && !node.text().isEmpty())
  {
    item->setCheckable(true);
    item->setCheckState(jsonInfoDoc.object().find(TAG_JSON_IS_USER_CHECKED).value().toBool() ? Qt::Checked : Qt::Unchecked);
  }

  int row = 0;

  // __ID__
  QDomAttr infoAttr = node.attributeNode(TAG_JSON_ID);
  if (!infoAttr.isNull() && DoShowInfo())
  {
    QStandardItem* jsonName = new QStandardItem(infoAttr.name());
    jsonName->setEditable(false);

    QStandardItem* jsonValue = new QStandardItem(infoAttr.value());
    jsonValue->setEditable(false);

    item->setChild(row, 0, jsonName);
    item->setChild(row++, 1, jsonValue);
  }

  // __INFO__
  infoAttr = node.attributeNode(TAG_JSON_INFO);
  if (!infoAttr.isNull() && DoShowInfo())
    StuffJsonInfo(item, row++, infoAttr.name(), jsonInfoDoc);

  // __ATTR__
  infoAttr = node.attributeNode(TAG_JSON_ATTR);
  QJsonDocument jsonInfoAttrDoc = WsdlFile::JsonDoc(infoAttr.value().toLatin1());
  if (!infoAttr.isNull() && DoShowInfo())
    StuffJsonInfo(item, row++, infoAttr.name(), jsonInfoAttrDoc);

  // Attributes
  QDomNamedNodeMap attrNodes = node.attributes();
  if (attrNodes.count())
  {
    QStandardItem* attrContainerItem = 0;
    int attrRow = 0;

    for (int i = 0; i < attrNodes.count(); ++i)
    {
      QDomAttr attr = attrNodes.item(i).toAttr();

      if (attr.name() == TAG_JSON_INFO || attr.name() == TAG_JSON_ATTR || attr.name() == TAG_JSON_ID)
        continue; // Already parsed out above so skip

      if (!attrContainerItem)
      {
        attrContainerItem = new QStandardItem(STR_ATTRIBUTES);
        QStandardItem* fillerItem = new QStandardItem("");
        fillerItem->setEditable(false);
        item->setChild(row, 0, attrContainerItem);
        item->setChild(row++, 1, fillerItem);
      }

      QStandardItem* attrNameItem = new QStandardItem(attr.name());
      attrNameItem->setEditable(false);
      attrNameItem->setCheckable(true);
      attrNameItem->setCheckState(jsonInfoAttrDoc.object().find(attr.name()).value().toObject().find(TAG_JSON_IS_USER_CHECKED).value().toBool() ? Qt::Checked : Qt::Unchecked);
      attrNameItem->setData(attr.name(), ATTR_NAME_ROLE);

      // Set Font to Bold if use is required
      QJsonValue val = jsonInfoAttrDoc.object().find(attr.name()).value().toObject().find(TAG_JSON_USE).value();
      if (!val.isNull() && val.toString() == TAG_JSON_USE_REQUIRED)
        attrNameItem->setFont(boldFont);

      QStandardItem* attrValueItem = new QStandardItem(attr.value());
      attrValueItem->setData(QColor(Qt::lightGray), Qt::BackgroundRole);
      attrValueItem->setData(attr.name(), ATTR_NAME_ROLE);
      attrValueItem->setData(true, IS_VALUE_ROLE);

      attrContainerItem->setChild(attrRow, 0, attrNameItem);
      attrContainerItem->setChild(attrRow++, 1, attrValueItem);
    }
  }

  // Children...and element value
  QDomNodeList childNodes = node.childNodes();
  for (int i = 0; i < childNodes.count(); ++i)
  {
    QDomNode childNode = childNodes.at(i);

    Q_ASSERT(!childNode.isNull());
    if (childNode.isNull()) 
      continue;

    if (childNode.isText())
    {
      QStandardItem* elementValueItem = new QStandardItem(childNode.toText().nodeValue());
      elementValueItem->setData(QColor(Qt::lightGray), Qt::BackgroundRole);
      elementValueItem->setData(node.attribute(TAG_JSON_ID), ID_ROLE);
      elementValueItem->setData(true, IS_VALUE_ROLE);
      item->parent()->setChild(item->row(), 1, elementValueItem);
    }
    else if (childNode.isElement())
    {
      QStandardItem* childItem = new QStandardItem(childNode.toElement().tagName());
      item->setChild(row++, childItem);
      StuffItem(childNode.toElement(), childItem);
    }
  }
}
//------------------------------------------------------------------------------
// StuffJson
//
void WsdlMethodView::StuffJson(QJsonObject obj, QStandardItem* item)
{
  int row = 0;
  for (QJsonObject::const_iterator it = obj.constBegin(); it != obj.constEnd(); ++it)
  {
    QStandardItem* keyItem = new QStandardItem(it.key());
    keyItem->setEditable(false);

    QJsonValue jsonVal = it.value();
    if (jsonVal.isObject())
      StuffJson(jsonVal.toObject(), keyItem);
    else
    {
      QString value;
      if (it.value().isBool())
        value  = (it.value().toBool()) ? "true" : "false";
      else if (it.value().isDouble())
        value = QString::number(it.value().toDouble());
      else 
        value = it.value().toString();

      QStandardItem* valItem = new QStandardItem(value);
      valItem->setEditable(false);
      item->setChild(row, 1, valItem);
    }
    item->setChild(row, 0, keyItem);
    row++;
  }
}
//------------------------------------------------------------------------------
// StuffJsonInfo
//
void WsdlMethodView::StuffJsonInfo(QStandardItem* parent, int row, const QString& title, const QJsonDocument& jsonDoc)
{
  QStandardItem* nameItem = new QStandardItem(title);
  nameItem->setEditable(false);

  QStandardItem* valueItem = new QStandardItem(QString(jsonDoc.toJson(QJsonDocument::Compact)));
  valueItem->setEditable(false);
  valueItem->setToolTip(jsonDoc.toJson());

  parent->setChild(row, 0, nameItem);
  parent->setChild(row, 1, valueItem);

  StuffJson(jsonDoc.object(), nameItem);
}
//------------------------------------------------------------------------------
// UpdateJsonInfo
//
void WsdlMethodView::UpdateJsonInfo(QStandardItem* parent, const QString& title, const QJsonDocument& jsonDoc)
{
  for (int row = 0; row < parent->rowCount(); ++row)
  {
    QStandardItem* child = parent->child(row);
    if (child->data(Qt::DisplayRole).toString() == title)
    {
      child->removeRows(0, child->rowCount()); // remove children so StuffJson can re-add
      StuffJson(jsonDoc.object(), child);
      QStandardItem* valueChild = parent->child(row, 1);
      valueChild->setData(jsonDoc.toJson(QJsonDocument::Compact), Qt::DisplayRole);
      valueChild->setToolTip(jsonDoc.toJson());
      break;
    }
  }
}
//------------------------------------------------------------------------------
// XmlUpdate
//
void WsdlMethodView::XmlUpdate()
{
  ui.XmlView->clear();
  ui.XmlView->setPlainText(WsdlFile::XmlSoap(m_host, m_method, m_doc, 2));
}
//------------------------------------------------------------------------------
// OnXmlExport
//
void WsdlMethodView::OnXmlExport()
{
  QString seedFile = QSettings().value(SK_EXPORT_XML_FILE, QVariant()).toString();

  // Load file
  QString fileName = QFileDialog::getSaveFileName(this, "Select File", seedFile, "XML (*.xml);; All (*.*)");

  if (fileName.isEmpty())
    return;

  QSettings().setValue(SK_EXPORT_XML_FILE, fileName);

  QFile file(fileName);

  if (!file.open(QIODevice::WriteOnly))
  {
    qDebug() << file.error() << file.errorString();
    return;
  }

  QByteArray bytes = WsdlFile::XmlSoap(m_host, m_method, m_doc, 2);
  file.write(bytes);
  if (file.error() != QFileDevice::NoError)
    qDebug() << "ERROR:" << file.error() << file.errorString();
  file.close();
}
//------------------------------------------------------------------------------
// OnXmlItemChanged
//
// This is a bit complicated because the attributes and the elements are done a bit differently
//  and not only does the checkbox need and value need to be updated but also the json info underlying in the dom
//
void WsdlMethodView::OnXmlItemChanged(QStandardItem* item)
{
  bool isChecked = (item->checkState() == Qt::Checked);
  qint64 id = item->data(ID_ROLE).toLongLong();

  if (id == 0) // If Id is 0 then this must be an attribute
  {
    // Attribute
    if (QStandardItem* attributesItem = item->parent())
    {
      if (attributesItem->data(Qt::DisplayRole).toString() == STR_ATTRIBUTES)
      {
        if (QStandardItem* elementItem = attributesItem->parent())
        {
          id = elementItem->data(ID_ROLE).toLongLong();
          QDomElement foundNode = WsdlFile::FindElementNodeById(m_doc.firstChildElement(), id);
      
          if (!foundNode.isNull())
          {
            QString attrName = item->data(ATTR_NAME_ROLE).toString();
            if (item->data(IS_VALUE_ROLE).toBool())
            {
              qDebug() << foundNode.tagName() << item->data(Qt::DisplayRole).toString();
              foundNode.setAttribute(attrName, item->data(Qt::DisplayRole).toString());
            }
            else
            {
              WsdlFile::WriteJsonAttrInfo(foundNode, attrName, TAG_JSON_IS_USER_CHECKED, QJsonValue(isChecked));
              if (DoShowInfo()) // Update the Json treeview items
              {
                // Find the __ATTR__ item
                UpdateJsonInfo(elementItem, TAG_JSON_ATTR, WsdlFile::JsonDoc(foundNode.attributeNode(TAG_JSON_ATTR).value().toLatin1()));
              }
            }
          }
        }
      }
    }
  }
  else // element
  {
    QDomElement foundNode = WsdlFile::FindElementNodeById(m_doc.firstChildElement(), id);
    // Found the Node...so update the info
    if (!foundNode.isNull())
    {
      if (item->data(IS_VALUE_ROLE).toBool())
      {
        // Set the Value if it has a QDomText child
        for (QDomNode n = foundNode.firstChild(); !n.isNull(); n = n.nextSibling())
        {
          QDomText t = n.toText();
          if (!t.isNull())
          {
            t.setData(item->data(Qt::DisplayRole).toString());
            break;
          }
        }
      }
      else
      {
        WsdlFile::WriteJsonInfo(foundNode, TAG_JSON_IS_USER_CHECKED, QJsonValue(isChecked));
      }
      if (DoShowInfo()) // Update the Json
      {
        // Find the __INFO__ item
        UpdateJsonInfo(item, TAG_JSON_INFO, WsdlFile::JsonDoc(foundNode.attributeNode(TAG_JSON_INFO).value().toLatin1()));
      }
    }
  }
  XmlUpdate();
}