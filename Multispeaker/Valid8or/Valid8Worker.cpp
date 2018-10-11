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
// Summary: Valid8Worker.cpp
//-------------------------------------------------------------------------------

#include "Valid8Worker.h"

#include <QApplication>
#include <QThread>
#include <QTime>
#include <QTimer>

#include "Process.h"
#include "QSL.h"
#include "Valid8.h"

//----------------------------------------------------------------------------------------------------------------------------------
Valid8Worker::Valid8Worker( QString s, QString e, QString x ) :
		m_SchemaRoot(s),
		m_EndPoint(e),
		m_XmlFilename(x)
{
	qRegisterMetaType<Qt::GlobalColor>("Qt::GlobalColor");
	qRegisterMetaType<uint64_t>("uint64_t");

	m_Process = new Process(this);
	m_timer   = new QTimer(this);
	m_timer->setInterval(1000);

	connect(m_Process, &Process::finished, this, &Valid8Worker::processFinished);
	connect(m_Process, &Process::log,      this, &Valid8Worker::log);
	connect(m_timer,   &QTimer::timeout,   this, &Valid8Worker::timeout);
}

//----------------------------------------------------------------------------------------------------------------------------------
void Valid8Worker::addStage(const StageType type) {
	struct StageData stageData;
	stageData.type = type;
	m_stages.append(stageData);
}

//----------------------------------------------------------------------------------------------------------------------------------
void Valid8Worker::cancel() {
	m_status = Status::Canceled;
}

//----------------------------------------------------------------------------------------------------------------------------------
bool Valid8Worker::doCheckVersion() {
	const StageData &stageData(m_stages[m_stageIndex]);
	emit log(QSL("Querying Java (%1)").arg(msToTimeEstimate(stageData.ms)), Qt::white);

	// Build command arguments and run command
	static const QString runJ(QSL("%1").arg("java"));
	QStringList args{ QSL("-version") };
	/*
	static const QString runJ(QSL("%1").arg("ls"));
	QStringList args{ QSL("-al") };
	args.append("/home/carl/h.py");// *.py")); for some reason, the '*' causes it to fail
	*/
	m_Process->start(runJ, args);
	return true;
}

//----------------------------------------------------------------------------------------------------------------------------------
bool Valid8Worker::doValidate() {
	const StageData &stageData(m_stages[m_stageIndex]);
	emit log(QSL("Running JRun (%1)").arg(msToTimeEstimate(stageData.ms)), Qt::white);

	QString Jarlib = qApp->applicationDirPath();// "/home/carl/MS-SPEAK/repo/Multispeaker/Debug/run"

	// Build command arguments and run command
	static const QString runJ(QSL("%1").arg("java"));
	QStringList args{ QSL("-cp") };
	args.append(QSL("%1/*").arg(Jarlib));
	args.append(QSL("JRun"));
	args.append(QSL("-sd"));
	args.append(QSL("%1").arg(m_SchemaRoot));
	args.append(QSL("-ep"));
	args.append(QSL("%1").arg(m_EndPoint));
	args.append(QSL("-xf"));
	args.append(QSL("%1").arg(m_XmlFilename));
	args.append(QSL("-v"));
	args.append(QSL("%1").arg(3));

	m_Process->start(runJ, args);
	return true;
}

//----------------------------------------------------------------------------------------------------------------------------------
bool Valid8Worker::error(const QString &msg) {
	emit log(msg, Qt::red);
	return stop(Status::Failed);
}

//----------------------------------------------------------------------------------------------------------------------------------
bool Valid8Worker::initProgress() {

	// Calculate approximate time for each stage to complete
	double totalMS = 0.0;
	for (StageData &stageData : m_stages) {
		switch (stageData.type) {
            case StageType::CheckVersion:
                stageData.ms = 2000;
				break;
            case StageType::Validate: {
				stageData.ms = 4000;
				break;
			}
        }
		totalMS += stageData.ms;
	}
	emit progress(0.0);//chm

	// Calculate percentage of total time for each stage
	for (StageData &stageData : m_stages) {
		stageData.percent = static_cast<double>(stageData.ms) / totalMS;
	}
	return true;
}

//----------------------------------------------------------------------------------------------------------------------------------
QString Valid8Worker::msToTimeEstimate(const quint64 ms) const {
	// If five minutes or less, round up to nearest minute
	// If fifteen minutes or less, round up to nearest five minutes
	// If over fifteen minutes, round up to nearest fifteen minutes

	uint32_t granularity;
	if      (ms <= 300000) { granularity =  1; }
	else if (ms <= 900000) { granularity =  5; }
	else                   { granularity = 15; }

	const uint32_t granularityMS = granularity * 60000;
	uint32_t       hours         = 0;
	uint32_t       minutes       = (ms / granularityMS) * granularity;
	if (ms % granularityMS) {
		minutes += granularity;
	}

	if (minutes > 60) {
		hours    = minutes / 60;
		minutes %= 60;
	} else if (minutes == 0) {
		minutes = 1;
	}

	QString estimate(QSL("about"));
	if (hours) {
		if (hours == 1) {
			estimate.append(QSL(" 1 hour"));
		} else {
			estimate.append(QSL(" %1 hours").arg(hours));
		}
	}
	if (minutes) {
		if (minutes == 1) {
			estimate.append(QSL(" 1 minute"));
		} else {
			estimate.append(QSL(" %1 minutes").arg(minutes));
		}
	}
	return estimate;
}

//----------------------------------------------------------------------------------------------------------------------------------
bool Valid8Worker::nextStage() {
	if (m_stageIndex >= 0) {
		m_progressPrevStage += m_stages[m_stageIndex].percent;
	}
	m_stageMs = 0;
	m_stageIndex++;
	if (m_stageIndex >= m_stages.size()) {
		return stop(Status::Successful);
	}

	bool rc = false;
	switch (m_stages[m_stageIndex].type) {
		case StageType::CheckVersion:
			rc = doCheckVersion();
			break;
		case StageType::Validate:
			rc = doValidate();
			break;
	}
	return rc ? true : stop(Status::Failed);
}

//----------------------------------------------------------------------------------------------------------------------------------
bool Valid8Worker::processFinished() {
	switch (m_Process->status())
	{
		case Status::Failed:
		case Status::Crashed:
		case Status::Canceled:
			return stop(m_Process->status());
		default:
			break;
	}
	return nextStage();
}

//----------------------------------------------------------------------------------------------------------------------------------
void Valid8Worker::sleep(const int secs) {
	static const int granularity = 100;
	const int        msecs       = secs * 1000;
	for (int i = 0; i < msecs; i += granularity) {
		QApplication::processEvents();
		QThread::msleep(granularity);
	}
}

//----------------------------------------------------------------------------------------------------------------------------------
bool Valid8Worker::start() {
	m_status = Status::Running;
	m_timer->start();

	//addStage(StageType::CheckVersion);
    addStage(StageType::Validate);

	if (!initProgress()) {
		return stop(Status::Failed);
	}

	return nextStage();
}

//----------------------------------------------------------------------------------------------------------------------------------
bool Valid8Worker::stop(const Status status) {
	if (!m_timer->isActive()) {
		return m_status == Status::Successful;
	}

	m_status = status;
	m_timer->stop();
	bool rc = false;

	int ret = m_Process->exitCode();
	//qDebug() << "stop: ret: " << ret;
	switch (ret) {
		case (int)JReturns::EXCEPTION:
			emit finished(QSL("Validation EXCEPTION"));
			break;
		case (int)JReturns::VALID8_FAIL:
			emit finished(QSL("Validation VALID8_FAIL"));
			break;
		case (int)JReturns::INITXSD_FAIL:
			emit finished(QSL("Validation INITXSD_FAIL"));
			break;
		case (int)JReturns::INIT_FAIL:
			emit finished(QSL("Validation INIT_FAIL"));
			break;
		case (int)JReturns::FAIL:
			emit finished(QSL("Validation FAIL"));
			break;
		case (int)JReturns::SUCCESS:
			rc = true;
			emit progress(1.0);
			emit finished(QSL("Validation SUCCESS"));
			break;
	}

	/*qDebug() << "stop: m_status:";
	switch (m_status) {
		case Status::Successful:
			rc = true;
			emit progress(1.0);
            emit finished(QSL("Validation finished"));
			break;
		case Status::Failed:
		case Status::Crashed:
            emit finished(QSL("Validation failed"));
			break;
		case Status::Canceled:
            emit finished(QSL("Validation canceled"));
			break;
		default:
			break;
	}*/
	return rc;
}

//----------------------------------------------------------------------------------------------------------------------------------
void Valid8Worker::timeout() {
	StageData &stageData(m_stages[m_stageIndex]);
	m_stageMs += m_timer->interval();

	if (m_status == Status::Canceled) {
		if (!m_Process->terminate()) {
			stop(m_status); // No running process to terminate
		}
    } else if (stageData.type == StageType::Validate){
        emit log(QSL("Validating XML File"), Qt::white);
		sleep(1);
		emit progress(m_progressPrevStage + stageData.percent);
	} else if (m_stageMs < stageData.ms) {
		emit progress(m_progressPrevStage + (static_cast<double>(m_stageMs) / static_cast<double>(stageData.ms) * stageData.percent));
	} else {
		emit progress(m_progressPrevStage + stageData.percent);
	}
}
