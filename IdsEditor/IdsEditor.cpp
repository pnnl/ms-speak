/*-------------------------------------------------------------------------------

  Multi-Speak - Secure Protocol Enterprise Access Kit(MS_SPEAK)
  Copyright © 2021, Battelle Memorial Institute
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
//		2021 - Modified By: Carl Miller <carl.miller@pnnl.gov> from original by
//                  Lance Irvine, LMI Developments, LLC.
//		02.09.2021 CHM - Populate from Sqlite DB.
//-------------------------------------------------------------------------------
//
// Summary: IdsEditor.cpp
//-------------------------------------------------------------------------------

#include <QtWidgets>  // rid invalid use of incomplete type ‘....’
#include <QDesktopServices>
#include <QDir>
#include <QFileDialog>
#include <QMessageBox>
#include <QSettings>
#include <QStandardItem>
#include <QTextStream>
#include <QTimer>
#include <QToolBar>
#include <QToolButton>
#include <QSqlRecord>

#include "IdsEditor.h"
#include "IdsSettings.h"
#include "Rule.h"
#include "RuleConst.h"
#include "RuleEditor.h"
#include "TesterEditor.h"

bool CLEAR_SETTINGS_ON_EXIT = false; // Used for the clear settings shortcut feature (Ctrl+Shift+C)

//-------------------------------------------------------------------------------
// IdsEditor
//
IdsEditor::IdsEditor(QWidget* parent)
	: QMainWindow(parent),
	  m_clearSettingsShortcut(QKeySequence(QStringLiteral("Ctrl+Shift+C")), this, SLOT(OnClearSettings())),
	  m_dbFileName(QSettings().value(SK_DB_FILE_NAME, DB_FILE_NAME).toString()),
	  m_prompt( false )

{
	ui.setupUi(this);
	ui.cmbTesters->addItem("<new>", ROLE_NEW_TESTER_KEY);

	ui.DeleteBtn->setEnabled(false);
	ui.EditBtn->setEnabled(false);
	ui.NewBtn->setEnabled(false);
	ui.btnEditTester->setEnabled(false);
	ui.cmbTesters->setEnabled(false);
	//ui.cmbTesters->setEditable(false);

	setWindowTitle(QStringLiteral("IDS Editor %1").arg(SOFTWARE_VERSION));
	RestoreGeometry();

	ui.RulesTreeView->setModel(&m_RemObjModel);
	ui.RulesTreeView->setHeaderHidden(true);
	ui.RulesTreeView->setSelectionBehavior(QAbstractItemView::SelectRows);
	ui.RulesTreeView->setSelectionMode(QAbstractItemView::SingleSelection);
	ui.RulesTreeView->setEditTriggers(QAbstractItemView::NoEditTriggers);

	statusBar()->addWidget(&m_dbFileNameLabel);
	m_dbFileNameLabel.setText(QDir::toNativeSeparators(m_dbFileName));


	connect(ui.FileOpenAct, SIGNAL(triggered()), this, SLOT(OnFileOpen()));
	connect(ui.FileSaveAct, SIGNAL(triggered()), this, SLOT(OnFileSave()));
	connect(ui.HelpAboutAct, SIGNAL(triggered()), this, SLOT(OnAbout()));
	connect(ui.HelpAct, SIGNAL(triggered()), this, SLOT(OnHelp()));
	connect(ui.HelpLicensingAct, SIGNAL(triggered()), this, SLOT(OnAboutQt()));
	connect(ui.QuitAct, SIGNAL(triggered()), this, SLOT(OnQuit()));
	connect(ui.DeleteBtn, SIGNAL(clicked()), this, SLOT(OnRuleDelete()));
	connect(ui.EditBtn, SIGNAL(clicked()), this, SLOT(OnRuleEdit()));
	connect(ui.NewBtn, SIGNAL(clicked()), this, SLOT(OnRuleNew()));
	connect(ui.RulesTreeView, SIGNAL(doubleClicked(const QModelIndex&)), this, SLOT(OnRulesTreeViewDoubleClicked(const QModelIndex&)));
	connect(ui.cmbTesters, SIGNAL(currentIndexChanged(int)),this,SLOT(OnTesterSelectionChanged(int)));
	connect(ui.btnEditTester, SIGNAL(clicked()), this, SLOT(OnEditTester()));

	QTimer::singleShot(100, this, SLOT(OnRestoreState())); // Restore State after Docks Created
	QTimer::singleShot(100, this, SLOT(OnReadDbFile()));
	QTimer::singleShot(150, this, SLOT(OnInitCombo()));
}
//-------------------------------------------------------------------------------
// ~IdsEditor
//
IdsEditor::~IdsEditor()
{
	ClearHHash();
}

//-------------------------------------------------------------------------------
// ClearHHash
//
void IdsEditor::ClearHHash()
{
	REMOBJ_HHASH::iterator hitr;
	for( hitr = m_RemObjs.begin(); hitr != m_RemObjs.end(); ++hitr ){
		REMOBJ_HASH& h = hitr.value();
		qDeleteAll(h); // is the same as qDeleteAll(c.begin(), c.end()).
		h.clear();
	}
	//qDeleteAll(m_RemObjs);
	m_RemObjs.clear();
}

//------------------------------------------------------------------------------
// Edit
//
void IdsEditor::Edit(const QModelIndex& index)
{
	if( index.isValid())
	{
		if( index.data(ROLE_REM_KEY).isValid())
		{
			QString remKey = index.data(ROLE_REM_KEY).toString();
			REMOBJ_HASH& rRemObjs = RemObjects();
			if( RemObject* remObj = rRemObjs.value(remKey, Q_NULLPTR))
			{
				RuleEditor dlg(*remObj, this);
				if( QDialog::Accepted == dlg.exec())
				{
					if( remObj->Rem() == dlg.RemObj().Rem())
					{
						// Same Rem...so just copy
						remObj->Copy(dlg.RemObj());
					}
					else
					{
						// Different Rem so delete old one and add new one
						delete rRemObjs.take(remObj->Rem()); // Removes the item with the key from the hash and returns the value associated with it.
						remObj = new RemObject(dlg.RemObj());
						rRemObjs.insert(remObj->Rem(), remObj);
					}
					UpdateObjectModel();
				}
			}
		}
	}
}

//------------------------------------------------------------------------------
// ModelIndexByKeyAndRole
//
QModelIndex IdsEditor::ModelIndexByKeyAndRole(const QString& remObj, int role)
{
	QModelIndex idx;
	if( QStandardItem* item = m_RemObjModel.item(0))
		idx = item->index();

	QModelIndexList idxList = m_RemObjModel.match(idx, role, remObj, 1, Qt::MatchExactly | Qt::MatchRecursive | Qt::MatchWrap);
	if( idxList.count())
		return idxList.first();
	else
		return QModelIndex();
}

//------------------------------------------------------------------------------
// ReadDbFile
//
// https://doc.qt.io/qt-5/sql-programming.html
// https://doc.qt.io/qt-5/examples-sql.html
// By default, SQLite operates in auto-commit mode. It means that for each command,
// SQLite starts, processes, and commits the transaction automatically.
bool IdsEditor::ReadDbFile(const QString& fileName, QString& errStr)
{
	bool bRet = false;

	if( !fileName.isEmpty() ){
		// Create database connetion.
		m_db = QSqlDatabase::addDatabase("QSQLITE", "BizConn");
		if( !m_db.isValid() ){
			qDebug("Error occurred adding the database.");
			qDebug("%s.", qPrintable(m_db.lastError().text()));
			return bRet;
		}
		/*m_db.setHostName("acidalia");
		m_db.setDatabaseName("customdb");
		m_db.setUserName("mojito");
		m_db.setPassword("J0a1m8");*/
		m_db.setConnectOptions("QSQLITE_OPEN_READONLY");
		m_db.setDatabaseName(fileName);
		if( !m_db.open()){
			errStr = QStringLiteral("Error occurred opening the database: '%1'").arg(m_db.lastError().text());
			qDebug("%s", qPrintable(errStr));
			return bRet;
		}
		QSqlQuery query(m_db);
		/*query.prepare("INSERT INTO person (id, forename, surname) "
					  "VALUES (:id, :forename, :surname)");
		query.bindValue(":id", 1001);
		query.bindValue(":forename", "Bart");
		query.bindValue(":surname", "Simpson");*/
		/* Insert row.
		query.prepare("INSERT INTO test VALUES (null, ?)");
		query.addBindValue("Some text");
		if( !query.exec()){
			qDebug("Error occurred inserting.");
			qDebug("%s.", qPrintable(m_db.lastError().text()));
			return bRet;
		}
		// Insert row.
		query.prepare("INSERT INTO test VALUES (null, ?)");
		query.addBindValue("Some text");
		if( !query.exec()){
			qDebug("Error occurred inserting.");
			qDebug("%s.", qPrintable(m_db.lastError().text()));
			return bRet;
		}
		*/

		// Query.
		QString strQuery = QStringLiteral(
		"SELECT functions.name as Function, endpoints.name as EndPoint, methods.name as Method"
		" FROM Functions"
		" INNER JOIN endpoints ON endpoints.Function = Functions.id"
		" INNER JOIN methods ON methods.EndPoint = endpoints.id"
		" ORDER BY Function, EndPoint, Method;"
		);

		query.prepare(strQuery);
		if( !query.exec() ){
			errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
			qDebug("%s", qPrintable(errStr));
			//qDebug("%s.", qPrintable(query.lastError().text()));
			m_db.close();
			return bRet;
		}

		QString fn;
		QString ep;
		QString me;
		// iQSqlQuery q("select * from employees");
		// iQSqlRecord rec = q.record();
		// iqDebug() << "Number of columns: " << rec.count();
		// int nameCol = rec.indexOf("name"); // index of the field "name"
		while( query.next() ){
			fn =  query.value(0).toString();
			ep =  query.value(1).toString();
			me =  query.value(2).toString();
			//qDebug() << "Function: " << fn << ", Endpoint: " << ep << ", Method: " << me;
			if( !m_functions[fn].contains(ep) )
				m_functions[fn].append(ep);
			if( !m_methods[ep].contains(me) )
				m_methods[ep].append(me);
		}
		strQuery = QStringLiteral("SELECT %1 FROM %2").arg("*", DB_TABLE_TESTERS );
		query.prepare(strQuery);
		if( !query.exec()){
			errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
			qDebug("%s", qPrintable(errStr));
			m_db.close();
			return bRet;
		}
		QString tester;
		while( query.next() ){
			tester =  query.value(1).toString();
			//qDebug() << "Tester: " << tester;
			ui.cmbTesters->insertItem(0, tester, ROLE_TESTER_KEY);
			m_origs << tester;
		}
		ui.cmbTesters->setCurrentIndex(0);

		bRet = LoadRules( m_db,errStr );
		m_db.close();
		UpdateObjectModel();
	}
	//QSqlDatabase::removeDatabase("BizConn");
	return bRet;
}
//------------------------------------------------------------------------------
// LoadRules
//
bool IdsEditor::LoadRules( QSqlDatabase& db, QString& errStr )
{
	bool bRet = false;

	ClearHHash();

	QSqlQuery query(db);
	// Query.
	// == Number of Rules ==
	QString strQuery = QStringLiteral(
	"SELECT COUNT(*) as count"
	" FROM rules"
	" INNER JOIN endpoints ON endpoints.id = rules.endpoint"
	" INNER JOIN methods ON methods.id = rules.method"
	" INNER JOIN testers ON testers.id = rules.Tester;"
	);

	query.prepare(strQuery);
	if( !query.exec() ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		//qDebug("%s.", qPrintable(m_db.lastError().text()));
		return bRet;
	}
	QSqlRecord rec = query.record();
	if( rec.isEmpty() ){
		errStr = QStringLiteral("isEmpty Error occurred querying.");
		qDebug("%s", qPrintable(errStr));
		return bRet;
	}
	QVariant qvRecval = rec.value( "count" );
	if( !qvRecval.isValid() ){
		errStr = QStringLiteral("Invalid record value for 'count'.");
		qDebug("%s", qPrintable(errStr));
		return bRet;
	}
	query.next();
	int cntCol = rec.indexOf("count");
	int numRules = query.value(cntCol).toInt();
	if( numRules == 0 ){
		qDebug("No Rules Defined.");
		return true;
	}
	// == All Rules ==
	strQuery = QStringLiteral(
	"SELECT testers.Name as who, endpoints.name as EndPoint, methods.name as Method,"
	" rules.maxTemp,rules.minTemp,rules.maxHour,rules.minHour,rules.numReq,rules.numRPH,rules.email"
	" FROM rules"
	" INNER JOIN endpoints ON endpoints.id = rules.endpoint"
	" INNER JOIN methods ON methods.id = rules.method"
	" INNER JOIN testers ON testers.id = rules.tester"
	" ORDER BY who;"
	);
	query.prepare(strQuery);
	if( !query.exec() ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		return bRet;
	}
	while( query.next() ){
		QString Tester =  query.value(0).toString();
		QString EndPoint =  query.value(1).toString();
		QString Method =  query.value(2).toString();
		QString maxTemp =  query.value(3).toString();
		QString minTemp =  query.value(4).toString();
		QString maxHour =  query.value(5).toString();
		QString minHour =  query.value(6).toString();
		QString numReq =  query.value(7).toString();
		QString numRPH =  query.value(8).toString();
		QString email =  query.value(9).toString();
		/*
		qDebug() << Tester;
		qDebug() << "   " << EndPoint << "::" << Method;
		qDebug() << "   " << maxTemp << "  " << minTemp << maxHour << "  " << minHour;
		qDebug() << "   " << numReq << "  " << numRPH << email;*/

		QString remKey = QStringLiteral("%1::%2").arg(EndPoint, Method);
		REMOBJ_HASH& rRemObjs = m_RemObjs[Tester];
		rRemObjs.insert(remKey, new RemObject());
		RemObject *pRemObj = rRemObjs[remKey];
		pRemObj->m_EndPoint = EndPoint;
		pRemObj->m_Method = Method;
		pRemObj->Rules.insert(RULE_TYPE_TEMP_RANGE, new Rule());
		if( Rule* rule = pRemObj->Rules.value(RULE_TYPE_TEMP_RANGE, Q_NULLPTR))
		{
			rule->Name = RULE_TYPE_TEMP_RANGE;
			rule->KeyValue.insert(RULE_KEY_MAXTEMP, maxTemp);
			rule->KeyValue.insert(RULE_KEY_MINTEMP, minTemp);
		}
		pRemObj->Rules.insert(RULE_TYPE_TIME_RANGE, new Rule());
		if( Rule* rule = pRemObj->Rules.value(RULE_TYPE_TIME_RANGE, Q_NULLPTR))
		{
			rule->Name = RULE_TYPE_TIME_RANGE;
			rule->KeyValue.insert(RULE_KEY_MAXTIME, maxHour);
			rule->KeyValue.insert(RULE_KEY_MINTIME, minHour);
		}
		pRemObj->Rules.insert(RULE_TYPE_MAX_VALUE, new Rule());
		if( Rule* rule = pRemObj->Rules.value(RULE_TYPE_MAX_VALUE, Q_NULLPTR))
		{
			rule->Name = RULE_TYPE_MAX_VALUE;
			rule->KeyValue.insert(RULE_KEY_NUMREQ, numReq);
			rule->KeyValue.insert(RULE_KEY_NUMRPH, numRPH);
		}
		pRemObj->Rules.insert(RULE_TYPE_MAX_VALUE, new Rule());
		if( Rule* rule = pRemObj->Rules.value(RULE_TYPE_MAX_VALUE, Q_NULLPTR))
		{
			rule->Name = RULE_TYPE_EMAIL;
			rule->KeyValue.insert(RULE_KEY_EMAIL, email);
		}
	}

	UpdateObjectModel();
	bRet = true;
	return bRet;
}

//------------------------------------------------------------------------------
// InitCombo
//
void IdsEditor::InitCombo(void)
{
	/* The idea of 'hosts' was that all rules to be enforced in ICAP based on
	 * specific IPs. By default, rules are created for the broadcast IP and will
	 * be applied to all IPs icap sees unless the IP exists within the DB, then
	 * any rules for the IP will take precedence.
	 * When icap see an IP if there is no rule associated with
	 * that IP it is accepted.
	 */
	ui.cmbTesters->setEditable(true);
	ui.cmbTesters->setMinimumWidth(150);
	ui.cmbTesters->lineEdit()->setAlignment(Qt::AlignCenter);
	//ui.cmbHosts->lineEdit()->setInputMask( "000.000.000.000" );
}

//------------------------------------------------------------------------------
// RestoreGeometry
//
void IdsEditor::RestoreGeometry()
{
	restoreGeometry(QSettings().value(SK_MAIN_GEOMETRY).toByteArray());
}

//------------------------------------------------------------------------------
// RestoreState
//
void IdsEditor::RestoreState()
{
	restoreState(QSettings().value(SK_MAIN_STATE).toByteArray());
}

//------------------------------------------------------------------------------
// RuleItem
//
QStandardItem* IdsEditor::RuleItem(const QString& ruleKey)
{
	return m_RemObjModel.itemFromIndex(ModelIndexByKeyAndRole(ruleKey, ROLE_RULE_KEY));
}

//------------------------------------------------------------------------------
// SaveGeometry
//
void IdsEditor::SaveGeometry()
{
	QSettings().setValue(SK_MAIN_GEOMETRY, saveGeometry());
}

//------------------------------------------------------------------------------
// SaveState
//
void IdsEditor::SaveState()
{
	QSettings().setValue(SK_MAIN_STATE, saveState());
}

//------------------------------------------------------------------------------
// RemItem
//
QStandardItem* IdsEditor::RemItem(const QString& ruleKey)
{
	return m_RemObjModel.itemFromIndex(ModelIndexByKeyAndRole(ruleKey, ROLE_REM_KEY));
}

//------------------------------------------------------------------------------
// UpdateObjectModel
//
void IdsEditor::UpdateObjectModel()
{
	m_RemObjModel.clear();

	REMOBJ_HASH& rRemObjs = RemObjects();
	for (RemObject* remObj : rRemObjs)
	{
		QStandardItem* RemItem = new QStandardItem(remObj->Rem());
		RemItem->setData(remObj->Rem(), ROLE_REM_KEY);
		m_RemObjModel.appendRow(RemItem);
		for (Rule* rule : remObj->Rules)
		{
			QStandardItem* ruleItem = new QStandardItem(rule->ToString());
			ruleItem->setData(remObj->Rem(), ROLE_REM_KEY);
			ruleItem->setData(rule->ToString(), ROLE_RULE_KEY);
			RemItem->appendRow(ruleItem);
		}
	}
}

//------------------------------------------------------------------------------
// OnAbout
//
void IdsEditor::OnAbout()
{
	QMessageBox::about(this, QStringLiteral("IDS Editor"), SOFTWARE_ABOUT);
}

//------------------------------------------------------------------------------
// OnAboutQt
//
void IdsEditor::OnAboutQt()
{
	QMessageBox::aboutQt(this, QStringLiteral("Qt License"));
}

//------------------------------------------------------------------------------
// OnClearSettings
//
void IdsEditor::OnClearSettings()
{
	if( QMessageBox::Ok == QMessageBox::question(this, QStringLiteral("Clear Settings"),
												 QStringLiteral("All the Settings for Windows Sizes and Docking positions will be reset on exit of application."), QMessageBox::Ok | QMessageBox::Cancel))
	{
		CLEAR_SETTINGS_ON_EXIT = true;
	}
}

//------------------------------------------------------------------------------
// OnFileOpen
//
void IdsEditor::OnFileOpen()
{
	if( m_prompt ){
		QString fileName = QFileDialog::getOpenFileName(this, QStringLiteral("Business Rules Database"),
														m_dbFileName, QStringLiteral("Sqlite DB File (*.db)"));
		if( fileName.isEmpty())
			return;
		m_dbFileName = fileName;
	}
	QString err;
	if( ReadDbFile(m_dbFileName, err) ){
		UpdateObjectModel();
		QSettings().setValue(SK_DB_FILE_NAME, m_dbFileName);
		m_dbFileNameLabel.setText(QDir::toNativeSeparators(m_dbFileName));
		ui.btnEditTester->setEnabled(true);
		ui.cmbTesters->setEnabled(true);


	}
	else{
		ui.btnEditTester->setEnabled(false);
		ui.cmbTesters->setEnabled(false);
		QString qs = QStringLiteral("Unable to Open File: %1\n%2").arg(m_dbFileName).arg(err);
		QString qs2 = QStringLiteral("Unable to Open File: %1").arg(m_dbFileName);
		m_dbFileNameLabel.setText(QDir::toNativeSeparators(qs2));
		QMessageBox::warning(this, QStringLiteral("IDS Editor"),
							 qs, QMessageBox::Ok, QMessageBox::Ok);
	}
}

//------------------------------------------------------------------------------
// OnFileSave
//
bool IdsEditor::OnFileSave()
{
	// Todo: save DB, or update as we go along?
// WriteIniFile
	// Rules
	// "ChangeCustomerData::CB_Server\nnumReq = 2\nminTemp = 20\nmaxTemp = 30\nmaxHour = 20\nminHour = 10"

	REMOBJ_HHASH::iterator hitr;
	for( hitr = m_RemObjs.begin(); hitr != m_RemObjs.end(); ++hitr ){
		REMOBJ_HASH& rRemObjs = hitr.value();
		if( rRemObjs.count() > 0 ){
			qDebug() << "Saving Rules For Tester " << hitr.key();
			for (RemObject* remObj : rRemObjs){
				qDebug() << "  " << remObj->ToString();// << Qt::endl << Qt::endl;
			}
		}
	}
//

	return true;
}

//------------------------------------------------------------------------------
// closeEvent
//
void IdsEditor::closeEvent(QCloseEvent* e)
{
	SaveState();

	// If the user has enabled the clear settings on exit ctrl-shift-c hot key combo, then clear them after save state called
	if( CLEAR_SETTINGS_ON_EXIT)
		QSettings().clear();

	if( !OnFileSave() )
	{
		QMessageBox::warning(this, QStringLiteral("IDS Editor"),
							 QStringLiteral("Unable to Save File: %1").arg(m_dbFileName),
							 QMessageBox::Ok,
							 QMessageBox::Ok);
	}

	QMainWindow::closeEvent(e);
}

//------------------------------------------------------------------------------
// OnHelp
//
void IdsEditor::OnHelp()
{
	QDesktopServices::openUrl(QUrl(QStringLiteral("file:///%1").arg(IDS_EDITOR_HELP_PDF), QUrl::TolerantMode));
}

//------------------------------------------------------------------------------
// OnEditTester
void IdsEditor::OnEditTester()
{
	TesterEditor dlg(this);
	if(QDialog::Accepted == dlg.exec() )
	{
		qDebug() << "Accepted";
	}
}

//------------------------------------------------------------------------------
// OnTesterSelectionChanged
//
void IdsEditor::OnTesterSelectionChanged(int index)
{
	QString newText = ui.cmbTesters->itemText(index);
	QString qs = QString("Current Tester by index: %1").arg(newText);
	qDebug() << qs;
	//statusBar()->showMessage(qs);
	m_currTester = ui.cmbTesters->currentText();
	if(	ui.cmbTesters->currentData() == ROLE_NEW_TESTER_KEY ){
		//qDebug() << "New Tester: " << m_tester;
		ui.DeleteBtn->setEnabled(false);
		ui.EditBtn->setEnabled(false);
		ui.NewBtn->setEnabled(false);
		ui.btnEditTester->setText("Add");
	}
	else{
		//qDebug() << "Current Tester: " << m_tester;
		ui.DeleteBtn->setEnabled(true);
		ui.EditBtn->setEnabled(true);
		ui.NewBtn->setEnabled(true);
		ui.btnEditTester->setText("Edit");
	}
	UpdateObjectModel();
}

//------------------------------------------------------------------------------
// OnRuleDelete
//
void IdsEditor::OnRuleDelete()
{
	if( NoCurr() ){
		QString qs = QStringLiteral("Sanity Check Failure: %1").arg("No Current Tester");
		QMessageBox::warning(this, QStringLiteral("IDS Editor"),
							 qs, QMessageBox::Ok, QMessageBox::Ok);
		return;
	}

	QModelIndexList list = ui.RulesTreeView->selectionModel()->selectedIndexes();
	for (QModelIndex index : list)
	{
		if( index.isValid())
		{
			if( index.data(ROLE_REM_KEY).isValid())
			{
				REMOBJ_HASH& rRemObjs = RemObjects();
				delete rRemObjs.take(index.data(ROLE_REM_KEY).toString());
				UpdateObjectModel();
			}
		}
	}
}

//------------------------------------------------------------------------------
// OnRuleEdit
//
void IdsEditor::OnRuleEdit()
{
	if( NoCurr() ){
		QString qs = QStringLiteral("Sanity Check Failure: %1").arg("No Current Tester");
		QMessageBox::warning(this, QStringLiteral("IDS Editor"),
							 qs, QMessageBox::Ok, QMessageBox::Ok);
		return;
	}

	QModelIndexList list = ui.RulesTreeView->selectionModel()->selectedIndexes();
	for (QModelIndex index : list)
	{
		Edit(index);
		break; // Only want first one
	}
}

//------------------------------------------------------------------------------
// OnRuleNew
//
void IdsEditor::OnRuleNew()
{
	if( NoCurr() ){
		QString qs = QStringLiteral("Sanity Check Failure: %1").arg("No Current Tester");
		QMessageBox::warning(this, QStringLiteral("IDS Editor"),
							 qs, QMessageBox::Ok, QMessageBox::Ok);
		return;
	}

	RemObject remObj;
	RuleEditor dlg(remObj, this);
	if(QDialog::Accepted == dlg.exec() )
	{
		REMOBJ_HASH& rRemObjs = RemObjects(); // m_RemObjs[m_currTester];
		remObj.Copy(dlg.RemObj());
		QString remKey = remObj.Rem();
		if( rRemObjs.contains(remKey))
			delete rRemObjs.take(remKey);

		rRemObjs.insert(remKey, new RemObject(remObj));
		UpdateObjectModel();
	}
}

//------------------------------------------------------------------------------
// OnRulesTreeViewDoubleClicked
//
void IdsEditor::OnRulesTreeViewDoubleClicked(const QModelIndex& index)
{
	Edit(index);
}

//------------------------------------------------------------------------------
// OnToolBarVisibilityChanged
//
void IdsEditor::OnToolBarVisibilityChanged(bool visible)
{
	// Prevent user from hiding the main tool bar
	if( !visible) qobject_cast<QToolBar*>(sender())->setVisible(true);
}
