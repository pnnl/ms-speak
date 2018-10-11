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
 | Date:                     20180730                            |
 | Guidance (if applicable): Client Correspondence               |
 *---------------------------------------------------------------*/

//----------------------------------------------------------------------------------------------------------------------------------
// Copyright (c) 2013-2018, Pacific Northwest National Laboratory
// This software is subject to copyright protection under the laws of the United States and other countries
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//----------------------------------------------------------------------------------------------------------------------------------

#ifndef AUTHORDEVICEWORKER_H
#define AUTHORDEVICEWORKER_H

#include <QHash>
#include <QTemporaryDir>
#include <QVector>

#include "Status.h"

class Firmware;
class Process;
class QTimer;

//----------------------------------------------------------------------------------------------------------------------------------
class Valid8Worker : public QObject {
	Q_OBJECT
public:
	explicit Valid8Worker(QString s, QString e, QString x);

	void cancel();
	bool start();

signals:
	void finished(const QString &msg);
	void log(const QString &msg, const Qt::GlobalColor color);
	void progress(const double progress);

private:
	enum class StageType {
        CheckVersion,
        Validate     // Validate XML against schema(s)
	};

	struct StageData {
		StageType type;           // Stage type
		uint64_t  ms{0};          // Approximate number of milliseconds to complete stage
		double    percent{0.0};   // Percentage of total progress allocated to this stage
	};

	void    addStage(const StageType type);
    bool    doCheckVersion();
    bool    doValidate();
    bool    error(const QString &msg);
	bool    initProgress();
	QString msToTimeEstimate(const quint64 ms) const;
	bool    nextStage();
	bool    processFinished();
	void    sleep(const int secs);
	bool    stop(const Status status);
	void    timeout();
	void    updateProgress();

	Process                 *m_Process{nullptr};       // Process to run
	double                   m_progressPrevStage{0.0}; // Progress when the previous stage completed
	uint8_t                  m_provisionLun{0};        // LUN to provision
	int                      m_stageIndex{-1};         // Index of the current processing stage
	uint64_t                 m_stageMs{0};             // Number of milliseconds the current stage has run
	QVector<StageData>       m_stages;                 // Processing stages for the selected operation
	Status                   m_status{Status::Ready};  // Operation status
	QTimer                  *m_timer{nullptr};         // Status check and progress update timer
	QString m_SchemaRoot;
	QString m_EndPoint;
	QString m_XmlFilename;
};

#endif // AUTHORDEVICEWORKER_H
