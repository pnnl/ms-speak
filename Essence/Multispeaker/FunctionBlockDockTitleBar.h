//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: FunctionBlockDockTitleBar
//

#ifndef FUNCTIONBLOCKDOCKTITLEBAR_H
#define FUNCTIONBLOCKDOCKTITLEBAR_H

#include "ui_FunctionBlockDockTitleBar.h"

#include <QWidget>

class FunctionBlockDockTitleBar : public QWidget
{
  Q_OBJECT
private:
  Ui::FunctionBlockDockTitleBar ui;

public:
  FunctionBlockDockTitleBar(QWidget* parent=0);
  ~FunctionBlockDockTitleBar();

  void SetFloating(bool isFloating);
  void SetTitle(QString title, int pointSize=0);

protected:
  virtual void paintEvent(QPaintEvent* e);

signals:
  void Close();

private slots:
  void OnFloatBtn();
};

#endif // FUNCTIONBLOCKDOCKTITLEBAR_H
