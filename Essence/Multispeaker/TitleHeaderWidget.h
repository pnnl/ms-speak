//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TitleHeaderWidget
//

#ifndef TITLEHEADERWIDGET_H
#define TITLEHEADERWIDGET_H

#include "ui_TitleHeaderWidget.h"

#include <QWidget>

class TitleHeaderWidget : public QWidget
{
  Q_OBJECT
private:
  Ui::TitleHeaderWidget ui;

  QColor m_color;

public:
  TitleHeaderWidget(QWidget* parent=0);
  ~TitleHeaderWidget();

  void SetColor(QColor color) {m_color = color;}
  void SetTitle(QString title, int pointSize=0);

protected:
  virtual void paintEvent(QPaintEvent* e);
};

#endif // TITLEHEADERWIDGET_H
