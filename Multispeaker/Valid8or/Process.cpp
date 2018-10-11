/*------------------------------------------------------------*
 |                  OFFICIAL USE ONLY                         |
 | May be exempt from public release under the Freedom of     |
 | Information Act (5 U.S.C 552), exemption number and        |
 | category:                                                  |
 |                                                            |
 | Exemptions 3, 5, 7                                         |
 |                                                            |
 | Department of Energy review required before public release |
 |                                                            |
 | Name / Org:  Wayne Meitzler / D7P25                        |
 | Date:        July 2018                                     |
 |                                                            |
 | Guidance (if applicable) Client Correspondence             |
 *------------------------------------------------------------*/

//----------------------------------------------------------------------------------------------------------------------------------
// Copyright (c) 2013-2018, Pacific Northwest National Laboratory
// This software is subject to copyright protection under the laws of the United States and other countries
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//----------------------------------------------------------------------------------------------------------------------------------

#include <QDateTime>
#include <QtGlobal>
#include <QDebug>

#include "Process.h"
#include "QSL.h"

//----------------------------------------------------------------------------------------------------------------------------------
Process::Process(QObject *parent)
	: QObject{parent}
{
}

//----------------------------------------------------------------------------------------------------------------------------------
int Process::execute(const QString &name, QString &output) {
	QStringList args;
	return execute(name, args, output);
}

//----------------------------------------------------------------------------------------------------------------------------------
int Process::execute(const QString &name, const QStringList &args) {
	QString output;
	return execute(name, args, output);
}

//----------------------------------------------------------------------------------------------------------------------------------
int Process::execute(const QString &name, const QStringList &args, QString &output) {
	// Don't use QProcess::execute(), since it can print the command output to the console
	int      exitCode = -2;
	QProcess proc;
	if (args.isEmpty()) {
		proc.start(name, QIODevice::ReadOnly);
	} else {
		proc.start(name, args, QIODevice::ReadOnly);
	}
	if (proc.waitForStarted() && proc.waitForFinished()) {
		if (proc.exitStatus() == QProcess::NormalExit) {
			output   = proc.readAllStandardOutput() + proc.readAllStandardError();
			exitCode = proc.exitCode();
		} else {
			exitCode = -1;
		}
	}
	return exitCode;
}

//----------------------------------------------------------------------------------------------------------------------------------
void Process::setEnv(const QString &name, const QString &arg) {
	//emit log(QString("Setting Environment Variable %1 to %2").arg(name, arg), Qt::yellow);

	QByteArray nameBytes;
	nameBytes = name.toUtf8();
	const char *pEnv = nameBytes.constData();// toStdString().c_str();// convert QString to char *, using this ,
		// and qDebug() << name << "is NOT set." ends up clearing pEnv somehow....

	QByteArray argBytes;
	argBytes = arg.toUtf8();
	if( !qputenv( pEnv, argBytes ) ){
		qDebug( "Error putting env.");
	}

	QProcessEnvironment env = QProcessEnvironment::systemEnvironment();
	env.insert(name, arg); // Add an environment variable
	m_process->setProcessEnvironment(env);

}

//----------------------------------------------------------------------------------------------------------------------------------
void Process::start(const QString &name, const QStringList &args) {
	emit log(QString("%1 %2").arg(name, args.join(' ')), Qt::yellow);

	delete m_process;
	m_status  = Status::Running;
	m_process = new QProcess(this);

	// In order to use the new connect syntax, we need to disambiguate the QProcess::finished pointer
	void (QProcess:: *finishedSignal)(int exitCode, QProcess::ExitStatus exitStatus) = &QProcess::finished;
	connect(m_process, &QProcess::readyReadStandardError,  [this]() { emit log(m_process->readAllStandardError(),  Qt::white); });
	connect(m_process, &QProcess::readyReadStandardOutput, [this]() { emit log(m_process->readAllStandardOutput(), Qt::white); });
	connect(m_process, finishedSignal,                     this, &Process::processFinished);

	//setEnv("CLASSPATH", "/home/carl/MS-SPEAK/repo/Multispeaker/Valid8or/java/bin");

	m_process->setProgram(name);
	if( !args.isEmpty() )
		m_process->setArguments(args);
	m_process->start(QIODevice::Unbuffered | QIODevice::ReadOnly);
	//m_process->start(name, args, QIODevice::Unbuffered | QIODevice::ReadOnly);
	if (!m_process->waitForStarted()) {
		m_status = Status::Crashed;
		emit log(QSL("Cannot start %1").arg(name), Qt::red);
		emit finished();
	}
}

//----------------------------------------------------------------------------------------------------------------------------------
void Process::processFinished(int exitCode, QProcess::ExitStatus exitStatus) {
	m_exitCode = exitCode;
	if (m_status == Status::Running) {
		switch (exitStatus)
		{
			case QProcess::NormalExit:
				m_status = (exitCode == EXIT_SUCCESS) ? Status::Successful : Status::Failed;
				break;
			case QProcess::CrashExit:
				m_status = Status::Crashed;
				break;
			}
	}
	emit log(m_process->readAllStandardError(),  Qt::white);
	emit log(m_process->readAllStandardOutput(), Qt::white);

	emit log(QSL("Exited with Code %1").arg(exitCode), Qt::blue);

	emit finished();
}

//----------------------------------------------------------------------------------------------------------------------------------
bool Process::terminate() {
	if (m_process && (m_process->state() == QProcess::Running)) {
		m_status = Status::Canceled;
		m_process->terminate();
		if (!m_process->waitForFinished(5000)) {
			m_process->kill();
		}
		return true;
	}
	return false;
}
