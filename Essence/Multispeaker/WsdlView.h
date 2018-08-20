//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlView
//

#ifndef WSDLVIEW_H
#define WSDLVIEW_H

#include "ui_WsdlView.h"

#include <QApplication>
#include <QWidget>

class QTreeWidget;
class QTreeWidgetItem;
class WsdlFileView;

class WsdlView : public QWidget
{
  Q_OBJECT
public:
protected:
private:
  Ui::WsdlView ui;

public:
  WsdlView(QWidget* parent=0);
  ~WsdlView();

protected:
  //virtual bool event(QEvent* e);
  virtual void paintEvent(QPaintEvent* e);

private:
  void AddWsdlFileView(QTreeWidget* tree, QTreeWidgetItem* parent, WsdlFileView* view);
  void CreateToolBox(const QStringList& fileNames);
  void UpdateStatusMsg(const QString& msg) {ui.StatusFrame->show(); ui.StatusLabel->setText(msg); QApplication::processEvents();}

signals:
private slots:
  void OnBrowse();
  void OnHideStatusFrame() {ui.StatusFrame->hide();}
};

#endif // WSDLVIEW_H
