//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineHeaderWidget
//

#ifndef TIMELINEHEADERWIDGET_H
#define TIMELINEHEADERWIDGET_H

#include "ui_TimelineHeaderWidget.h"

#include <QWidget>

class TimelineHeaderWidget : public QWidget
{
  Q_OBJECT
private:
  Ui::TimelineHeaderWidget ui;

  QColor m_color;

public:
  TimelineHeaderWidget(QWidget* parent=0);
  ~TimelineHeaderWidget();

  void SetColor(QColor color) {m_color = color;}
  void SetTitle(QString title, int pointSize=0);
  
protected:
  virtual void paintEvent(QPaintEvent* e);

signals:
  void ClearClicked();
  void PauseClicked();
  void PlayClicked();
  void ResetClicked();
};

#endif // TIMELINEHEADERWIDGET_H
