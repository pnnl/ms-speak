//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HostEditor
//

#ifndef HOSTEDITOR_H
#define HOSTEDITOR_H

#include "ui_HostEditor.h"

#include <QDialog>

#include "Host.h"

class HostEditor : public QDialog
{
  Q_OBJECT
private:
  Ui::HostEditor ui;
  Host m_host;

public:
  HostEditor(const Host& host, QWidget* parent=0);
  ~HostEditor();

  const Host& HostRef() const {return m_host;}

private slots:
  void OnCheckToggled(bool checked);
};

#endif // HOSTEDITOR_H
