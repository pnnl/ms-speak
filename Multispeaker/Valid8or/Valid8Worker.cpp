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
 | Date:                     20180810                            |
 | Guidance (if applicable): Client Correspondence               |
 *---------------------------------------------------------------*/

//----------------------------------------------------------------------------------------------------------------------------------
// Copyright (c) 2013-2018, Pacific Northwest National Laboratory
// This software is subject to copyright protection under the laws of the United States and other countries
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//----------------------------------------------------------------------------------------------------------------------------------

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
