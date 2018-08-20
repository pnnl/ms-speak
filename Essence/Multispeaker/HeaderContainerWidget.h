//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HeaderContainerWidget
//

#ifndef HEADERCONTAINERWIDGET_H
#define HEADERCONTAINERWIDGET_H

#include "ui_HeaderContainerWidget.h"

#include <QDebug>
#include <QWidget>

class HeaderWidget;

class HeaderContainerWidget : public QWidget
{
  Q_OBJECT
private:
  Ui::HeaderContainerWidget ui;
  int m_index;

public:
  HeaderContainerWidget(int index, const QString& title, QWidget* parent=0);
  ~HeaderContainerWidget();

  void Collapse() {Container()->setVisible(false); Header()->Collapse();}

  virtual QWidget* Container() {return ui.Container;}

  void Expand() {Container()->setVisible(true); Header()->Expand();}

  virtual HeaderWidget* Header() {return ui.Header;}

  int Index() const {return m_index;}

  virtual void Update() {qDebug() << "HeaderContainerWidget::Update" << m_index;}

signals:
  void Collapsed(int index);
  void Expanded(int index);

private slots:
  void OnCollapsed() {Container()->setVisible(false); emit Collapsed(Index());}
  void OnExpanded() {Container()->setVisible(true); emit Expanded(Index());}
};

#endif // HEADERCONTAINERWIDGET_H
