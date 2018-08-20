//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlView
//

#include <QDir>
#include <QEvent>
#include <QFileDialog>
#include <QPainter>
#include <QScrollArea>
#include <QSettings>
#include <QTimer>
#include <QToolBox>
#include <QTreeWidget>

#include "Settings.h"
#include "WsdlFileView.h"
#include "WsdlView.h"

//------------------------------------------------------------------------------
// WsdlView
//
WsdlView::WsdlView(QWidget* parent)
  : QWidget(parent)
{
  ui.setupUi(this);
  UpdateStatusMsg("");
  ui.ProgressBar->setVisible(false);
  connect(ui.BrowseBtn, SIGNAL(clicked()), this, SLOT(OnBrowse()));

  ui.StatusFrame->hide();
  ui.FileNameLabel->setText(QDir::toNativeSeparators(QSettings().value(SK_WSDL_IMPORT_FILE_NAME, QDir::homePath()).toString()));
}
//------------------------------------------------------------------------------
// ~WsdlView
//
WsdlView::~WsdlView()
{
}
////-------------------------------------------------------------------------------
//// event
////
//bool WsdlView::event(QEvent* e)
//{
//  return true;
//}
//-------------------------------------------------------------------------------
// paintEvent
//
void WsdlView::paintEvent(QPaintEvent* e)
{
  QWidget::paintEvent(e);
  QPainter p(this);

  p.setPen(Qt::black);
  p.setBrush(Qt::lightGray);
  p.drawRect(QRect(0, 0, width()-1, height()-1));
  p.end();
}
//------------------------------------------------------------------------------
// AddWsdlFileView
//
void WsdlView::AddWsdlFileView(QTreeWidget* tree, QTreeWidgetItem* parent, WsdlFileView* view)
{
  QTreeWidgetItem* item = new QTreeWidgetItem(parent);
  item->setFlags(Qt::ItemIsEnabled);
  //connect(view, SIGNAL(scratchPadChanged()), this, SLOT(slotSave()));
  //connect(view, SIGNAL(pressed(QString,QString,QPoint)), this, SIGNAL(pressed(QString,QString,QPoint)));
  //connect(view, SIGNAL(itemRemoved()), this, SLOT(slotScratchPadItemDeleted()));
  //connect(view, SIGNAL(lastItemRemoved()), this, SLOT(slotLastScratchPadItemDeleted()));
  tree->setItemWidget(item, 0, view);
}
//------------------------------------------------------------------------------
// CreateToolBox
//
void WsdlView::CreateToolBox(const QStringList& fileNames)
{
  UpdateStatusMsg("Parsing...");
  ui.ProgressBar->setVisible(true);
  ui.ProgressBar->setMinimum(0);
  ui.ProgressBar->setValue(0);
  ui.ProgressBar->setMaximum(fileNames.count());

  QToolBox* toolBox = new QToolBox(ui.ScrollArea);
  toolBox->setObjectName(QStringLiteral("ToolBox"));
  ui.ScrollArea->setWidget(toolBox);

  int i = 0;
  foreach (const QString& fileName, fileNames)
  {
    QWidget* page = new QWidget();
    page->setObjectName(QString("Page%1").arg(i));
    page->setGeometry(QRect(0, 0, 1180, 392));
    QVBoxLayout* layout = new QVBoxLayout(page);
    layout->setSpacing(0);
    layout->setContentsMargins(2, 2, 2, 2);
    WsdlFile wsdlFile(fileName, this);
    WsdlFileView* view = new WsdlFileView(wsdlFile, page);
    connect(view, SIGNAL(Float(const QString&)), this, SLOT(OnFloat(const QString&)));
    view->setObjectName(QString("View%1").arg(i));
    layout->addWidget(view);
    //m_EyeRetinaFileHash.insert(fileName, view->EyeRetinaFileObj()); // populate hash for later export
    page->setToolTip(QDir::toNativeSeparators(fileName));
    toolBox->setItemIcon(toolBox->addItem(page, QFileInfo(fileName).fileName()), QIcon(QStringLiteral(":/MultiSpeaker/Resources/float_dock-16.png")));
    ui.ProgressBar->setValue(++i);
  }
  ui.ProgressBar->setVisible(false);
  UpdateStatusMsg("Parse Complete.");
  QTimer::singleShot(1000, this, SLOT(OnHideStatusFrame()));
}
//------------------------------------------------------------------------------
// OnBrowse
//
void WsdlView::OnBrowse()
{
  QString seedFile = QSettings().value(SK_WSDL_IMPORT_FILE_NAME, QDir::homePath()).toString();

  // Load file
  QStringList fileNames = QFileDialog::getOpenFileNames(this, "Select WSDL File(s)", seedFile, "WSDL (*.wsdl);; All (*.*)");

  if (fileNames.isEmpty())
    return;

  QStringList nativeFileNames;
  foreach (QString name, fileNames)
    nativeFileNames << QDir::toNativeSeparators(name);

  ui.FileNameLabel->setText(nativeFileNames.join(","));
  ui.FileNameLabel->setToolTip(nativeFileNames.join("\n"));

  QSettings().setValue(SK_WSDL_IMPORT_FILE_NAME, fileNames.first());

  CreateToolBox(fileNames);
}
