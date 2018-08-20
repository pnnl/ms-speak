//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineEventEditor
//

#ifndef TIMELINEEVENTEDITOR_H
#define TIMELINEEVENTEDITOR_H

#include "ui_TimelineEventEditor.h"

#include <QDialog>

#include "TimelineEvent.h"
#include "Timer.h"

class TimelineEventEditor : public QDialog
{
  Q_OBJECT
public:
protected:
private:
  Ui::TimelineEventEditor ui;

  TimelineEvent m_request;
  TimelineEvent m_response;

public:
  TimelineEventEditor(const TimelineEvent& request, const TimelineEvent& response, QWidget* parent=0);
  ~TimelineEventEditor();

  int RequestTimeStamp() const {return Timer().TicsFromTimeInMSecs(ui.TimeStampEdit->time());}
  int ResponseTimeStamp() const {return (RequestTimeStamp() + Timer().TicsFromTimeInMSecs(ui.ResponseDelayTimeEdit->time()));}

  const TimelineEvent& Request();
  const TimelineEvent& Response();

protected:
  virtual void closeEvent(QCloseEvent* e) {SaveState(); QDialog::closeEvent(e);}

private:
  void RestoreState();
  void SaveState();

private slots:
  void OnAccept() {SaveState(); accept();}
  void OnInit();
  void OnReject() {SaveState(); reject();}
};

#endif // TIMELINEEVENTEDITOR_H
