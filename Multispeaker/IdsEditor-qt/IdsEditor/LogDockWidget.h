//-------------------------------------------------------------------------------
// This code created by LMI Developments, LLC
//
// Copyright 2019.  All Rights Reserved.
//
//  Created By: Lance Irvine
//
//  LogDockWidget
// 

#ifndef LOGDOCKWIDGET_H
#define LOGDOCKWIDGET_H

#include "ui_LogDockWidget.h"

#include <QDockWidget>
#include <QFileSystemWatcher>

class LogDockWidget : public QDockWidget
{
  Q_OBJECT
private:
  Ui::LogDockWidget ui;

  QString m_logFileName;
  QFileSystemWatcher m_logWatcher;

public:
  LogDockWidget(const QString& title, const QString& logFileName, QWidget* parent = Q_NULLPTR);
  ~LogDockWidget();

signals:
  void LogFileChanged(const QString& logFileName);

private slots:
  void OnBrowse();
  void OnLogFileChanged(const QString& file);
  void OnMoveScrollBarToBottom(int min, int max);
  void OnRefresh();
};
#endif // LOGDOCKWIDGET_H