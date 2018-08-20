//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlXmlViewHeaderWidget
//

#ifndef WSDLXMLVIEWHEADERWIDGET_H
#define WSDLXMLVIEWHEADERWIDGET_H

#include "ui_WsdlXmlViewHeaderWidget.h"

#include <QWidget>

class WsdlXmlViewHeaderWidget : public QWidget
{
  Q_OBJECT
public:
protected:
private:
  Ui::WsdlXmlViewHeaderWidget ui;

public:
  QColor m_color;

public:
  WsdlXmlViewHeaderWidget(QWidget* parent=0);
  ~WsdlXmlViewHeaderWidget();

  void SetColor(QColor color) {m_color = color;}
  void SetTitle(QString title, int pointSize=0);

protected:
  virtual void paintEvent(QPaintEvent* e);

signals:
  void ExportClicked();
  //void RefreshClicked();
};

#endif // WSDLXMLVIEWHEADERWIDGET_H
