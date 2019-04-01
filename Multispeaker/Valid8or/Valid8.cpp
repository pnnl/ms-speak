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
//		2018 - Created By: Carl Miller <carl.miller@pnnl.gov>
//-------------------------------------------------------------------------------
//
// Summary: Valid8.cpp
//-------------------------------------------------------------------------------

#include <QFileDialog>
#include <QCloseEvent>
#include <QMessageBox>

#include <cassert>
#include <iostream>

#include "Valid8.h"
#include "Process.h"
#include "Settings.h"
#include "QSL.h"

#ifdef _MS_ // MultiSpeaker, not MultiSpeakerServer ?
//#include "MultiSpeaker.h"
#include "TimelineEventEditor.h"
#endif

//------------------------------------------------------------------------------
// Valid8or
/*  (The ? sign declares that the element can occur zero or one time inside the import element)
		Note: If a URI has spaces, replace them with %20
			adding all XSDs as resources, use the following line:
				<xsd:include schemaLocation="qrc:///xsd/commondefinitions.xsd"/>
				Where "xsd" is a virtual ressource path, not a physical path. This means the path
				is specified the following way:
					<qresource prefix="/xsd/">
					   <file alias="commondefinitions.xsd">../framework/data/xml/commondefinitions.xsd</file>
					</qresource>
Placing the targetNamespace attribute at the top of your XSD schema means that all entities defined in it are part of this namespace.

Elements that do not have text nodes, nor other elements as children, can be expressed as empty elements.
	The syntax for empty elements is slightly different:
	  <elementName />

xmlns:tns
	This name space should be set to the same URI as the targetNameSpace attribute.
*/
Valid8or::Valid8or(QString ep, QString f, QWidget* parent)
		: QDialog(parent),
		m_SchemaRoot(QString::null),
		m_JCP(QString::null),
	    m_EndPoint(ep),
	    m_XmlFilename(f)
{
	if (!initialize(parent)) {
		QTimer::singleShot(0, this, &Valid8or::close);
		return;
	}
}
//----------------------------------------------------------------------------------------------------------------------------------
Valid8or::Valid8or(const QByteArray& msg, QWidget* parent)
		: QDialog(parent),
		m_SchemaRoot(QString::null),
		m_JCP(QString::null),
		m_EndPoint("CD_Server"),
		m_XmlFilename(QString::null)
{

	//QTemporaryFile file;
	if( !m_file.open() )
	{
		qDebug() << m_file.error() << m_file.errorString();
		return;
	}
	m_file.write(msg);
	if (m_file.error() != QFileDevice::NoError)
		qDebug() << "ERROR:" << m_file.error() << m_file.errorString();
	m_file.close();

	m_XmlFilename = m_file.fileName();
	m_byteArray = true;
	if (!initialize(parent)) {
		QTimer::singleShot(0, this, &Valid8or::close);
		return;
	}
}
//----------------------------------------------------------------------------------------------------------------------------------
bool Valid8or::initialize(QWidget* parent) {
	// Set up UI and restore UI state and geometry
	ui.setupUi(this);
	QSettings s;
	const QByteArray windowGeometry(s.value(QSL("WindowGeometry")).toByteArray());
	if (windowGeometry.isEmpty()) {
		//showMaximized();
		int nWidth = 300;
		int nHeight = 400;
		if (parent != Q_NULLPTR){
	#ifdef _MS_
			//MultiSpeaker *theApp = MultiSpeaker::theApp();
			//QRect rect = theApp->rect();
			TimelineEventEditor *theEditor = TimelineEventEditor::theEditor();
			QRect rect = theEditor->rect();
	#else
			QRect rect = parent->rect();
	#endif
			setGeometry( rect );
			/*
			QPoint parentPos = parent->mapToGlobal(parent->pos());
			nWidth = parent->width();
			nHeight = (3*parent->height()) / 4;
			setGeometry(parentPos.x(),
						parentPos.y() + parent->height()/2 - nHeight/2,
						nWidth, nHeight);
			//setGeometry(parentPos.x() + parent->width()/2 - nWidth/2,
			//			parentPos.y() + parent->height()/2 - nHeight/2,
			//			nWidth, nHeight);
			*/
		}
		else
			resize(nWidth, nHeight);
	} else {
		restoreGeometry(windowGeometry);
	}

	setSizeGripEnabled(true);

	ui.schemaSelection->setText(tr("No Schema Selected"));
	ui.instanceSelection->setText(tr("No XML Selected"));
	ui.validationStatus->setAlignment(Qt::AlignCenter | Qt::AlignVCenter);

	ui.resetXsd->setCheckState(Qt::Unchecked);
	ui.resetJcp->setCheckState(Qt::Unchecked);
	ui.resetXml->setCheckState(Qt::Unchecked);

	ui.buttonBox->button(QDialogButtonBox::Ok)->setText("Close");
	ui.buttonBox->button(QDialogButtonBox::Cancel)->hide();

	connect(ui.validateButton, SIGNAL(clicked()), SLOT(validate()));
	connect(ui.instanceEdit, SIGNAL(textChanged()), SLOT(textChanged()));
	connect(ui.buttonBox, SIGNAL(accepted()), this, SLOT(OnAccept()));
	connect(ui.buttonBox, SIGNAL(rejected()), this, SLOT(reject()));
	connect(ui.resetXsd, SIGNAL(clicked()), SLOT(resetXsd()));
	connect(ui.resetJcp, SIGNAL(clicked()), SLOT(resetJcp()));
	connect(ui.resetXml, SIGNAL(clicked()), SLOT(resetXml()));
	connect(ui.progressWidget, &ProgressWidget::valid8Done, this, &Valid8or::valid8Done);

	selectSchema();
	selectJcp();
	loadXml(m_XmlFilename);
	// Finish laying out widgets after the window is shown so the sizes are correct
	QTimer::singleShot(0, this, &Valid8or::initializeWidgets);
	m_initialized = true;
	return true;
}
//----------------------------------------------------------------------------------------------------------------------------------
void Valid8or::initializeWidgets() {
	/*
	create splitter containing items in Qt Designer :
		create an HLayout for each reset line on top half
		create a VLayout with them and the ProgressBox below
		do the same for bottom half
		select both top and bottom halves (but not button box) and
		right click,  Lay Out Vertically in Splitter.
		Then make sure to top most QWidget has a VLayout so everything fills the form.
	*/

	QSettings s;
	// size the top and bottom halves of the window
    /*QList<int>Sizes = ui.splitter->sizes();
    int top = Sizes[0];
    int bot = Sizes[1];
    Sizes[0] = top + bot/2;
    Sizes[1] = bot/2;
    ui.splitter->setSizes( Sizes );*/
	const QByteArray state(s.value(QSL("MainSplitterState")).toByteArray());
	if (state.isEmpty()) {
		const int parentWidth = parentWidget()->width();
		ui.splitter->setSizes({ static_cast<int>(parentWidth * 0.40), static_cast<int>(parentWidth * 0.60) });
	} else {
		ui.splitter->restoreState(state);
	}
	if( m_byteArray )
		QTimer::singleShot(0, this, &Valid8or::validate);
}
//------------------------------------------------------------------------------
// OnAccept
void Valid8or::OnAccept()
{
	//accept();
	QWidget::close();
}
void Valid8or::selectSchema()
{
	QString defDir = qApp->applicationDirPath();
	//qDebug() << "App path : " << defDir + "/Wsdls";
	qDebug() << "App path : " << defDir + "/EndPoints"; // 18.12.17
	QString xsdDir = QSettings().value(SK_XSD_FILE, QVariant()).toString();
	if(xsdDir.isEmpty() ){
		QFileDialog dialog;

        m_SchemaRoot = QFileDialog::getExistingDirectory(this, tr("Select Schema XSD Directory"),
                                                        defDir, QFileDialog::ShowDirsOnly );// | QFileDialog::DontResolveSymlinks
        if( !m_SchemaRoot.isEmpty() )
        {
			qDebug() << dialog.selectedFiles();
			QSettings().setValue(SK_XSD_FILE, m_SchemaRoot);
		}
		else {
			qDebug() << "Cancelled.";
		}
	}
	else
		m_SchemaRoot = xsdDir;

	if (m_SchemaRoot.isEmpty()){
		ui.schemaSelection->setText(tr("No Schema Folder Selected"));
		return;
	}
	ui.schemaSelection->setText("Using Schema Folder " + m_SchemaRoot);

	textChanged();

}
void Valid8or::selectJcp()
{
	QString defDir = qApp->applicationDirPath();
	QString jcpDir = QSettings().value(SK_JCP_FILE, QVariant()).toString();
	if (jcpDir.isEmpty()) {
		QFileDialog dialog;

		m_JCP = QFileDialog::getExistingDirectory(this, tr("Select Java Class Path Directory"),
			defDir, QFileDialog::ShowDirsOnly);
		if (!m_JCP.isEmpty())
		{
			qDebug() << dialog.selectedFiles();
			QSettings().setValue(SK_JCP_FILE, m_JCP);
		}
		else {
			qDebug() << "Cancelled.";
		}
	}
	else
		m_JCP = jcpDir;

	if (m_JCP.isEmpty()) {
		ui.javaCP->setText(tr("No Class Path Selected"));
		return;
	}
	ui.javaCP->setText("Using Class Path " + m_JCP);

}
QString Valid8or::selectXml()
{
	QString fileName = QSettings().value(SK_XML_FILE, QVariant()).toString();
	if(fileName.isEmpty() ){
		fileName = QFileDialog::getOpenFileName(this, "Select XML File", "", "XML (*xml);; All (*.*)");
		QSettings().setValue(SK_XML_FILE, fileName);
	}
	if (fileName.isEmpty()){
		ui.instanceSelection->setText(tr("No XML File Selected"));
	}
	return fileName;
}
/* notes on resource files:
 * The resource files listed in the .qrc file are files that are part of the application's source tree.
 * The specified paths are relative to the directory containing the .qrc file. Note that the listed
 * resource files must be located in the same directory as the .qrc file, or one of its subdirectories.
 *
 * reset;grep -rio --include='*.xsd' --include='*.xml' -e 'targetNamespace="[^"]*"'
 */
void Valid8or::loadXml(QString fileName)
{

	QFile instanceFile(fileName);
    if (!instanceFile.open(QIODevice::ReadOnly)) {
        qWarning() << "Cannot open" << QDir::toNativeSeparators(fileName)
            << ':' << instanceFile.errorString();
		ui.schemaSelection->setText(instanceFile.errorString());
        return;
    }
	QFileInfo XSDinfo(fileName);
	ui.instanceSelection->setText(XSDinfo.fileName());
    const QString instanceText(QString::fromUtf8(instanceFile.readAll()));
    ui.instanceEdit->setPlainText(instanceText);

	if( m_byteArray ){
		ui.validateButton->hide();
		ui.instanceLabel->hide();
		ui.instanceSelection->hide();
		ui.resetXml->hide();
	}
	else
		ui.validateButton->setEnabled(true);
	m_XmlFilename = fileName;
}

void Valid8or::validate()
{
	//ui.validateButton->setEnabled(false);
	ui.validationStatus->setText("Validating...");
	ui.progressWidget->valid8Xml(m_SchemaRoot, m_JCP, m_EndPoint, m_XmlFilename);
}
//----------------------------------------------------------------------------------------------------------------------------------
void Valid8or::valid8Done( QString msg ) {
	ui.validationStatus->setText(msg);
	//ui.validateButton->setEnabled(true);
	//ui.validateButton->setEnabled(false);
}
void Valid8or::textChanged()
{
	ui.instanceEdit->setExtraSelections(QList<QTextEdit::ExtraSelection>());
}

void Valid8or::resetXsd()
{
	QSettings().setValue(SK_XSD_FILE, "");
	selectSchema();
}
void Valid8or::resetJcp()
{
	QSettings().setValue(SK_JCP_FILE, "");
	selectJcp();
}

void Valid8or::resetXml()
{
	QSettings().setValue(SK_XML_FILE, "");
	QString xmlFile = selectXml();
	if( !xmlFile.isEmpty() ){
		loadXml(xmlFile);
	}
}

//----------------------------------------------------------------------------------------------------------------------------------
void Valid8or::closeEvent(QCloseEvent *event) {
	bool accept = false;
	if (!m_initialized) { // called from constructor?
		accept = true;
	} else if (ui.progressWidget->running()) {
		accept = false;
	} else {
		accept = true;
	}
	if (accept) {
		QSettings s;
		//s.clear(); this will delete everything
		s.setValue(QSL("WindowGeometry"), saveGeometry());
		s.setValue(QSL("MainSplitterState"), ui.splitter->saveState());
		event->accept();
	} else {
		event->ignore();
	}
}












