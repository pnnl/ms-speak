//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HeaderWidget

#ifndef HEADERWIDGET_H
#define HEADERWIDGET_H

#include "ui_HeaderWidget.h"

#include <QWidget>

class HeaderWidget : public QWidget
{
  Q_OBJECT
private:
  Ui::HeaderWidget ui;
  QColor m_color;
  bool m_isExpanded;

public:
  HeaderWidget(QWidget* parent = 0);
  ~HeaderWidget();

  void Collapse() {m_isExpanded = false; SetIcon(m_isExpanded);}
  void Expand() {m_isExpanded = true;  SetIcon(m_isExpanded);}
  bool IsCollapsed() const {return !m_isExpanded;}
  bool IsExpanded() const {return m_isExpanded;}

  void SetColor(QColor color) {m_color = color;}
	void SetExpanded(bool isExpanded) {m_isExpanded = isExpanded; SetIcon(m_isExpanded);}
  void SetTitle(QString title, int pointSize=0);
  void ShowAddDelete(bool doShow);
  QString Title() const {return ui.TitleLabel->text();}

protected:
  virtual void mouseDoubleClickEvent(QMouseEvent* e);
  virtual void mouseMoveEvent(QMouseEvent* e);
  virtual void mouseReleaseEvent(QMouseEvent* e);
  virtual void paintEvent(QPaintEvent* e);
  void SetIcon(bool isExpanded);

signals:
  void Add();
  void Collapsed();
  void Delete();
  void Expanded();

private slots:
};

#endif // HEADERWIDGET_H
