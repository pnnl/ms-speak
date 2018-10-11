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
// Summary: Process.cpp
//-------------------------------------------------------------------------------

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
