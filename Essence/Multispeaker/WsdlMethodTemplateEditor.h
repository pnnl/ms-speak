//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlMethodTemplateEditor
//

#ifndef WSDLMETHODTEMPLATEEDITOR_H
#define WSDLMETHODTEMPLATEEDITOR_H

#include "ui_WsdlMethodTemplateEditor.h"

#include <QDialog>

class WsdlFile;

class WsdlMethodTemplateEditor : public QDialog
{
  Q_OBJECT
private:
  Ui::WsdlMethodTemplateEditor ui;
  QString m_method;
  WsdlFile* m_wsdlFile;
  
public:
  WsdlMethodTemplateEditor(WsdlFile* wsdlFile, const QString& method, QWidget* parent=0);
  ~WsdlMethodTemplateEditor();
protected:
private:
  void RestoreState();
  void SaveState();

signals:
private slots:
  void OnAccept();
  void OnInit();
  void OnReject() {SaveState(); reject();}
};

#endif // WSDLMETHODTEMPLATEEDITOR_H
