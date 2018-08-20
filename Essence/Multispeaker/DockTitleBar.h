//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: DockTitleBar
//

#ifndef DOCKTITLEBAR_H
#define DOCKTITLEBAR_H

#include "ui_DockTitleBar.h"

#include <QWidget>

class DockTitleBar : public QWidget
{
  Q_OBJECT
public:
protected:
private:
  Ui::DockTitleBar ui;

public:
  DockTitleBar(QWidget* parent=0);
  ~DockTitleBar();

  void SetFloating(bool isFloating);
  void SetTitle(QString title, int pointSize=0);

protected:
  virtual void paintEvent(QPaintEvent* e);

signals:
  void Close();

private slots:
  void OnFloatBtn();
};

#endif // DOCKTITLEBAR_H
