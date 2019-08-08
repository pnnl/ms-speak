//-------------------------------------------------------------------------------
// This code created by LMI Developments, LLC
//
// Copyright 2019.  All Rights Reserved.
//
//  Created By: Lance Irvine
//
//  IdsEditor
// 

#include <QDesktopServices>
#include <QDir>
#include <QFileDialog>
#include <QMessageBox>
#include <QSettings>
#include <QStandardItem>
#include <QTextStream>
#include <QTimer>
#include <QToolBar>
#include <QToolButton>

#include "IdsEditor.h"
#include "IdsSettings.h"
#include "LogDockWidget.h"
#include "Rule.h"
#include "RuleConst.h"
#include "RuleEditor.h"

bool CLEAR_SETTINGS_ON_EXIT = false; // Used for the clear settings shortcut feature (Ctrl+Shift+C)

//-------------------------------------------------------------------------------
// IdsEditor
//
IdsEditor::IdsEditor(QWidget* parent)
  : QMainWindow(parent),
  m_clearSettingsShortcut(QKeySequence(QStringLiteral("Ctrl+Shift+C")), this, SLOT(OnClearSettings())),
  m_iniFileName(QSettings().value(SK_INI_FILE_NAME, INI_FILE_NAME).toString()),
  m_logDock(Q_NULLPTR),
  m_logFileName(QSettings().value(SK_LOG_FILE_NAME, LOG_FILE_NAME).toString())
{
  ui.setupUi(this);
  setWindowTitle(QStringLiteral("IDS Editor %1").arg(SOFTWARE_VERSION));
  RestoreGeometry();

  ui.RulesTreeView->setModel(&m_sectionModel);
  ui.RulesTreeView->setHeaderHidden(true);
  ui.RulesTreeView->setSelectionBehavior(QAbstractItemView::SelectRows);
  ui.RulesTreeView->setSelectionMode(QAbstractItemView::SingleSelection);
  ui.RulesTreeView->setEditTriggers(QAbstractItemView::NoEditTriggers);

  statusBar()->addWidget(&m_iniFileNameLabel);
  m_iniFileNameLabel.setText(QDir::toNativeSeparators(m_iniFileName));

  connect(ui.FileNewAct, SIGNAL(triggered()), this, SLOT(OnFileNew()));
  connect(ui.FileOpenAct, SIGNAL(triggered()), this, SLOT(OnFileOpen()));
  connect(ui.FileSaveAct, SIGNAL(triggered()), this, SLOT(OnFileSave()));
  connect(ui.FileSaveAsAct, SIGNAL(triggered()), this, SLOT(OnFileSaveAs()));
  connect(ui.HelpAboutAct, SIGNAL(triggered()), this, SLOT(OnAbout()));
  connect(ui.HelpAct, SIGNAL(triggered()), this, SLOT(OnHelp()));
  connect(ui.HelpLicensingAct, SIGNAL(triggered()), this, SLOT(OnAboutQt()));
  connect(ui.LogAct, SIGNAL(triggered()), this, SLOT(OnLogDock()));
  connect(ui.QuitAct, SIGNAL(triggered()), this, SLOT(OnQuit()));

  connect(ui.DeleteBtn, SIGNAL(clicked()), this, SLOT(OnRuleDelete()));
  connect(ui.EditBtn, SIGNAL(clicked()), this, SLOT(OnRuleEdit()));
  connect(ui.NewBtn, SIGNAL(clicked()), this, SLOT(OnRuleNew()));

  connect(ui.RulesTreeView, SIGNAL(doubleClicked(const QModelIndex&)), this, SLOT(OnRulesTreeViewDoubleClicked(const QModelIndex&)));

  QTimer::singleShot(100, this, SLOT(OnRestoreState())); // Restore State after Docks Created
  QTimer::singleShot(100, this, SLOT(OnReadIniFile()));
}
//-------------------------------------------------------------------------------
// ~IdsEditor
//
IdsEditor::~IdsEditor()
{
  qDeleteAll(m_sections);
  m_sections.clear();
}
//------------------------------------------------------------------------------
// closeEvent
//
void IdsEditor::closeEvent(QCloseEvent* e)
{
  SaveState();

  // If the user has enabled the clear settings on exit ctrl-shift-c hot key combo, then clear them after save state called
  if (CLEAR_SETTINGS_ON_EXIT)
    QSettings().clear();

  if (!WriteIniFile(m_iniFileName))
  {
    QMessageBox::warning(this, QStringLiteral("IDS Editor"),
      QStringLiteral("Unable to Save File: %1").arg(m_iniFileName),
      QMessageBox::Ok,
      QMessageBox::Ok);
  }

  QMainWindow::closeEvent(e);
}
//------------------------------------------------------------------------------
// CreateLogDock
//
void IdsEditor::CreateLogDock()
{
  m_logDock = new LogDockWidget(QStringLiteral("Log"), m_logFileName, this);
  connect(m_logDock, SIGNAL(LogFileChanged(const QString&)), this, SLOT(OnLogFileChanged(const QString&)));
  addDockWidget(Qt::BottomDockWidgetArea, m_logDock);
}
//------------------------------------------------------------------------------
// Edit
//
void IdsEditor::Edit(const QModelIndex& index)
{
  if (index.isValid())
  {
    if (index.data(ROLE_SECTION_KEY).isValid())
    {
      QString sectionKey = index.data(ROLE_SECTION_KEY).toString();
      if (RuleSection* section = m_sections.value(sectionKey, Q_NULLPTR))
      {
        RuleEditor dlg(*section, this);
        if (dlg.exec())
        {
          if (section->Section() == dlg.Section().Section())
          {
            // Same Section...so just copy
            section->Copy(dlg.Section());
          }
          else
          {
            // Different Section so delete old one and add new one
            delete m_sections.take(section->Section());
            section = new RuleSection(dlg.Section());
            m_sections.insert(section->Section(), section);
          }
          UpdateSectionModel();
        }
      }
    }
  }
}
//------------------------------------------------------------------------------
// ModelIndexByKeyAndRole
//
QModelIndex IdsEditor::ModelIndexByKeyAndRole(const QString& section, int role)
{
  QModelIndex idx;
  if (QStandardItem* item = m_sectionModel.item(0))
    idx = item->index();

  QModelIndexList idxList = m_sectionModel.match(idx, role, section, 1, Qt::MatchExactly | Qt::MatchRecursive | Qt::MatchWrap);
  if (idxList.count())
    return idxList.first();
  else
    return QModelIndex();
}
//------------------------------------------------------------------------------
// ReadIniFile
//
void IdsEditor::ReadIniFile(const QString& fileName)
{
  qDeleteAll(m_sections);
  m_sections.clear();

  QSettings ini(fileName, QSettings::IniFormat);

  QString sectionKey;
  QString key;
  QString value;
  for (QString iniKey : ini.allKeys())
  {
    sectionKey = QStringLiteral("[%1]").arg(iniKey.left(iniKey.indexOf(QStringLiteral("/"))));

    if (sectionKey.startsWith(SETTINGS_GROUP))
    {
      key = iniKey.right(iniKey.length() - iniKey.indexOf(QStringLiteral("/")) - 1);
      if (key == SETTINGS_LOG_FILE)
        m_logFileName = ini.value(iniKey).toString();
      continue;
    }

    if (!m_sections.contains(sectionKey))
      m_sections.insert(sectionKey, new RuleSection());

    if (RuleSection* section = m_sections.value(sectionKey, Q_NULLPTR))
    {
      section->Method = iniKey.left(iniKey.indexOf(QStringLiteral("@")));
      section->EndPoint = iniKey.mid(iniKey.indexOf(QStringLiteral("@")) + 1, iniKey.indexOf(QStringLiteral("/")) - iniKey.indexOf(QStringLiteral("@")) - 1);
      key = iniKey.right(iniKey.length() - iniKey.indexOf(QStringLiteral("/")) - 1);
      value = ini.value(iniKey).toString();

      if (key == RULE_KEY_NUMREQ)
      {
        if (!section->Rules.contains(RULE_TYPE_MAX_VALUE))
          section->Rules.insert(RULE_TYPE_MAX_VALUE, new Rule());

        if (Rule* rule = section->Rules.value(RULE_TYPE_MAX_VALUE, Q_NULLPTR))
        {
          rule->Name = RULE_TYPE_MAX_VALUE;
          rule->KeyValue.insert(key, value);
        }
      }
      else if (key == RULE_KEY_MAXTEMP || key == RULE_KEY_MINTEMP)
      {
        if (!section->Rules.contains(RULE_TYPE_TEMP_RANGE))
          section->Rules.insert(RULE_TYPE_TEMP_RANGE, new Rule());

        if (Rule* rule = section->Rules.value(RULE_TYPE_TEMP_RANGE, Q_NULLPTR))
        {
          rule->Name = RULE_TYPE_TEMP_RANGE;
          rule->KeyValue.insert(key, value);
        }
      }
      else if (key == RULE_KEY_MAXTIME || key == RULE_KEY_MINTIME)
      {
        if (!section->Rules.contains(RULE_TYPE_TIME_RANGE))
          section->Rules.insert(RULE_TYPE_TIME_RANGE, new Rule());

        if (Rule* rule = section->Rules.value(RULE_TYPE_TIME_RANGE, Q_NULLPTR))
        {
          rule->Name = RULE_TYPE_TIME_RANGE;
          rule->KeyValue.insert(key, value);
        }
      }
    }
  }
  UpdateSectionModel();
}
//------------------------------------------------------------------------------
// RestoreGeometry
//
void IdsEditor::RestoreGeometry()
{
  restoreGeometry(QSettings().value(SK_MAIN_GEOMETRY).toByteArray());
}
//------------------------------------------------------------------------------
// RestoreState
//
void IdsEditor::RestoreState()
{
  restoreState(QSettings().value(SK_MAIN_STATE).toByteArray());
}
//------------------------------------------------------------------------------
// RuleItem
//
QStandardItem* IdsEditor::RuleItem(const QString& ruleKey)
{
  return m_sectionModel.itemFromIndex(ModelIndexByKeyAndRole(ruleKey, ROLE_RULE_KEY));
}
//------------------------------------------------------------------------------
// SaveGeometry
//
void IdsEditor::SaveGeometry()
{
  QSettings().setValue(SK_MAIN_GEOMETRY, saveGeometry());
}
//------------------------------------------------------------------------------
// SaveState
//
void IdsEditor::SaveState()
{
  QSettings().setValue(SK_MAIN_STATE, saveState());
}
//------------------------------------------------------------------------------
// SectionItem
//
QStandardItem* IdsEditor::SectionItem(const QString& ruleKey)
{
  return m_sectionModel.itemFromIndex(ModelIndexByKeyAndRole(ruleKey, ROLE_SECTION_KEY));
}
//------------------------------------------------------------------------------
// UpdateSectionModel
//
void IdsEditor::UpdateSectionModel()
{
  m_sectionModel.clear();
  for (RuleSection* section : m_sections)
  {
    QStandardItem* sectionItem = new QStandardItem(section->Section());
    sectionItem->setData(section->Section(), ROLE_SECTION_KEY);
    m_sectionModel.appendRow(sectionItem);
    for (Rule* rule : section->Rules)
    {
      QStandardItem* ruleItem = new QStandardItem(rule->ToString());
      ruleItem->setData(section->Section(), ROLE_SECTION_KEY);
      ruleItem->setData(rule->ToString(), ROLE_RULE_KEY);
      sectionItem->appendRow(ruleItem);
    }
  }
}
//------------------------------------------------------------------------------
// WriteIniFile
//
bool IdsEditor::WriteIniFile(const QString& fileName)
{
  QFile file(fileName);
  if (file.open(QIODevice::WriteOnly))
  {
    QTextStream out(&file);

    // Log File
    out << SETTINGS_GROUP << endl;
    out << QStringLiteral("%1 = %2").arg(SETTINGS_LOG_FILE, m_logFileName) << endl << endl;
    
    // Rules
    for (RuleSection* section : m_sections)
      out << section->ToString() << endl << endl;
    file.close();
    return true;
  }
  return false;
}
//------------------------------------------------------------------------------
// OnAbout
//
void IdsEditor::OnAbout()
{
  QMessageBox::about(this, QStringLiteral("IDS Editor"), SOFTWARE_ABOUT);
}
//------------------------------------------------------------------------------
// OnAboutQt
//
void IdsEditor::OnAboutQt()
{
  QMessageBox::aboutQt(this, QStringLiteral("Qt License"));
}
//------------------------------------------------------------------------------
// OnClearSettings
//
void IdsEditor::OnClearSettings()
{
  if (QMessageBox::Ok == QMessageBox::question(this, QStringLiteral("Clear Settings"),
    QStringLiteral("All the Settings for Windows Sizes and Docking positions will be reset on exit of application."), QMessageBox::Ok | QMessageBox::Cancel))
  {
    CLEAR_SETTINGS_ON_EXIT = true;
  }
}
//------------------------------------------------------------------------------
// OnFileNew
//
void IdsEditor::OnFileNew()
{
  QString fileName = QFileDialog::getSaveFileName(this, QStringLiteral("New Biz Rules Config File"),
    m_iniFileName, QStringLiteral("Config File (*.cfg);; All (*.*)"));

  if (fileName.isEmpty())
    return;

  m_iniFileName = fileName;
  ReadIniFile(m_iniFileName);
  UpdateSectionModel();

  QSettings().setValue(SK_INI_FILE_NAME, m_iniFileName);
  m_iniFileNameLabel.setText(QDir::toNativeSeparators(m_iniFileName));
}
//------------------------------------------------------------------------------
// OnFileOpen
//
void IdsEditor::OnFileOpen()
{
  QString fileName = QFileDialog::getOpenFileName(this, QStringLiteral("Biz Rules Config File"),
    m_iniFileName, QStringLiteral("Config File (*.cfg);; All (*.*)"));

  if (fileName.isEmpty())
    return;

  m_iniFileName = fileName;
  ReadIniFile(m_iniFileName);
  UpdateSectionModel();

  QSettings().setValue(SK_INI_FILE_NAME, m_iniFileName);
  m_iniFileNameLabel.setText(QDir::toNativeSeparators(m_iniFileName));
}
//------------------------------------------------------------------------------
// OnFileSave
//
void IdsEditor::OnFileSave()
{
  WriteIniFile(m_iniFileName);
}
//------------------------------------------------------------------------------
// OnFileSaveAs
//
void IdsEditor::OnFileSaveAs()
{
  QString fileName = QFileDialog::getSaveFileName(this, QStringLiteral("New Biz Rules Config File"),
    m_iniFileName, QStringLiteral("Config File (*.cfg);; All (*.*)"));

  if (fileName.isEmpty())
    return;

  m_iniFileName = fileName;

  QSettings().setValue(SK_INI_FILE_NAME, m_iniFileName);
  m_iniFileNameLabel.setText(QDir::toNativeSeparators(m_iniFileName));
}
//------------------------------------------------------------------------------
// OnHelp
//
void IdsEditor::OnHelp()
{
  QDesktopServices::openUrl(QUrl(QStringLiteral("file:///%1").arg(IDS_EDITOR_HELP_PDF), QUrl::TolerantMode));
}
//------------------------------------------------------------------------------
// OnLogDock
//
void IdsEditor::OnLogDock()
{
  LogDock().show();
}
//------------------------------------------------------------------------------
// OnLogFileChanged
//
void IdsEditor::OnLogFileChanged(const QString& fileName)
{
  m_logFileName = fileName;
  QSettings().setValue(SK_LOG_FILE_NAME, m_logFileName);
  WriteIniFile(m_iniFileName);
}
//------------------------------------------------------------------------------
// OnRuleDelete
//
void IdsEditor::OnRuleDelete()
{
  QModelIndexList list = ui.RulesTreeView->selectionModel()->selectedIndexes();
  for (QModelIndex index : list)
  {
    if (index.isValid())
    {
      if (index.data(ROLE_SECTION_KEY).isValid())
      {
        delete m_sections.take(index.data(ROLE_SECTION_KEY).toString());
        UpdateSectionModel();
      }
    }
  }
}
//------------------------------------------------------------------------------
// OnRuleEdit
//
void IdsEditor::OnRuleEdit()
{
  QModelIndexList list = ui.RulesTreeView->selectionModel()->selectedIndexes();
  for (QModelIndex index : list)
  {
    Edit(index);
    break; // Only want first one
  }
}
//------------------------------------------------------------------------------
// OnRuleNew
//
void IdsEditor::OnRuleNew()
{
  RuleSection section;
  RuleEditor dlg(section, this);
  if (dlg.exec())
  {
    section.Copy(dlg.Section());
    QString sectionKey = section.Section();
    if (m_sections.contains(sectionKey))
      delete m_sections.take(sectionKey);

    m_sections.insert(sectionKey, new RuleSection(section));
    UpdateSectionModel();
  }
}
//------------------------------------------------------------------------------
// OnRulesTreeViewDoubleClicked
//
void IdsEditor::OnRulesTreeViewDoubleClicked(const QModelIndex& index)
{
  Edit(index);
}
//------------------------------------------------------------------------------
// OnToolBarVisibilityChanged
//
void IdsEditor::OnToolBarVisibilityChanged(bool visible)
{
  // Prevent user from hiding the main tool bar
  if (!visible) qobject_cast<QToolBar*>(sender())->setVisible(true);
}
