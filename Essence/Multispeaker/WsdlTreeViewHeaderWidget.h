//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlTreeViewHeaderWidget
//

#ifndef WSDLTREEVIEWHEADERWIDGET_H
#define WSDLTREEVIEWHEADERWIDGET_H

#include "ui_WsdlTreeViewHeaderWidget.h"

#include <QWidget>

class WsdlTreeViewHeaderWidget : public QWidget
{
  Q_OBJECT
private:
  Ui::WsdlTreeViewHeaderWidget ui;

public:
  QColor m_color;

public:
  WsdlTreeViewHeaderWidget(QWidget* parent=0);
  ~WsdlTreeViewHeaderWidget();

  bool InfoChecked() {return ui.InfoBtn->isChecked();}

  void SetColor(QColor color) {m_color = color;}
  void SetTitle(QString title, int pointSize=0);

protected:
  virtual void paintEvent(QPaintEvent* e);

signals:
  void InfoToggled();
  void SaveClicked();
};

#endif // WSDLTREEVIEWHEADERWIDGET_H
