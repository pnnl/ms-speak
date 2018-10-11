#include <QFileDialog>
#include <QCloseEvent>
#include <QMessageBox>

#include <cassert>
#include <iostream>

#include "Valid8.h"
#include "Process.h"
#include "QSL.h"

#ifdef _MS_ // MultiSpeaker, not MultiSpeakerServer ?
//#include "MultiSpeaker.h"
#include "TimelineEventEditor.h"
#endif

const QString SK_XSD_FILE = "sk_xsd_file";
const QString SK_XML_FILE = "sk_xml_file";

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
	ui.resetXml->setCheckState(Qt::Unchecked);

	ui.buttonBox->button(QDialogButtonBox::Ok)->setText("Close");
	ui.buttonBox->button(QDialogButtonBox::Cancel)->hide();

	connect(ui.validateButton, SIGNAL(clicked()), SLOT(validate()));
	connect(ui.instanceEdit, SIGNAL(textChanged()), SLOT(textChanged()));
	connect(ui.buttonBox, SIGNAL(accepted()), this, SLOT(OnAccept()));
	connect(ui.buttonBox, SIGNAL(rejected()), this, SLOT(reject()));
	connect(ui.resetXsd, SIGNAL(clicked()), SLOT(resetXsd()));
	connect(ui.progressWidget, &ProgressWidget::valid8Done, this, &Valid8or::valid8Done);

	selectSchema();
	loadXml();
	// Finish laying out widgets after the window is shown so the sizes are correct
	QTimer::singleShot(0, this, &Valid8or::initializeWidgets);
	m_initialized = true;
	return true;
}
//----------------------------------------------------------------------------------------------------------------------------------
void Valid8or::initializeWidgets() {
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
	QString xsdFile = QSettings().value(SK_XSD_FILE, QVariant()).toString();
	if( xsdFile.isEmpty() ){
		QFileDialog dialog;

        m_SchemaRoot = QFileDialog::getExistingDirectory(this, tr("Select Schema XSD Directory"),
                                                        "", QFileDialog::ShowDirsOnly );// | QFileDialog::DontResolveSymlinks
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
		m_SchemaRoot = xsdFile;

	if (m_SchemaRoot.isEmpty()){
		ui.schemaSelection->setText(tr("No Schema Folder Selected"));
		return;
	}
	ui.schemaSelection->setText("Using Schema Folder " + m_SchemaRoot);

	textChanged();

}
/* notes on resource files:
 * The resource files listed in the .qrc file are files that are part of the application's source tree.
 * The specified paths are relative to the directory containing the .qrc file. Note that the listed
 * resource files must be located in the same directory as the .qrc file, or one of its subdirectories.
 *
 * reset;grep -rio --include='*.xsd' --include='*.xml' -e 'targetNamespace="[^"]*"'
 */
void Valid8or::loadXml()
{

	QString fileName = m_XmlFilename;
	/*
	QString xmlFile = QSettings().value(SK_XML_FILE, QVariant()).toString();
	if( xmlFile.isEmpty() ){
		fileName = QFileDialog::getOpenFileName(this, "Select XML File", ""
												, "XML (*xml);; All (*.*)");
		QSettings().setValue(SK_XML_FILE, fileName);
	}
	else
		fileName = xmlFile;
	if (fileName.isEmpty()){
        ui.instanceSelection->setText(tr("No XML File Selected"));
		return;
	}
	*/
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

}

void Valid8or::validate()
{
	//ui.validateButton->setEnabled(false);
	ui.validationStatus->setText("Validating...");
	ui.progressWidget->valid8Xml(m_SchemaRoot, m_EndPoint, m_XmlFilename);
}
//----------------------------------------------------------------------------------------------------------------------------------
void Valid8or::valid8Done( QString msg ) {
	ui.validationStatus->setText(msg);
	//ui.validateButton->setEnabled(true);
	ui.validateButton->setEnabled(false);
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
/*
void Valid8or::resetXml()
{
	QSettings().setValue(SK_XML_FILE, "");
	loadXml();
}
*/
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












