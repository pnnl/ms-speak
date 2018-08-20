//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: MultiSpeaker
//

#ifndef MULTISPEAKER_H
#define MULTISPEAKER_H

#include "ui_MultiSpeaker.h"

#include <QHash>
#include <QMainWindow>
#include <QProcess>
#include <QShortcut>
#include <QToolBar>

#include "FunctionBlockDock.h"
#include "LogDock.h"
#include "MethodDock.h"
#include "TimelineEvent.h"
#include "WsdlDock.h"

class MultiSpeaker : public QMainWindow
{
  Q_OBJECT
private:
  Ui::MultiSpeakerClass ui;

	QShortcut m_clearSettingsShortcut;
  FunctionBlockDock* m_functionBlockDock;
  LogDock* m_logDock;

  MethodDock* m_methodDock;
  LogDock* m_miniNetCmdDock;

  WsdlDock* m_wsdlDock;

public:
  MultiSpeaker(QWidget* parent=0);
  ~MultiSpeaker();

protected:
	virtual void closeEvent(QCloseEvent* e);
  virtual void resizeEvent(QResizeEvent* e) {Q_UNUSED(e); SaveState();}

private:
  void CreateFunctionBlockDock();
  void CreateLogDock();
  void CreateMethodDock();
  void CreateMiniNetCmdDock();
  void CreateTitleToolBar();
  void CreateToolBar();
  void CreateWsdlDock();

  void EditTimelineEvent(TimelineEvent& e);

  FunctionBlockDock& FunctionBlockDockkRef() {if (!m_functionBlockDock) CreateFunctionBlockDock(); return *m_functionBlockDock;}
  LogDock& LogDockRef() {if (!m_logDock) CreateLogDock(); return *m_logDock;}

  MethodDock& MethodDockRef() {if (!m_methodDock) CreateMethodDock(); return *m_methodDock;}
  LogDock& MiniNetCmdDockRef() {if (!m_miniNetCmdDock) CreateMiniNetCmdDock(); return *m_miniNetCmdDock;}

  void RestoreState();
  void SaveState();

  WsdlDock& WsdlDockRef() {if (!m_wsdlDock) CreateWsdlDock(); return *m_wsdlDock;}

signals:
private slots:
  void OnAbout();
  void OnClearSettings();
  void OnHostDoubleClicked(int id);
  void OnHostSceneChanged();
  void OnMiniNet();
  void OnMiniNetMsg(const QString& msg) {LogDockRef().Append(msg);}
  void OnTimelineEventDoubleClicked(TimelineEvent& e) {EditTimelineEvent(e);}
  void OnTimelineEventListViewDoubleClicked(const QModelIndex& index);
  void OnToolBarVisibilityChanged(bool visible) {if (!visible) qobject_cast<QToolBar*>(sender())->setVisible(true);} // Prevent user from hiding the main tool bar
  void OnWsdl() {WsdlDockRef().show();}
  void OnWsdlFileChanged(const QString& host);

};

#endif // MULTISPEAKER_H
