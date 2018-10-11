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

#ifndef PROGRESSWIDGET_H
#define PROGRESSWIDGET_H

#include <QDateTime>
#include <QWidget>

//----------------------------------------------------------------------------------------------------------------------------------
namespace Ui {
	class ProgressWidget;
}

class Valid8Worker;
class QStandardItem;
class QStandardItemModel;
class QTimer;

//----------------------------------------------------------------------------------------------------------------------------------
class ProgressWidget : public QWidget {
	Q_OBJECT

public:
	explicit ProgressWidget(QWidget *parent = nullptr);
	~ProgressWidget();

	bool    running() const;
	void    valid8Xml(QString s, QString e, QString x);

signals:
	void valid8Done(QString m);

private:
	struct OperationInfo {
		QString  output;        // Operation progress output
		QString  elapsedTime;   // Elapsed time
		double   progress{0.0}; // Current value for progress
	};

	void    valid8XmlFinished(const QString &msg);
	int     calculateProgressValue(const OperationInfo &operationInfo);
	void    operationLog(const QString &msg, const Qt::GlobalColor color);
	void    operationProgress(const double progress);
	void    operationTick();
	void    setOutput(const QString &output);

	Ui::ProgressWidget   *ui{nullptr};
    Valid8Worker         *m_valid8Worker{nullptr};			   // validate thread worker
	OperationInfo         m_currentOperation;                  // Current operation information
	QDateTime             m_currentOperationStartTime;         // Time the current operation started
	QTimer               *m_currentOperationTimer{nullptr};    // Timer to update current operation elapsed time
};

#endif // PROGRESSWIDGET_H
