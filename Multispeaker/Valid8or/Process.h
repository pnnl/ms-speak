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

#ifndef PROCESS_H
#define PROCESS_H

#include <QProcess>
#include <QStringList>

#include "Status.h"

//----------------------------------------------------------------------------------------------------------------------------------
class Process : public QObject {
	Q_OBJECT
public:
	explicit Process(QObject *parent = nullptr);

	static int execute(const QString &name, QString &output);
	static int execute(const QString &name, const QStringList &args);
	static int execute(const QString &name, const QStringList &args, QString &output);

	int    exitCode() const { return m_exitCode; }
	void   start(const QString &name, const QStringList &args);
	void   setEnv(const QString &name, const QString &arg);
	Status status() const { return m_status; }
	bool   terminate();

signals:
	void finished();
	void log(const QString &msg, const Qt::GlobalColor color);

private:
	void processFinished(int exitCode, QProcess::ExitStatus exitStatus);

	int       m_exitCode{0};           // Process exit code
	QProcess *m_process{nullptr};      // Process object
	Status    m_status{Status::Ready}; // Process status
};

#endif // PROCESS_H
