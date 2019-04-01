/*-------------------------------------------------------------------------------

  Multi-Speak - Secure Protocol Enterprise Access Kit(MS_SPEAK)
  Copyright © 2018, Battelle Memorial Institute
  All rights reserved.
  1.	Battelle Memorial Institute (hereinafter Battelle) hereby grants permission to any person or
		entity lawfully obtaining a copy of this software and associated documentation files
		(hereinafter “the Software”) to redistribute and use the Software in source and binary forms,
		with or without modification.  Such person or entity may use, copy, modify, merge, publish,
		distribute, sublicense, and/or sell copies of the Software, and may permit others to do so,
		subject to the following conditions:
		•	Redistributions of source code must retain the above copyright notice, this list of
			conditions and the following disclaimers.
		•	Redistributions in binary form must reproduce the above copyright notice, this list of
			conditions and the following disclaimer in the documentation and/or other materials
			provided with the distribution.
		•	Other than as used herein, neither the name Battelle Memorial Institute or Battelle may
			be used in any form whatsoever without the express written consent of Battelle.

  2.	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
		OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
		AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BATTELLE OR CONTRIBUTORS
		BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
		(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
		OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
		CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
		OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


  This material was prepared as an account of work sponsored by an agency of the United States Government.
  Neither the United States  Government nor the United States Department of Energy, nor Battelle, nor
  any of their employees, nor any jurisdiction or organization  that has cooperated in the development
  of these materials, makes any warranty, express or implied, or assumes any legal liability or
  responsibility for the accuracy, completeness, or usefulness or any information, apparatus, product,
  software, or process disclosed, or represents that its use would not infringe privately owned rights.
  Reference herein to any specific commercial product, process, or service by trade name, trademark,
  manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or
  favoring by the United States Government or any agency thereof, or Battelle Memorial Institute. The
  views and opinions of authors expressed herein do not necessarily state or reflect those of the
  United States Government or any agency thereof.
									 PACIFIC NORTHWEST NATIONAL LABORATORY
											    operated by
												  BATTELLE
											      for the
									  UNITED STATES DEPARTMENT OF ENERGY
									   under Contract DE-AC05-76RL01830


    This notice including this sentence must appear on any copies of this computer software.
*/
//-------------------------------------------------------------------------------
//	History
//		2018 - Created By: Carl Miller <carl.miller@pnnl.gov>
//-------------------------------------------------------------------------------
//
// Summary: ProgressWidget.cpp
//-------------------------------------------------------------------------------

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
#include "Valid8.h"
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
void ProgressWidget::valid8Xml(QString s, QString cp, QString e, QString x )
{
	m_valid8Worker = new Valid8Worker( s, cp, e, x );
	QThread *thread      = new QThread;
    m_valid8Worker->moveToThread(thread);
    connect(m_valid8Worker, &Valid8Worker::finished, thread, &QThread::quit);
    connect(m_valid8Worker, &Valid8Worker::finished, this,   &ProgressWidget::valid8XmlFinished);
    connect(m_valid8Worker, &Valid8Worker::finishedi, this,   &ProgressWidget::valid8XmlFinishedi);
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
void ProgressWidget::valid8XmlFinishedi(const int iExitCode )
{
	QString msg = "Validation ";
	
	switch (iExitCode) 
	{
		case (int)JReturns::EXCEPTION:
			msg += "EXCEPTION";
			break;
		case (int)JReturns::VALID8_FAIL:
			msg += "VALID8_FAIL";
			break;
		case (int)JReturns::INITXSD_FAIL:
		{
			QMessageBox messageBox;
			QString EndPoint = m_valid8Worker->m_EndPoint;
			QString SchemaRoot=m_valid8Worker->m_SchemaRoot;
			QString err=QString("'%1' Components Could Not Be Located.\n").arg(SchemaRoot);
			QString dirs = "\nSchema Path Hierarchy must be similar to '<path>/EndPoints'\n";
			QString ep = QString( "    where <path>/EndPoints contains: %1/%2.wsdl and %3.xsd\n").arg(EndPoint).arg(EndPoint).arg(EndPoint);
			dirs += ep+ "    and <path>/xsd contains *.xsd";
			dirs += "\n    (specify the location of <path>/EndPoints)";
			err += dirs;
			messageBox.critical (Q_NULLPTR,"\nSchema Root Path Not Found", err );
			msg += "INITXSD_FAIL";
			break;
		}
		case (int)JReturns::INIT_FAIL:
			msg += "INITXSD_FAIL";
			break;
		case (int)JReturns::FAIL:
			msg += "FAIL";
			break;
		case (int)JReturns::SUCCESS:
			msg += "SUCCESS";
			break;
	}
	valid8XmlFinished( msg );
}

//----------------------------------------------------------------------------------------------------------------------------------
void ProgressWidget::valid8XmlFinished(const QString &msg)
{
	m_currentOperationTimer->stop();
    m_valid8Worker = nullptr;
	operationTick();
	operationLog(QSL("%1 after %2").arg(msg, ui->elapsedTime->text()), Qt::white);
	emit valid8Done(msg);
	//qDebug() << "valid8XmlFinished: " << msg;
}

//----------------------------------------------------------------------------------------------------------------------------------
int ProgressWidget::calculateProgressValue(const OperationInfo &operationInfo)
{
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
