//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: MiniNetEditor
//

#ifndef MININETEDITOR_H
#define MININETEDITOR_H

#include "ui_MiniNetEditor.h"

#include <QDialog>
#include <QDir>

class MiniNetEditor : public QDialog
{
  Q_OBJECT
public:
protected:
private:
  Ui::MiniNetEditor ui;
  bool m_doStart;
  bool m_doStop;

public:
  MiniNetEditor(QWidget* parent=0);
  ~MiniNetEditor();

  QString App() const {return ui.AppEdit->text();}
  QString ConfFile() const {return QDir::fromNativeSeparators(ui.ConfFileEdit->text());}
  QString HostIp() const {return ui.HostIpEdit->text();}
  int HostPort() const {return ui.HostPortSpin->value();}
  QString NetworkId() const {return ui.NetworkIdEdit->text();}
  QString ScriptFile() const {return QDir::fromNativeSeparators(ui.ScriptFileEdit->text());}
  QString CmdLine() const {return ui.CmdLineEdit->toPlainText();}

  bool DoStart() const {return m_doStart;}
  bool DoStop() const {return m_doStop;}

private slots:
  void OnConfFileBrowse();
  void OnHostIpEditFinished();
  void OnHostPortValueChanged(int port);
  void OnInit();
  void OnScriptFileBrowse();
  void OnStartClicked();
  void OnStopClicked();
  void OnUpdateCmdLineEdit();
};

#endif // MININETEDITOR_H
