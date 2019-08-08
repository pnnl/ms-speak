//-------------------------------------------------------------------------------
// This code created by LMI Developments, LLC
//
// Copyright 2019.  All Rights Reserved.
//
//  Created By: Lance Irvine
//
//  LogDockWidget
// 

#include <QDateTime>
#include <QDir>
#include <QFileDialog>
#include <QMessageBox>
#include <QScrollBar>
#include <QTextStream>
#include <QTimer>

#include "IdsSettings.h"
#include "LogDockWidget.h"

//-------------------------------------------------------------------------------
// LogDockWidget
//
LogDockWidget::LogDockWidget(const QString& title, const QString& logFileName, QWidget* parent)
  : QDockWidget(parent),
  m_logFileName(logFileName)
{
  ui.setupUi(this);
  setWindowTitle(title);

  ui.LogFileLabel->setText(QDir::toNativeSeparators(m_logFileName));
  m_logWatcher.addPath(m_logFileName);

  connect(ui.LogFileBrowseBtn, SIGNAL(clicked()), this, SLOT(OnBrowse()));
  connect(&m_logWatcher, SIGNAL(fileChanged(const QString&)), this, SLOT(OnLogFileChanged(const QString&)));
  connect(ui.PlainTextEdit, SIGNAL(rangeChanged(int, int)), this, SLOT(OnMoveScrollBarToBottom(int, int)));
  connect(ui.LogRefreshBtn, SIGNAL(clicked()), this, SLOT(OnRefresh()));
  QTimer::singleShot(100, this, SLOT(OnRefresh()));
}
//-------------------------------------------------------------------------------
// ~LogDockWidget
//
LogDockWidget::~LogDockWidget()
{
}
//------------------------------------------------------------------------------
// OnBrowse
//
void LogDockWidget::OnBrowse()
{
  QString fileName = QFileDialog::getSaveFileName(this, QStringLiteral("Log File"),
    m_logFileName, QStringLiteral("Log File (*.log);; All (*.*)"));

  if (fileName.isEmpty())
    return;

  m_logWatcher.removePath(m_logFileName);
  m_logFileName = fileName;
  ui.LogFileLabel->setText(QDir::toNativeSeparators(fileName));
  m_logWatcher.addPath(fileName);
  OnRefresh();
  emit LogFileChanged(fileName);
}
//------------------------------------------------------------------------------
// OnLogFileChanged
//
void LogDockWidget::OnLogFileChanged(const QString& file)
{
  Q_UNUSED(file);
  OnRefresh();
}
//------------------------------------------------------------------------------
// OnMoveScrollBarToBottom
//
void LogDockWidget::OnMoveScrollBarToBottom(int min, int max)
{
  Q_UNUSED(min);
  ui.PlainTextEdit->verticalScrollBar()->setValue(max);
}
//------------------------------------------------------------------------------
// OnRefresh
//
void LogDockWidget::OnRefresh()
{
  ui.PlainTextEdit->clear();

  if (!QFileInfo::exists(m_logFileName))
  {
    // Write an entry so the file exists
    QFile file(m_logFileName);
    if (file.open(QIODevice::WriteOnly))
    {
      QTextStream out(&file);
      out << QStringLiteral("%1: Log Created")
        .arg(QDateTime::currentDateTime().toString("yyyy.MM.dd hh:mm:ss.z")) << endl;
    }
    file.close();
  }
  QFile file(m_logFileName);
  if (file.open(QIODevice::ReadOnly))
  {
    ui.PlainTextEdit->appendPlainText(file.readAll());
  }
  else
  {
    QMessageBox::warning(this, QStringLiteral("IDS Editor"),
      QStringLiteral("Unable to Read File: %1").arg(m_logFileName),
      QMessageBox::Ok, QMessageBox::Ok);
  }
  file.close();
}
