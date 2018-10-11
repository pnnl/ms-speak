/*---------------------------------------------------------------*
 |                       OFFICIAL USE ONLY                       |
 | May be exempt from public release under the Freedom of        |
 | Information Act (5 U.S.C 552), exemption number and category: |
 |                                                               |
 |   3, Statutory Exemption                                      |
 |   5, Privileged Information                                   |
 |   7, Law Enforcement                                          |
 |                                                               |
 | Department of Energy review required before public release    |
 |                                                               |
 | Name / Org:               Wayne Meitzler / D7P25              |
 | Date:                     20180806                            |
 | Guidance (if applicable): Client Correspondence               |
 *---------------------------------------------------------------*/

//----------------------------------------------------------------------------------------------------------------------------------
// Copyright (c) 2013-2018, Pacific Northwest National Laboratory
// This software is subject to copyright protection under the laws of the United States and other countries
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//----------------------------------------------------------------------------------------------------------------------------------

#include "ProgressWidget.h"
#include "ui_ProgressWidget.h"

#include <QColor>
#include <QMessageBox>
#include <QRegularExpression>
#include <QScrollBar>
#include <QSettings>
#include <QStandardItemModel>
#include <QThread>
#include <QTimer>
#include <QToolBar>
#include <QToolButton>
//#include <QDebug>

#include "Valid8Worker.h"
#include "QSL.h"

//----------------------------------------------------------------------------------------------------------------------------------
ProgressWidget::ProgressWidget(QWidget *parent)
	: QWidget{parent}
	, ui{new Ui::ProgressWidget}
{
	ui->setupUi(this);
	m_currentOperationTimer = new QTimer(this);
	m_currentOperationTimer->setInterval(1000); // 1 second

	connect(m_currentOperationTimer, &QTimer::timeout, this, &ProgressWidget::operationTick);
}

//----------------------------------------------------------------------------------------------------------------------------------
ProgressWidget::~ProgressWidget() {
	delete ui;
}

//----------------------------------------------------------------------------------------------------------------------------------
void ProgressWidget::valid8Xml( QString s, QString e, QString x )
{
	m_valid8Worker = new Valid8Worker( s, e, x );
	QThread *thread      = new QThread;
    m_valid8Worker->moveToThread(thread);
    connect(m_valid8Worker, &Valid8Worker::finished, thread, &QThread::quit);
    connect(m_valid8Worker, &Valid8Worker::finished, this,   &ProgressWidget::valid8XmlFinished);
    connect(m_valid8Worker, &Valid8Worker::log,      this,   &ProgressWidget::operationLog);
    connect(m_valid8Worker, &Valid8Worker::progress, this,   &ProgressWidget::operationProgress);
    connect(thread,         &QThread::started,  m_valid8Worker, &Valid8Worker::start);
    connect(thread,         &QThread::finished, m_valid8Worker, &Valid8Worker::deleteLater);
    connect(thread,         &QThread::finished, thread, &QThread::deleteLater);
	thread->start(QThread::HighPriority);
	m_currentOperationStartTime = QDateTime::currentDateTime();
	m_currentOperationTimer->start();
}

//----------------------------------------------------------------------------------------------------------------------------------
void ProgressWidget::valid8XmlFinished(const QString &msg) {
	m_currentOperationTimer->stop();
    m_valid8Worker = nullptr;
	operationTick();
	operationLog(QSL("%1 after %2").arg(msg, ui->elapsedTime->text()), Qt::white);
	emit valid8Done(msg);
	//qDebug() << "valid8XmlFinished: " << msg;
}

//----------------------------------------------------------------------------------------------------------------------------------
int ProgressWidget::calculateProgressValue(const OperationInfo &operationInfo) {
	return operationInfo.progress * ui->progress->maximum();
}

//----------------------------------------------------------------------------------------------------------------------------------
void ProgressWidget::operationLog(const QString &msg, const Qt::GlobalColor color) {
	static const QChar newline('\n');
	const QStringList lines = msg.split(newline, QString::SkipEmptyParts);
	if (lines.isEmpty()) {
		return;
	}

	for (QString line : lines) {
		// Strip date/time from beginning of line
		static const QRegularExpression regex(QSL("^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} "));
		line.remove(regex);

		const QString dateTime(QDateTime::currentDateTime().toString(QSL("yyyy-MM-dd hh:mm:ss.zzz")));
		QString html(QSL("<span style=\"color:orange\">%1</span> <span style=\"color:%2\">").arg(dateTime, QColor(color).name()));
		for (const QChar &c : line) {
			static const QChar dot(0x2022);
			const ushort u = c.unicode();
			html.append((::iscntrl(u) && (u != '\t')) ? dot : c);
		}
		html.append(QSL("</span><br>\n"));
		m_currentOperation.output.append(html);
	}
	QScrollBar *sb    = ui->progressOutput->verticalScrollBar();
	const int   value = sb->value();
	const bool  isMax = sb->maximum() == value;
	ui->progressOutput->setHtml(m_currentOperation.output);
	sb->setValue(isMax ? sb->maximum() : value);
	ui->progressOutput->setEnabled(true);//chm

}

//----------------------------------------------------------------------------------------------------------------------------------
void ProgressWidget::operationProgress(const double progress) {
	m_currentOperation.progress = progress;
	ui->progress->setValue(calculateProgressValue(m_currentOperation));
}

//----------------------------------------------------------------------------------------------------------------------------------
void ProgressWidget::operationTick() {
	uint64_t seconds   = m_currentOperationStartTime.msecsTo(QDateTime::currentDateTime()) / 1000;
	const int hours    = seconds / 3600;
	seconds           -= hours   * 3600;
	const int minutes  = seconds / 60;
	seconds           -= minutes * 60;

	static const QChar zero('0');
	m_currentOperation.elapsedTime = QSL("%1:%2:%3").arg(hours, 2, 10, zero).arg(minutes, 2, 10, zero).arg(seconds, 2, 10, zero);
	ui->elapsedTime->setText(m_currentOperation.elapsedTime);
}

//----------------------------------------------------------------------------------------------------------------------------------
bool ProgressWidget::running() const {
    return (m_valid8Worker || false) ? true : false;
}

//----------------------------------------------------------------------------------------------------------------------------------
void ProgressWidget::setOutput(const QString &output) {
	ui->progressOutput->setHtml(output);
	QScrollBar *sb = ui->progressOutput->verticalScrollBar();
	sb->setValue(sb->maximum());
}
