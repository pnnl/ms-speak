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
// Summary: WsdlMethodView.cpp
//-------------------------------------------------------------------------------

#include <QDebug>
#include <QFileDialog>
#include <QJsonDocument>
#include <QJsonObject>
#include <QSettings>
#include <QMessageBox>
#include <QComboBox>

#include "Settings.h"
#include "TimelineEvent.h"
#include "WsdlFile.h"
#include "WsdlMethodView.h"

const int ID_ROLE = Qt::UserRole + 2;
const int IS_VALUE_ROLE = Qt::UserRole + 3;
const int ATTR_NAME_ROLE = Qt::UserRole + 4;

//------------------------------------------------------------------------------
// WsdlMethodView
//
WsdlMethodView::WsdlMethodView(QWidget* parent)
	: QWidget(parent),
	  m_timelineEvent(Q_NULLPTR)
{
	ui.setupUi(this);
	ui.TreeHeader->SetTitle("Editor", 10);
	ui.XmlHeader->SetTitle("Xml", 10);
	ui.TreeView->setModel(&m_model);

	// Don't show xml by default
	ui.XmlHeader->hide();
	ui.XmlView->hide();

	connect(ui.TreeHeader, SIGNAL(InfoToggled()), this, SLOT(OnInfoToggled()));
	connect(ui.TreeHeader, SIGNAL(SaveClicked()), this, SLOT(OnSaveClicked()));
	connect(ui.TreeHeader, SIGNAL(EnableClicked(bool)), this, SLOT(OnEnableClicked(bool)));
	connect(ui.TreeHeader, SIGNAL(RestoreClicked()), this, SLOT(OnRestoreClicked()));
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
// Init - called from WsdlMethodTemplateEditor::OnInit
// WsdlView.cpp needed, but not included in .pri file...
//
void WsdlMethodView::Init(QDomDocument doc)
{
	//m_host = host;
	//m_method = method;
	m_doc = doc;
	CreateTreeView(doc);
	XmlUpdate();
}
//------------------------------------------------------------------------------
// Init - called on TimelineEventEditor dialog init from HostMethodListWidget::OnListViewDoubleClicked
//
void WsdlMethodView::Init(TimelineEvent* timelineEvent, bool bIsRequest/*=true*/)
{
	m_timelineEvent = timelineEvent;
	m_isRequest = bIsRequest;
	IsEnabled(m_isRequest); // OnEnableClicked(  );// init Requests as enabled, Responses not.
	m_doc = m_timelineEvent->Doc();
	CreateTreeView(m_doc);
	XmlUpdate();
}
//------------------------------------------------------------------------------
// XmlUpdate
//
void WsdlMethodView::XmlUpdate()
{
	if (!m_timelineEvent)
		return;
	ui.XmlHeader->show();
	ui.XmlView->show();
	ui.XmlView->clear();
	ui.XmlView->setPlainText(WsdlFile::XmlSoap(*m_timelineEvent, 2));
}
//------------------------------------------------------------------------------
// CreateTreeView - called on dbl-click of function method
//
void WsdlMethodView::CreateTreeView(const QDomDocument& doc)
{
	//qDebug() << "InfoBtn IsChecked:" << DoShowInfo();

	m_model.clear();
	ui.XmlView->clear();
	QApplication::processEvents();
	m_model.setHorizontalHeaderLabels(QStringList() << "Name" << "Value");

	QDomElement root = doc.documentElement();
	QStandardItem* rootItem = new QStandardItem(root.tagName());
	int row = 0;
	QDomElement node = root.firstChildElement();
	//qDebug() << node.tagName(); // i.e., "request:MultiSpeakRequestMsgHeader"
	while (!node.isNull())
	{
		QString name = node.tagName();
		name = name.right(name.length() - name.indexOf(":")-1);
		QStandardItem* item = new QStandardItem(name);
		rootItem->setChild(row++, item);
		StuffItem(node, item);
		node = node.nextSiblingElement();
	}
	m_model.appendRow(rootItem);

	// Expand what seems appropriate
	if( rootItem )
		ExpandItem(rootItem);

	ui.TreeView->resizeColumnToContents(0);

	SetItemsEnableState();
}
//------------------------------------------------------------------------------
// EnableItem
//
void WsdlMethodView::SetEnableState( QStandardItemModel* model, QStandardItem* item, bool bEnable )
{
	item->setEnabled(bEnable);

	if( bEnable )
		if (item->data(Qt::DisplayRole).toString() == TAG_JSON_ATTR || item->data(Qt::DisplayRole).toString() == TAG_JSON_INFO || item->data(Qt::DisplayRole).toString() == TAG_JSON_NS)
			ui.TreeView->collapse(item->index());
		else
			ui.TreeView->expand(item->index());
	else
		ui.TreeView->collapse(item->index());

	int row = 0;
	while( QStandardItem* child = item->child(row) )
	{
		QModelIndex sibidx = model->sibling(row++, 1, item->index());
		if( sibidx.isValid() )
		{
			QStandardItem *sib = model->itemFromIndex(sibidx);
			if (sib->data(IS_VALUE_ROLE).toBool())
			{
				QVariant name = child->data();
				sib->setEditable(bEnable);
				if( bEnable )
					sib->setData(QColor(Qt::lightGray), Qt::BackgroundRole);
				else
					sib->setData(QColor(Qt::white), Qt::BackgroundRole);
			}
		}
		SetEnableState(model,child,bEnable);
	}
}
//------------------------------------------------------------------------------
// SetItemsEnable
//
void WsdlMethodView::SetItemsEnableState()
{
	//QModelIndex idx = m_model.index(0, 0, QModelIndex());
	QStandardItem* rootItem = m_model.invisibleRootItem();// = m_model.itemFromIndex( idx );
	if (rootItem) // ""
		;//qDebug() << rootItem->text(); // i.e., 'Request'
	else{
		qDebug() << "Failed to Set Items Enable State";
		return;
	}
	SetEnableState(&m_model, rootItem->child(0), IsEnabled());
}
//------------------------------------------------------------------------------
// ExpandItem
//
void WsdlMethodView::ExpandItem(QStandardItem* item)
{
	if (item->data(Qt::DisplayRole).toString() == TAG_JSON_ATTR || item->data(Qt::DisplayRole).toString() == TAG_JSON_INFO || item->data(Qt::DisplayRole).toString() == TAG_JSON_NS)
		ui.TreeView->collapse(item->index());
	else
		ui.TreeView->expand(item->index());

	int row = 0;
	while (QStandardItem* child = item->child(row++)){
		ExpandItem(child);
	}
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
	QString name = node.tagName();
	item->setData(name.right(name.length() - name.indexOf(":") - 1), Qt::DisplayRole); // strip off the ns prefix
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

	// __NS__
	infoAttr = node.attributeNode(TAG_JSON_NS);
	QJsonDocument jsonNsInfoDoc = WsdlFile::JsonDoc(infoAttr.value().toLatin1());
	if (!infoAttr.isNull() && DoShowInfo())
		StuffJsonInfo(item, row++, infoAttr.name(), jsonNsInfoDoc);

	// Attributes
	QDomNamedNodeMap attrNodes = node.attributes();
	if (attrNodes.count())
	{
		QStandardItem* attrContainerItem = Q_NULLPTR;
		int attrRow = 0;

		for (int i = 0; i < attrNodes.count(); ++i)
		{
			QDomAttr attr = attrNodes.item(i).toAttr();

			if (attr.name() == TAG_JSON_INFO || attr.name() == TAG_JSON_ATTR || attr.name() == TAG_JSON_ID || attr.name() == TAG_JSON_NS)
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
// OnInfoToggled
//
void WsdlMethodView::OnInfoToggled()
{
	CreateTreeView(m_doc);
	XmlUpdate();
}
//------------------------------------------------------------------------------
// OnSaveClicked
//
void WsdlMethodView::OnSaveClicked()
{
	ExportXmlOrSoap();
}
//------------------------------------------------------------------------------
// OnXmlExport
//
void WsdlMethodView::OnXmlExport()
{
	ExportXmlOrSoap( true );
}

void WsdlMethodView::ExportXmlOrSoap( bool bExport/*=false*/ )
{
	QByteArray bytes;
	QString seedFile;
	QString saveKey;
	QFileDialog *fileDialog = new QFileDialog;
	QString suffix;
	QString fltr;
	QString prmpt;

	/*
	 * setDefaultSuffix only seems supported on WinDoze
	fileDialog->setAcceptMode(QFileDialog::AcceptMode::AcceptSave);
	fileDialog->setFileMode(QFileDialog::AnyFile);
	QComboBox* cb = fileDialog->findChild<QComboBox*>("fileTypeCombo");
	if (cb)
		cb->setEditable(true);
	*/

	// Load file
	QString fileName;
	if( bExport ){
		if( m_isRequest )
			saveKey = SK_EXPORT_XMLREQ_FILE;
		else
			saveKey = SK_EXPORT_XMLRES_FILE;
		seedFile = QSettings().value(saveKey, QVariant()).toString();
		fltr = "XML (*.xml);; All (*.*)";
		prmpt = "Select XML File";
		suffix = "xml";
	}
	else{
		prmpt = "Select Editor Settings File";
		if( m_isRequest ){
			saveKey = SK_EXPORT_EDTREQ_FILE;
			fltr = "REQ (*req);; All (*.*)";
			suffix = "req";
		}
		else{
			saveKey = SK_EXPORT_EDTRES_FILE;
			fltr = "RES (*res);; All (*.*)";
			suffix = "res";
		}
	}

	seedFile = QSettings().value(saveKey, QVariant()).toString();
	fileDialog->setDefaultSuffix(suffix);
	fileName = fileDialog->getSaveFileName(this, prmpt, seedFile, fltr);
	if (fileName.isEmpty())
		return;

	if( !fileName.contains("."))
		fileName += "." + suffix;

	QSettings().setValue(saveKey, fileName);

	QFile file(fileName);

	if (!file.open(QIODevice::WriteOnly))
	{
		qDebug() << file.error() << file.errorString();
		return;
	}
	if( bExport )
		bytes = WsdlFile::XmlSoap(*m_timelineEvent, 2);
	else
		bytes = WsdlFile::Xml(m_doc, 2, true);

	file.write(bytes);
	if (file.error() != QFileDevice::NoError)
		qDebug() << "ERROR:" << file.error() << file.errorString();
	file.close();
}
//------------------------------------------------------------------------------
// OnEnableClicked
//
void WsdlMethodView::OnEnableClicked(bool checked)
{
	Q_UNUSED(checked)
	/*
	QString dbgStr;
	if( m_isRequest )
		dbgStr = "Request Packet";
	else
		dbgStr = "Response Packet";
	if( IsEnabled() )
		dbgStr += " Is Enabled.";
	else
		dbgStr += " Is NOT Enabled.";
	qDebug() << dbgStr;*/
	SetItemsEnableState();
}
//------------------------------------------------------------------------------
// OnRestoreClicked
//
void WsdlMethodView::OnRestoreClicked()
{
	QString saveKey;
	QString fltr;
	if( m_isRequest ){
		saveKey = SK_IMPORT_EDTREQ_FILE;
		fltr = "REQ (*req);; All (*.*)";
	}
	else{
		saveKey = SK_IMPORT_EDTRES_FILE;
		fltr = "RES (*res);; All (*.*)";
	}
	QString seedFile = QSettings().value(saveKey, QVariant()).toString();
	// Load file
	QString fileName = QFileDialog::getOpenFileName(this, "Select Editor Settings File", seedFile, fltr);
	if (fileName.isEmpty())
		return;

	QSettings().setValue(saveKey, fileName);

	QFile file(fileName);
	if (!file.open(QIODevice::ReadOnly | QIODevice::Text))	{
		qDebug() << file.error() << file.errorString();
		return;
	}
	QDomDocument domDocument;
	QString errorStr;
	int errorLine;
	int errorColumn;
	if (!domDocument.setContent(&file, false, &errorStr, &errorLine, &errorColumn))
	{
		file.close();
		QString errorStr2;
		QTextStream out(&errorStr2);
		out << "Failed to set DomDocument Content from file: " << errorStr << ", Line " << errorLine << ", Column " << errorColumn;
		qDebug() << errorStr2;
		QMessageBox messageBox;
		messageBox.critical(Q_NULLPTR, fileName, errorStr2);
		return;
	}
	file.close();

	QHash<QString, QString> hashimoto;
	QHash<QString,QHash<QString, QString>> attribs;
	QHash<QString, QString>::const_iterator hitr;
	QDomElement root = domDocument.documentElement(); // now e contains "Node" - it's a document element - means root element
    QString startTag = root.tagName();
	for(QDomNode n = root; !n.isNull(); n = n.nextSibling())
		TraverseXmlNode( n, hashimoto, attribs );

	root = m_doc.documentElement();
	hitr = hashimoto.constBegin();
	while( hitr != hashimoto.constEnd() )
	{
		QString tag = hitr.key();
		// Find elements with tag names
		QDomNodeList nodes = root.elementsByTagName(tag);
		int tagCount = nodes.length();
		if( tagCount == 0 )
		{
			qDebug() << "Error" << QString("Tag '%1' Does not Exist!").arg(tag);
			QMessageBox messageBox;
			messageBox.critical(Q_NULLPTR,"Error",QString("Tag '%1' Does not Exist!").arg(tag));
			return;
		}
		if( tagCount != 1 )
		{
			qDebug() << "Error" << QString("Tag '%1' Exist More than Once!").arg(tag);
			QMessageBox messageBox;
			messageBox.critical(Q_NULLPTR,"Error",QString("Tag '%1' Exist More than Once!").arg(tag));
			return;
		}
		// Iterate through all we found (should only be 1)
		for(int i=0; i<nodes.count(); i++)
		{
			QDomNode node = nodes.item(i);
			if(node.nodeType() == QDomNode::ElementNode)// Check the node is a DOM element
			{
				QDomElement element = node.toElement();// Access the DOM element
				QHash<QString,QHash<QString, QString>>::const_iterator aitr = attribs.find(tag);
				if( aitr != attribs.end() )
				{
					QHash<QString, QString>::const_iterator attrmoto =  aitr.value().constBegin();
					while( attrmoto != aitr.value().constEnd() )
					{
						if( element.hasAttribute(attrmoto.key()) )
						{
							//qDebug() << "   Has Attribute: " << attrmoto.key() << "with value: " << attrmoto.value();
							element.setAttribute(attrmoto.key(),attrmoto.value() );
						}
						else
						{
							qDebug() << "Error" << QString("Tag '%1' Does not Have Attribute '%2'!").arg(tag,attrmoto.key());
							QMessageBox messageBox;
							messageBox.critical(Q_NULLPTR,"Error",QString("Tag '%1' Does not Have Attribute '%2'!").arg(tag,attrmoto.key()));
							return;
						}
						++attrmoto;
					}
				}

				// Iterate through it's children look for DOM type text
				for(QDomNode n = element.firstChild(); !n.isNull(); n = n.nextSibling())
				{
					 QDomText t = n.toText();
					 if (!t.isNull())
					 {
						//qDebug() << "Old text was " << t.data();
						//qDebug() << "New text is " << hitr.value();
						t.setData(hitr.value());
					 }
					 /*else{
						 qDebug() << element.tagName().toLocal8Bit().constData() << " is NOT text, skipping...";
					 }*/
				}
			}
		}
		++hitr;
	}
	CreateTreeView(m_doc);
	XmlUpdate();

}
void WsdlMethodView::TraverseXmlNode(const QDomNode& node, QHash<QString, QString>& rList,
										   QHash<QString,QHash<QString, QString>>& rAttribs, QString tagname)
{
	QDomNode domNode = node.firstChild();
	QDomElement domElement;
	QDomText domText;
	static int level = 0;

	level++;
	while(!(domNode.isNull()))
	{
		if( domNode.hasAttributes() )
		{
			QString domTag =  domNode.toElement().tagName();
			//qDebug()<<"domNode tag is: " << domTag;
			QDomNamedNodeMap map = domNode.attributes();
			for( int i = 0 ; i < map.length() ; ++i )
			{
				if(!(map.item(i).isNull()))
				{
					QDomNode debug = map.item(i);
					QDomAttr attr = debug.toAttr();
					if( !attr.isNull() )
					{
						if( attr.name().startsWith( "xmlns:" ) )
							continue;
						//qDebug() << "    attribute name: " << attr.name() << ", value: " << attr.value();
						rList[domTag] = "hasAttr";
						rAttribs[domTag][attr.name()] = attr.value();
					}
				}
			}
		}
		else if(domNode.isElement())
		{
			domElement = domNode.toElement();
			//qDebug()<<"domElement tag is: " << domElement.tagName();
			if(!(domElement.isNull()))
			{
				//qDebug() << __FUNCTION__ << "isElement" << level << QString(level, ' ').toLocal8Bit().constData() << "tagName: "  << domElement.tagName().toLocal8Bit().constData();
				tagname = domElement.tagName().toLocal8Bit().constData();

			}
		}
		else if(domNode.isText())
		{
			domText = domNode.toText();
			if( !domText.isNull() )
			{
				if( tagname != Q_NULLPTR )
				{
					//qDebug() << "Tag Value is: " << domText.data() << " For Tag " << tagname;
					rList[tagname] = domText.data();
				}
				else{
					qDebug() << "Text Found With No Tag!";
				}
			}
		}
		TraverseXmlNode(domNode, rList, rAttribs, tagname);
		domNode = domNode.nextSibling();
	}

	level--;
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
							//qDebug() << foundNode.tagName() << item->data(Qt::DisplayRole).toString();
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
