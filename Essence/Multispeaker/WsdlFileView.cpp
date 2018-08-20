//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlFileView
//

#include <QDebug>
#include <QFileDialog>
#include <QSettings>
#include <QStandardItem>
#include <QTimer>

#include "HeaderContainerWidget.h"
#include "WsdlFileView.h"
#include "WebServiceInfo.h"
#include "WsdlMethodTemplateEditor.h"

const QString TAG_WSDL_OPERATION = "wsdl:operation";
const QString TAG_NAME = "name";

//------------------------------------------------------------------------------
// WsdlFileView
//
WsdlFileView::WsdlFileView(const QString& host, QWidget* parent)
  : QWidget(parent),
  m_host(host),
  m_wsdlFile(WsInfo().Wsdl(host))
{
  ui.setupUi(this);

  ui.TableView->setModel(&m_model);
  ui.TableView->horizontalHeader()->hide();
  ui.TableView->verticalHeader()->hide();
  ui.TableView->horizontalHeader()->setStretchLastSection(true);
  ui.TableView->setEditTriggers(QAbstractItemView::NoEditTriggers);
  connect(ui.TableView, SIGNAL(doubleClicked(const QModelIndex&)), this, SLOT(OnMethodDoubleClicked(const QModelIndex&)));

  ui.WsdlFileNameLabel->setText(QFileInfo(m_wsdlFile->FileName()).fileName());
  ui.WsdlFileNameLabel->setToolTip(QDir::toNativeSeparators(m_wsdlFile->FileName()));

  connect(ui.BrowseBtn, SIGNAL(clicked()), this, SLOT(OnBrowse()));
  connect(&m_model, SIGNAL(itemChanged(QStandardItem*)), this, SLOT(OnModelChanged(QStandardItem*)));
  connect(m_wsdlFile, SIGNAL(WsdlMethodUpdated()), this, SLOT(OnWsdlMethodUpdated()));

  // force update after the m_wsdlFile has been parsed and instantiated in its constructor
  QTimer::singleShot(0, this, SLOT(OnUpdate()));
}
//------------------------------------------------------------------------------
// ~WsdlFileView
//
WsdlFileView::~WsdlFileView()
{
}
//------------------------------------------------------------------------------
// OnBrowse
//
void WsdlFileView::OnBrowse()
{
  QString seedFile = QSettings().value(WsInfo().WsdlFileNameKey(m_host), QVariant()).toString();

  // Load file
  QString fileName = QFileDialog::getOpenFileName(this, QString("Select %1 WSDL File").arg(m_host), seedFile, "WSDL (*.wsdl);; All (*.*)");

  if (fileName.isEmpty())
    return;

  ui.WsdlFileNameLabel->setText(QFileInfo(fileName).fileName());
  ui.WsdlFileNameLabel->setToolTip(QDir::toNativeSeparators(fileName));

  if (HeaderContainerWidget* w = qobject_cast<HeaderContainerWidget*>(parent()->parent()))
  {
    w->Header()->SetTitle(QFileInfo(fileName).fileName());
    w->Header()->setToolTip(QDir::toNativeSeparators(fileName));
  }

  QSettings().setValue(WsInfo().WsdlFileNameKey(m_host), fileName);
  WsInfo().SetWsdlFile(m_host, fileName);
  m_wsdlFile = WsInfo().Wsdl(m_host);
  OnUpdate();
}
//------------------------------------------------------------------------------
// OnMethodDoubleClicked
//
void WsdlFileView::OnMethodDoubleClicked(const QModelIndex& index)
{
  if (!index.isValid())
    return;

  QString method = index.data(Qt::DisplayRole).toString();
  WsdlMethodTemplateEditor dlg(m_wsdlFile, method, this);
  dlg.exec();
}
//------------------------------------------------------------------------------
// OnModelChanged
//
void WsdlFileView::OnModelChanged(QStandardItem* item)
{
  bool isChecked = (item->checkState() == Qt::Checked) ? true : false;
  QString name = item->data(Qt::DisplayRole).toString();
  m_wsdlFile->SetMethodEnabled(name, isChecked);
}
//------------------------------------------------------------------------------
// OnUpdate
//
void WsdlFileView::OnUpdate()
{
  QApplication::setOverrideCursor(Qt::WaitCursor);
  m_model.clear();
  QStringList enabledMethods = m_wsdlFile->EnabledMethodNames();
  QStringList methods = m_wsdlFile->Methods().keys();
  methods.sort();
  foreach (const QString method, methods)
  {
    QStandardItem* item = new QStandardItem(method);
    item->setCheckable(true);
    item->setCheckState((enabledMethods.contains(method)) ? Qt::Checked : Qt::Unchecked);
    item->setToolTip(QString("Double Click to edit Template\n%1").arg(m_wsdlFile->Method(method)->Desc));
    m_model.appendRow(item);
  }
  ui.TableView->verticalHeader()->setSectionResizeMode(QHeaderView::ResizeToContents);
  QApplication::restoreOverrideCursor();
}
