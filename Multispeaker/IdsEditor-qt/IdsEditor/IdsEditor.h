//-------------------------------------------------------------------------------
// This code created by LMI Developments, LLC
//
// Copyright 2019.  All Rights Reserved.
//
//  Created By: Lance Irvine
//
//  IdsEditor
// 

#ifndef IDSEDITOR_H
#define IDSEDITOR_H

#include "ui_IdsEditor.h"

#include <QMainWindow>
#include <QShortcut>
#include <QStandardItemModel>

class LogDockWidget;
class RuleSection;

class IdsEditor : public QMainWindow
{
  Q_OBJECT
private:
  Ui::IdsEditorClass ui;
  QShortcut m_clearSettingsShortcut;
  QString m_iniFileName;
  QLabel m_iniFileNameLabel;
  LogDockWidget* m_logDock;
  QString m_logFileName;
  QStandardItemModel m_sectionModel;
  QHash<QString, RuleSection*> m_sections; // Key is section Name
  
public:
  IdsEditor(QWidget* parent = Q_NULLPTR);
  ~IdsEditor();

protected:
  virtual void closeEvent(QCloseEvent* e);
  virtual void resizeEvent(QResizeEvent* e) { QMainWindow::resizeEvent(e); SaveGeometry(); }

private:
  void CreateLogDock();
  void Edit(const QModelIndex& index);
  LogDockWidget& LogDock() { if (!m_logDock) CreateLogDock(); return *m_logDock; }

  QModelIndex ModelIndexByKeyAndRole(const QString& key, int role);

  void ReadIniFile(const QString& fileName);
  void RestoreGeometry();
  void RestoreState();
  QStandardItem* RuleItem(const QString& ruleKey);
  void SaveGeometry();
  void SaveState();
  QStandardItem* SectionItem(const QString& sectionKey);
  void UpdateSectionModel();
  bool WriteIniFile(const QString& fileName);

private slots:
  void OnAbout();
  void OnAboutQt();
  void OnClearSettings();
  void OnFileNew();
  void OnFileOpen();
  void OnFileSave();
  void OnFileSaveAs();
  void OnHelp();
  void OnLogDock();
  void OnLogFileChanged(const QString& fileName);
  void OnQuit() { close(); }
  void OnReadIniFile() { ReadIniFile(m_iniFileName); }
  void OnRestoreState() { RestoreState(); }
  void OnRuleDelete();
  void OnRuleEdit();
  void OnRuleNew();
  void OnRulesTreeViewDoubleClicked(const QModelIndex& index);
  void OnToolBarVisibilityChanged(bool visible);
};
#endif // IDSEDITOR_H