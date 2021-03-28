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
	  m_prompt(false),
	  m_saveErr(false),
	  m_DBmods(false)
{
	ui.setupUi(this);

	ui.DeleteBtn->setEnabled(false);
	ui.EditBtn->setEnabled(false);
	ui.NewBtn->setEnabled(false);
	ui.btnEditTester->setEnabled(false);

	setWindowTitle(QStringLiteral("IDS Editor %1").arg(SOFTWARE_VERSION));
	RestoreGeometry();

	ui.RulesTreeView->setModel(&m_RemObjModel);
	ui.RulesTreeView->setHeaderHidden(true);
	ui.RulesTreeView->setSelectionBehavior(QAbstractItemView::SelectRows);
	ui.RulesTreeView->setSelectionMode(QAbstractItemView::SingleSelection);
	ui.RulesTreeView->setEditTriggers(QAbstractItemView::NoEditTriggers);

	statusBar()->addWidget(&m_dbFileNameLabel);
	statusBar()->setToolTip( "SQLite Open-source Database" );

	m_dbFileNameLabel.setText(QDir::toNativeSeparators(m_dbFileName));

	connect(ui.FileNewAct, SIGNAL(triggered()), this, SLOT(OnFileNew()));
	connect(ui.FileOpenAct, SIGNAL(triggered()), this, SLOT(OnFileOpen()));
	connect(ui.FileSaveAct, SIGNAL(triggered()), this, SLOT(OnFileSave()));
	connect(ui.FileSaveAsAct, SIGNAL(triggered()), this, SLOT(OnFileSaveAs()));

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
	ClearHashes();
	if( m_db.isOpen() ){
		qDebug("~IdsEditor""Database still Open.");
		m_db.close();
	}
}

//-------------------------------------------------------------------------------
// ClearHHash
//
void IdsEditor::ClearHashes()
{
	REMOBJ_HHASH::iterator hitr;
	for( hitr = m_RemObjs.begin(); hitr != m_RemObjs.end(); ++hitr ){
		REMOBJ_HASH& h = hitr.value();
		qDeleteAll(h); // is the same as qDeleteAll(c.begin(), c.end()).
		h.clear();
	}
	//qDeleteAll(m_RemObjs);
	m_RemObjs.clear();

	//TESTER_HASH::iterator titr;
	//for( titr = m_Testers.begin(); titr != m_Testers.end(); ++titr ){
	qDeleteAll(m_Testers);
	m_Testers.clear();
	DB_HASH::iterator ditr;
	for( ditr = m_functions.begin(); ditr != m_functions.end(); ++ditr ){
		QStringList& ql = ditr.value();
		ql.clear();
	}
	for( ditr = m_methods.begin(); ditr != m_methods.end(); ++ditr ){
		QStringList& ql = ditr.value();
		ql.clear();
	}
}

//-------------------------------------------------------------------------------
// reset
//
void IdsEditor::reset()
{
	ClearHashes();
	m_ActTesterOrig = Q_NULLPTR;
	m_ActTester = Q_NULLPTR;
	m_currTester = Q_NULLPTR;
	m_origs.clear();
	m_DBmods = false;
	ui.cmbTesters->clear();

	//ui.cmbTesters->setEditable(false);
	ui.cmbTesters->addItem("<new>", ROLE_NEW_TESTER_KEY);
	ui.DeleteBtn->setEnabled(false);
	ui.EditBtn->setEnabled(false);
	ui.NewBtn->setEnabled(false);
	ui.btnEditTester->setEnabled(false);
	//ui.cmbTesters->setEnabled(false);
	//ui.cmbTesters->setEditable(false);
	m_RemObjModel.clear();
	m_dbFileNameLabel.setText(QDir::toNativeSeparators(""));
	this->repaint();
	qApp->processEvents();
}

//-------------------------------------------------------------------------------
// Modded
//
void IdsEditor::Modded( bool bTester /*=true*/ )
{
	if( bTester )
		m_Testers[m_currTester]->Modded(true);
	m_DBmods = true;
}

//-------------------------------------------------------------------------------
// DirtyRules
//
void IdsEditor::DirtyRules( bool b )
{
	m_Testers[m_currTester]->DirtyRules(b);
	m_DBmods = true;
}

//-------------------------------------------------------------------------------
// DirtyRules
/*
bool IdsEditor::DirtyRules( void )
{
	return m_Testers[m_currTester]->DirtyRules();
}*/

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
// OpenBizDB
//
bool IdsEditor::OpenBizDB(const QString& fileName, QString& errStr,
						  const QString &options, const bool bNew /*=false*/)
{
	bool bRet = false;
	if( fileName.isEmpty() ){
		errStr = QStringLiteral("Error Opening DB - File Name is Empty.");
		return bRet;
	}
	if( !bNew )
	{
		QFileInfo check_file(fileName);
		// check if file exists and if it does, check that it;s really a file and not a directory
		if( !check_file.exists() ) {
			errStr = QStringLiteral("Error Opening DB - File Does Not Exist.");
			return bRet;
		}
		if( !check_file.isFile() ) {
			errStr = QStringLiteral("Error Opening DB - File Name is a Directory.");
			return bRet;
		}
	}
	if( m_db.isOpen() ){
		qDebug("Database still Open.");
		m_db.close();
	}

	/* Create database connection.
	 * if connection name is defined application-wide and you call addDatabase in each of
	 * the objects that use it, you are changing all QSqlDatabase objects that uses the same
	 * connection name and invalidating all queries that were active on them.
	 */
	if( !m_db.isValid() ){
		m_db = QSqlDatabase::addDatabase("QSQLITE", DB_CONNECTION_NAME);
		if( !m_db.isValid() ){
			qDebug("Error occurred adding the database.");
			qDebug("%s.", qPrintable(m_db.lastError().text()));
			return bRet;
		}
	}
	else{
		qDebug("SqlDatabase::addDatabase already valid");
	}
	/*m_db.setHostName("acidalia");
	m_db.setDatabaseName("customdb");
	m_db.setUserName("mojito");
	m_db.setPassword("J0a1m8");*/
	m_db.setConnectOptions(options); // For the QSQLITE driver, if the database name specified does not exist, 
									 // then it will create the file for you unless the QSQLITE_OPEN_READONLY option is set
	m_db.setDatabaseName(fileName);
	if( !m_db.open() ){ // this line creates the db, if it didn't exist
		errStr = QStringLiteral("Error occurred opening the database: '%1'").arg(m_db.lastError().text());
		qDebug("%s", qPrintable(errStr));
		return bRet;
	}
	return true;
}

//------------------------------------------------------------------------------
// CreateBizDB
bool IdsEditor::CreateBizDB(const QString& fileName, QString& errStr)
{
	bool bRet = OpenBizDB( fileName, errStr, QString(""), true );
	if( !bRet ){
		return bRet;
	}
	bRet = false;
	/*
	 * all QSqlQuery are detached from the QSqlDatabase before closing the database
	 *  by calling QSqlQuery::finish(), which is automatic when the QSqlQuery object
	 *  goes out of scope,
	 */
	QSqlQuery query(m_db);

	// create tester table
	QString strQuery = QStringLiteral(
	"CREATE TABLE [Testers] (" 
	"	[Id] INTEGER NOT NULL PRIMARY KEY,"
	"	[Name]  NVARCHAR(50) NOT NULL,"
	"	[AppId] NVARCHAR(50),"
	"	[Zipcode] NVARCHAR(6),"
	"	UNIQUE(Name) );"
	);
	if( !query.exec(strQuery) ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		//qDebug("%s.", qPrintable(query.lastError().text()));
		m_db.close();
		return bRet;
	}	
 
	// create ActiveTester table
	strQuery = QStringLiteral(
	"CREATE TABLE [ActiveTester] ("
	"	[Id] INTEGER NOT NULL PRIMARY KEY,"
	"	[Tester] INTEGER NOT NULL,"
	"	FOREIGN KEY(Tester) REFERENCES Testers(Id) );"	
	);
	if( !query.exec(strQuery) ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		m_db.close();
		return bRet;
	}	
		
	// create Functions table
	strQuery = QStringLiteral(
	"CREATE TABLE [Functions] ("
	"	[Id] INTEGER NOT NULL PRIMARY KEY," 
	"	[Name] NVARCHAR(50) NOT NULL,"
	"	UNIQUE(Name) );" 
	);
	if( !query.exec(strQuery) ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		m_db.close();
		return bRet;
	}
	bool bInsert = query.exec("insert into Functions (Name) VALUES ('Customer Billing');");
	bInsert &= query.exec("insert into Functions (Name) VALUES ('Metering Management');");
	bInsert &= query.exec("insert into Functions (Name) VALUES ('Outage Management');");

	// create EndPoints table
	strQuery = QStringLiteral(
	"CREATE TABLE [EndPoints] ("
	"	[Id] INTEGER NOT NULL PRIMARY KEY,"
	"	[Function] INTEGER NOT NULL,"
	"	[Name] NVARCHAR(50) NOT NULL,"
	"	UNIQUE(Name),"
	"	FOREIGN KEY(Function) REFERENCES Functions(Id) ); "
	);
	if( !query.exec(strQuery) ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		m_db.close();
		return bRet;
	}
	// set function keys
	bInsert &= query.exec("INSERT INTO EndPoints (Function, Name ) VALUES "
	"	((SELECT Id FROM Functions WHERE Name ='Customer Billing'), 'CB_Server');");
	bInsert &= query.exec("INSERT INTO EndPoints (Function, Name ) VALUES "
	"	((SELECT Id FROM Functions WHERE Name ='Customer Billing'), 'MDM_Server');" );
	bInsert &= query.exec("INSERT INTO EndPoints (Function, Name ) VALUES "
	"	((SELECT Id FROM Functions WHERE Name ='Customer Billing'), 'PG_Server');");
	bInsert &= query.exec("INSERT INTO EndPoints (Function, Name ) VALUES "
	"	((SELECT Id FROM Functions WHERE Name ='Metering Management'), 'CD_Server');");
	bInsert &= query.exec("INSERT INTO EndPoints (Function, Name ) VALUES "
	"	((SELECT Id FROM Functions WHERE Name ='Metering Management'), 'MR_Server');");
	bInsert &= query.exec("INSERT INTO EndPoints (Function, Name ) VALUES "
	"	((SELECT Id FROM Functions WHERE Name ='Outage Management'), 'OD_Server');");

	// create Methods table
	strQuery = QStringLiteral(
	"CREATE TABLE [Methods] ("
	"	[Id] INTEGER NOT NULL PRIMARY KEY,"
	"	[EndPoint] INTEGER NOT NULL,"
	"	[Name] NVARCHAR(50) NOT NULL,"
	"	UNIQUE(EndPoint, Name),"
	"	FOREIGN KEY(EndPoint) REFERENCES EndPoints(Id) );"
	);
	if( !query.exec(strQuery) ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		m_db.close();
		return bRet;
	}
	// set Endpoint keys
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), 'ChangeCustomerData');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), 'ChangeMeterData');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), 'ChangeStreetLightData');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES"
	"	((SELECT Id FROM EndPoints WHERE Name ='CB_Server'), 'PingURL');");	

	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES"
	"	((SELECT Id FROM EndPoints WHERE Name ='CD_Server'), 'GetCDSupportedMeters');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='CD_Server'), 'InitiateConnectDisconnect');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='CD_Server'), 'IsCDSupported');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='CD_Server'), 'SetCDDevicesDisabled');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='CD_Server'), 'SetCDDevicesEnabled');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES"
	"	((SELECT Id FROM EndPoints WHERE Name ='CD_Server'), 'PingURL');");

	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='MDM_Server'), 'InitiateBillingDeterminants');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES"
	"	((SELECT Id FROM EndPoints WHERE Name ='MDM_Server'), 'PingURL');");

	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), 'GetLatestMeterReadings');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), 'GetMeterReadingsByBillingCycle');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), 'GetEndDeviceEventsByMeterIDs');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES"
	"	((SELECT Id FROM EndPoints WHERE Name ='MR_Server'), 'PingURL');");

	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), 'ChangePaymentTransactions');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), 'ChangeRecurringPaymentConfiguration');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), 'ProcessPaymentTransactions');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES"
	"	((SELECT Id FROM EndPoints WHERE Name ='PG_Server'), 'PingURL');");

	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='OD_Server'), 'GetMeterIDsByEndDeviceStateTypes');");
	bInsert &= query.exec("INSERT INTO Methods (EndPoint, Name ) VALUES "
	"	((SELECT Id FROM EndPoints WHERE Name ='OD_Server'), 'InitiateEndDevicePings');");
	//INSERT INTO Methods (EndPoint, Name ) VALUES
	//	((SELECT Id FROM EndPoints WHERE Name ='OD_Server'), 'PingURL"); 	
	if( !bInsert ){
		errStr = QStringLiteral("Error preparing Insert queryies:\n%1").arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		m_db.close();
		return bRet;
	}
	// create Rules table
	strQuery = QStringLiteral(
	"CREATE TABLE [Rules] ("
	"	[Id] INTEGER NOT NULL PRIMARY KEY,"
	"	[Tester] INTEGER NOT NULL,"
	"   [Function] INTEGER NOT NULL,"
	"	[Endpoint] INTEGER NOT NULL,"
	"	[Method] INTEGER NOT NULL,"
	"	[maxTemp] INTEGER CHECK( (maxTemp = NULL) OR (maxTemp between 32 and 120) ),"
	"	[minTemp] INTEGER CHECK( (minTemp = NULL) OR (minTemp between 0 and 100) ),"
	"	[maxHour] INTEGER CHECK( (maxHour = NULL) OR (maxHour between 1 and 24) ),"
	"	[minHour] INTEGER CHECK( (minHour = NULL) OR (minHour between 0 and 23) ),"
	"	[numReq] INTEGER,"
	"	[numRPH] INTEGER,"
	"	[email] NVARCHAR(50),"
	"	UNIQUE(Tester,Endpoint,Method),"
	"	CHECK( (maxTemp = NULL AND minTemp = NULL) OR (maxTemp > minTemp) ),"
	"	CHECK( (maxHour = NULL AND minHour = NULL) OR (maxHour > minHour) ),"
	"	FOREIGN KEY(Tester) REFERENCES Testers(Id),"
	"   FOREIGN KEY(Function) REFERENCES Functions(Id),"
	"	FOREIGN KEY(Endpoint) REFERENCES Endpoints(Id),"
	"	FOREIGN KEY(Method) REFERENCES Methods(Id) );"
	);
	if( !query.exec(strQuery) ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		m_db.close();
		return bRet;
	}
	return true;
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
	bool bRet = OpenBizDB( fileName, errStr, QString("") ); // QSQLITE_OPEN_READONLY
	if( !bRet ){
		return bRet;
	}
	bRet = false;
	QSqlQuery query(m_db);
	
	// Query.
	QString strQuery = QStringLiteral(
	"SELECT functions.name as Function, endpoints.name as EndPoint, methods.name as Method"
	" FROM Functions"
	" INNER JOIN endpoints ON endpoints.Function = Functions.id"
	" INNER JOIN methods ON methods.EndPoint = endpoints.id"
	" ORDER BY Function, EndPoint, Method;"
	);

	if( !query.prepare(strQuery) ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		//qDebug("%s.", qPrintable(query.lastError().text()));
		m_db.close();
		return bRet;
	}
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

	m_ActTester = Q_NULLPTR;
	strQuery = QStringLiteral(
	"SELECT %1 FROM %2"
	" INNER JOIN %3 ON testers.id = ActiveTester.Tester"
	" WHERE( Testers.Id =(SELECT Tester FROM ActiveTester));"
	).arg(DB_COLUMN_NAME).arg(DB_TABLE_TESTERS).arg(DB_TABLE_ACTIVE);

	if( !query.prepare(strQuery) ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		m_db.close();
		return bRet;
	}

	if( !query.exec() ){
		errStr = QStringLiteral("Error executing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		m_db.close();
		return bRet;
	}
	if( query.next() ){
		m_ActTester = query.value(0).toString();
	}
	m_ActTesterOrig = m_ActTester;
	qDebug() << "Active Tester is: " << m_ActTesterOrig;

	strQuery = QStringLiteral("SELECT Name, AppId, Zipcode FROM %1").arg(DB_TABLE_TESTERS);
	if( !query.prepare(strQuery) ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		m_db.close();
		return bRet;
	}
	if( !query.exec() ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		m_db.close();
		return bRet;
	}
	while( query.next() ){
		QString tester =  query.value(0).toString();
		QString AppId =  query.value(1).toString();
		QString Zipcode =  query.value(2).toString();
		//qDebug() << tester << ", " << AppId << ", " << Zipcode;
		ui.cmbTesters->insertItem(0, tester, ROLE_TESTER_KEY);
		m_origs << tester;

		m_Testers[tester] = new Tester();
		Tester *pTester = m_Testers[tester];
		pTester->Name( tester );
		pTester->AppId( AppId );
		pTester->Zip( Zipcode );
		pTester->Original( true );
	}
	ui.cmbTesters->setCurrentIndex(0);

	bRet = LoadRules( m_db,errStr );
	//m_db.close();
	//UpdateObjectModel();
	return bRet;
}

//------------------------------------------------------------------------------
// LoadRules
//
bool IdsEditor::LoadRules( QSqlDatabase& db, QString& errStr )
{
	bool bRet = false;

	//ClearHashes();

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

	if( !query.prepare(strQuery) ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		m_db.close();
		return bRet;
	}
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
	"SELECT testers.Name as who, functions.Name as Function, endpoints.name as EndPoint, methods.name as Method,"
	" rules.maxTemp,rules.minTemp,rules.maxHour,rules.minHour,rules.numReq,rules.numRPH,rules.email"
	" FROM rules"
	" INNER JOIN functions ON functions.id = rules.function"
	" INNER JOIN endpoints ON endpoints.id = rules.endpoint"
	" INNER JOIN methods ON methods.id = rules.method"
	" INNER JOIN testers ON testers.id = rules.tester"
	" ORDER BY who;"
	);
	if( !query.prepare(strQuery) ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		m_db.close();
		return bRet;
	}
	if( !query.exec() ){
		errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
		qDebug("%s", qPrintable(errStr));
		return bRet;
	}
	while( query.next() ){
		QString Tester =  query.value(0).toString();
		QString Function =  query.value(1).toString();
		QString EndPoint =  query.value(2).toString();
		QString Method =  query.value(3).toString();
		QString maxTemp =  query.value(4).toString();
		QString minTemp =  query.value(5).toString();
		QString maxHour =  query.value(6).toString();
		QString minHour =  query.value(7).toString();
		QString numReq =  query.value(8).toString();
		QString numRPH =  query.value(9).toString();
		QString email =  query.value(10).toString();
		/*
		qDebug() << Tester;
		qDebug() << "   " << EndPoint << "::" << Method;
		qDebug() << "   " << maxTemp << "  " << minTemp << maxHour << "  " << minHour;
		qDebug() << "   " << numReq << "  " << numRPH << email;*/

		QString remKey = QStringLiteral("%1::%2").arg(EndPoint, Method);
		REMOBJ_HASH& rRemObjs = m_RemObjs[Tester];
		rRemObjs.insert(remKey, new RemObject());
		RemObject *pRemObj = rRemObjs[remKey];
		pRemObj->m_Function = Function;
		pRemObj->m_EndPoint = EndPoint;
		pRemObj->m_Method = Method;

		if( !maxTemp.isEmpty() ){
			pRemObj->Rules.insert(RULE_TYPE_TEMP_RANGE, new Rule());
			if( Rule* rule = pRemObj->Rules.value(RULE_TYPE_TEMP_RANGE, Q_NULLPTR))
			{
				rule->Name = RULE_TYPE_TEMP_RANGE;
				rule->KeyValue.insert(RULE_KEY_MAXTEMP, maxTemp);
				rule->KeyValue.insert(RULE_KEY_MINTEMP, minTemp);
			}
		}
		if( !maxHour.isEmpty() ){
			pRemObj->Rules.insert(RULE_TYPE_TIME_RANGE, new Rule());
			if( Rule* rule = pRemObj->Rules.value(RULE_TYPE_TIME_RANGE, Q_NULLPTR))
			{
				rule->Name = RULE_TYPE_TIME_RANGE;
				rule->KeyValue.insert(RULE_KEY_MAXTIME, maxHour);
				rule->KeyValue.insert(RULE_KEY_MINTIME, minHour);
			}
		}
		if( !numReq.isEmpty() ){
			pRemObj->Rules.insert(RULE_TYPE_MAX_VALUE, new Rule());
			if( Rule* rule = pRemObj->Rules.value(RULE_TYPE_MAX_VALUE, Q_NULLPTR))
			{
				rule->Name = RULE_TYPE_MAX_VALUE;
				rule->KeyValue.insert(RULE_KEY_NUMREQ, numReq);
				if( !numRPH.isEmpty() )
					rule->KeyValue.insert(RULE_KEY_NUMRPH, numRPH);
			}
		}
		else if( !numRPH.isEmpty() ){
			pRemObj->Rules.insert(RULE_TYPE_MAX_VALUE, new Rule());
			if( Rule* rule = pRemObj->Rules.value(RULE_TYPE_MAX_VALUE, Q_NULLPTR))
			{
				rule->Name = RULE_TYPE_MAX_VALUE;
				rule->KeyValue.insert(RULE_KEY_NUMRPH, numRPH);
			}
		}
		if( !email.isEmpty() ){
			pRemObj->Rules.insert(RULE_TYPE_EMAIL, new Rule());
			if( Rule* rule = pRemObj->Rules.value(RULE_TYPE_EMAIL, Q_NULLPTR))
			{
				rule->Name = RULE_TYPE_EMAIL;
				rule->KeyValue.insert(RULE_KEY_EMAIL, email);
			}
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
	ui.cmbTesters->addItem("<new>", ROLE_NEW_TESTER_KEY);
	ui.cmbTesters->setMinimumWidth(150);
	ui.cmbTesters->lineEdit()->setAlignment(Qt::AlignCenter);
	//ui.cmbHosts->lineEdit()->setInputMask( "000.000.000.000" );
	ui.cmbTesters->setEnabled(true);
	ui.cmbTesters->setEditable(false);
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
void IdsEditor::UpdateObjectModel(QString rem /*= Q_NULLPTR*/)
{
	QModelIndex	index;

	m_RemObjModel.clear();

	REMOBJ_HASH& rRemObjs = RemObjects();
	for (RemObject* remObj : rRemObjs)
	{
		QString ItemRem = remObj->Rem();
		QStandardItem* RemItem = new QStandardItem(ItemRem);
		RemItem->setData(ItemRem, ROLE_REM_KEY);
		m_RemObjModel.appendRow(RemItem);
		for (Rule* rule : remObj->Rules)
		{
			QStandardItem* ruleItem = new QStandardItem(rule->ToString());
			ruleItem->setData(ItemRem, ROLE_REM_KEY);
			ruleItem->setData(rule->ToString(), ROLE_RULE_KEY);
			RemItem->appendRow(ruleItem);
			if( !rem.isNull() ){
				if( rem == ItemRem ){
					index = RemItem->index();
				}
			}
		}
	}
	//ui.RulesTreeView->expandAll();
	if( index.isValid() ){
		ui.RulesTreeView->expand(index);
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
// OnFileNew
//
void IdsEditor::OnFileNew()
{
	QString fileName = QFileDialog::getSaveFileName(this, QStringLiteral("New Business Rules Database"),
	m_dbFileName, QStringLiteral("Sqlite DB File (*.db)"));

	if (fileName.isEmpty())
		return;

	reset();

	if( QFile::exists(fileName) ){
		QFile file (fileName);
		file.remove();
	}
	m_dbFileName = fileName;

	QString err;
	if( CreateBizDB(m_dbFileName, err) ){
	}
	else{
		ui.btnEditTester->setEnabled(false);
		//ui.cmbTesters->setEnabled(false);
		QString qs = QStringLiteral("Unable to Open File: %1\n%2").arg(m_dbFileName).arg(err);
		QString qs2 = QStringLiteral("Unable to Open File: %1").arg(m_dbFileName);
		m_dbFileNameLabel.setText(QDir::toNativeSeparators(qs2));
		QMessageBox::warning(this, QStringLiteral("IDS Editor"),
							 qs, QMessageBox::Ok, QMessageBox::Ok);
		return;
	}
	m_prompt = false;
	OnFileOpen();
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
		reset();
		m_dbFileName = fileName;
	}
	else{

	}
	m_prompt = true;
	QString err;
	if( ReadDbFile(m_dbFileName, err) ){
		//UpdateObjectModel(); this is done inside ReadDbFile
		QSettings().setValue(SK_DB_FILE_NAME, m_dbFileName);
		m_dbFileNameLabel.setText(QDir::toNativeSeparators(m_dbFileName));
		ui.btnEditTester->setEnabled(true);
		//ui.cmbTesters->setEnabled(true);
	}
	else{
		ui.btnEditTester->setEnabled(false);
		//ui.cmbTesters->setEnabled(false);
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
/*
 * If you want to insert many records at the same time, it is often more efficient to separate the
 * query from the actual values being inserted. This can be done using placeholders. Qt supports two
 * placeholder syntaxes: named binding and positional binding. Here's an example of named binding:

	QSqlQuery query;
	query.prepare("INSERT INTO employee (id, name, salary) "
				  "VALUES (:id, :name, :salary)");
	query.bindValue(":id", 1001);
	query.bindValue(":name", "Thad Beaumont");
	query.bindValue(":salary", 65000);
	query.exec();
Here's an example of positional binding:
	QSqlQuery query;
	query.prepare("INSERT INTO employee (id, name, salary) "
				  "VALUES (?, ?, ?)");
	query.addBindValue(1001);
	query.addBindValue("Thad Beaumont");
	query.addBindValue(65000);
	query.exec();

The actual query that ends up being executed by the DBMS is available as QSqlQuery::executedQuery().

When inserting multiple records, you only need to call QSqlQuery::prepare() once. Then you call
 bindValue() or addBindValue() followed by exec() as many times as necessary.
*/
bool IdsEditor::OnFileSave()
{
	qDebug() << "TODO: check if new rules are not saved when doing 'SaveAs'";

	if( !m_db.open() ){
		QString qs = QStringLiteral("Unable to Save DB '%1', Not Open.").arg(m_dbFileName);
		QMessageBox::warning(this, QStringLiteral("IDS Editor"),
							 qs, QMessageBox::Ok, QMessageBox::Ok);
		return false;
	}

	if( !m_DBmods ){
		qDebug() << "Nothing Changed, Nothing to Save";
		return true;
	}
	m_DBmods = false;
	m_saveErr = true;
	//qDebug() << "Changes Saved.";
	//return true;

	TESTER_HASH::iterator titr;
	REMOBJ_HHASH::iterator hitr;
	bool bShowAll = false;
	if( bShowAll )
	{
		for( hitr = m_RemObjs.begin(); hitr != m_RemObjs.end(); ++hitr ){
			REMOBJ_HASH& rRemObjs = hitr.value();
			if( rRemObjs.count() > 0 ){
				qDebug() << "Saving Rules For Tester " << hitr.key();
				for (RemObject* remObj : rRemObjs){
					//qDebug() << "  " << remObj->ToString();// << Qt::endl << Qt::endl;
					qDebug() << "  " << remObj->m_Function;
				}
			}
		}
		for( titr = m_Testers.begin(); titr != m_Testers.end(); ++titr ){
			Tester* tester= titr.value();
			qDebug() << "Showing Attributes For Tester " << titr.key();
			qDebug() << "  " << tester->ToString();// << Qt::endl << Qt::endl;
		}
	}
	QString errStr;
	QSqlQuery query(m_db);
	QString strQuery;

	// == Add or Modify Tester ==
	QString strQueryAddMod = QStringLiteral(
			"INSERT OR REPLACE INTO Testers(Name, AppId, Zipcode) "
			"VALUES (:Name, :AppId, :Zipcode);"
	);

	// == Update Active Tester ==
	QString strQueryModAct = QStringLiteral(
		"INSERT OR REPLACE INTO ActiveTester(Id,Tester) "
		"VALUES(1, (SELECT Id FROM Testers WHERE Name = ?));"
	);

	// == Remove From Active Tester ==
	QString strQueryDelAct = QStringLiteral(
		"DELETE FROM ActiveTester WHERE Id = 1;"
	);
	// "DELETE FROM ActiveTester WHERE Tester = "
	// "(SELECT Id FROM Testers WHERE Name = ?);"

	// == Add Tester Rule ==
	QString strQueryQAddRule = QStringLiteral(
		"WITH EpId AS (SELECT Id FROM EndPoints WHERE Name = :EpName) "
		"INSERT OR REPLACE INTO Rules (Tester, Function, Endpoint, Method, maxTemp, minTemp, maxHour, minHour, numReq, numRPH, email ) "
		"VALUES ((SELECT Id FROM Testers WHERE Name = :TstrName), "
		"(SELECT Id FROM Functions WHERE Name =:FuncName), "
		"(SELECT * from EpId), "
		"(SELECT Id FROM Methods WHERE (Name = :MetName AND EndPoint=(SELECT * from EpId))), "
		":mxTemp, :mnTemp, :mxHour, :mnHour, :nReq, :nRPH, :em);"
	);

	// == Remove Tester Rule ==
	QString strQueryDelRule = QStringLiteral(
		"DELETE FROM Rules WHERE id ="
		" (SELECT rules.id"
		" FROM rules"
		" INNER JOIN endpoints ON endpoints.id = rules.endpoint"
		" INNER JOIN methods ON methods.id = rules.method"
		" WHERE( Tester =(SELECT id FROM Testers WHERE Name = :TstrName) AND"
		"  rules.endpoint =(SELECT id FROM endpoints WHERE Name = :EpName) AND"
		"  rules.method IN (SELECT id FROM methods WHERE Name = :MetName)));"
	);

	// == Remove Tester Rules ==
	QString strQueryDelRules = QStringLiteral(
		"DELETE FROM Rules WHERE id IN "
		"(SELECT rules.id FROM rules "
		"WHERE( Tester =(SELECT id FROM Testers WHERE Name = ?)));"
	);
	// == Remove Tester ==
	QString strQueryDelTstr = QStringLiteral(
		"DELETE FROM Testers WHERE Name = ?;"
	);

	bool delActive = false;
	QString op;
	for( titr = m_Testers.begin(); titr != m_Testers.end(); ++titr ){
		Tester* tester= titr.value();
		//	if we added a new user, we need to add it to the table before removing rules
		//	but if Dirty-Rules(), we need to delete them all before deleting a tester
		QString qsName = tester->Name();
		if( tester->Dirty() || tester->DirtyRules() ){
			// show dirty users
			qDebug() << "Showing Dirty Tester:" << qsName;
			tester->Modded(false);
			bool addrules = true;
			bool delrules = true;
			if( tester->Dirty() ){
				tester->Dirty(false);
				switch( tester->Op() ){
					case NIL:
						qDebug() << "NIL ---> " << tester->ToString();
						continue;
						break;

					case ADD:
					case MOD:
						if( tester->Op() == ADD ){
							qDebug() << "ADD ---> " << tester->ToString();
							delrules = false;
							// tester->DirtyRules(true); ?????
						}
						else
							qDebug() << "MOD ---> " << tester->ToString();
						break;

					case DEL:
						qDebug() << "DEL ---> " << tester->ToString();
						// set DirtyRules to force going in below, then
						// remove rules prior to removing tester
						tester->DirtyRules(true);
						addrules = false;
						break;
				} // switch on tester->Op()
				if( tester->Op() != DEL ){
					qDebug() << "Add/Moddiing Tester:" << qsName;
					if( query.prepare( strQueryAddMod ) ){
						query.bindValue(":Name", qsName);
						query.bindValue(":AppId", tester->AppId());
						query.bindValue(":Zipcode", tester->Zip());
						if( !ExecQuery( query ) ){
							return false;
						}
					}
					else{
						errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQueryAddMod).arg(query.lastError().text());
						qDebug("%s", qPrintable(errStr));
						QMessageBox::warning(this, QStringLiteral("IDS Editor"),
											 errStr, QMessageBox::Ok, QMessageBox::Ok);
						return false;
					}
				}
			} // >Dirty()
			if( tester->DirtyRules() ){
				tester->DirtyRules(false);
				/* can't maintain add/del/mod per rule since when deleted, the
				 * rule is no longer in the hash, so won't have it to use when
				 * needed here to delete from the DB.
				 */
				if( delrules ){
					// delete all old rules, then add back existing ones
					//qDebug() << "---> Del Dirty Rules for " << qsName;
					if( query.prepare( strQueryDelRules ) ){
						query.addBindValue(qsName);
						if( !ExecQuery( query ) ){
							return false;
						}
					}
					else{
						errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQueryDelRules).arg(query.lastError().text());
						qDebug("%s", qPrintable(errStr));
						QMessageBox::warning(this, QStringLiteral("IDS Editor"),
											 errStr, QMessageBox::Ok, QMessageBox::Ok);
						return false;
					}
				}
				if( addrules ){
					// To bind a NULL value, use a null QVariant; for example,
					//  use QVariant(QVariant::String) if you are binding a string. for Qt5
					//	use QVariant(QMetaType::QString) if you are binding a string. for Qt6
					qDebug() << "---> Adding Rules for " << qsName;
					if( query.prepare( strQueryQAddRule ) ){
						REMOBJ_HASH& rRemObjs = m_RemObjs[qsName];
						for (RemObject* pRemObj : rRemObjs)
						{
							RuleData rd;
							pRemObj->getData( rd, qsName );
							QString Str = QString("       %1:%2").arg(rd.m_Endpoint).arg(rd.m_Method);
							qDebug() << Str;

							query.bindValue(":TstrName", rd.m_Tester);
							query.bindValue(":FuncName", rd.m_Function);
							query.bindValue(":EpName", rd.m_Endpoint);
							query.bindValue(":MetName", rd.m_Method);
							if (rd.m_maxTemp.isEmpty()){
								query.bindValue(":mxTemp", QVariant(QVariant::String));
								query.bindValue(":mnTemp", QVariant(QVariant::String));
							}else{
								query.bindValue(":mxTemp", rd.m_maxTemp.toInt());
								query.bindValue(":mnTemp", rd.m_minTemp.toInt());
							}
							if (rd.m_maxHour.isEmpty()){
								query.bindValue(":mxHour", QVariant(QVariant::String));
								query.bindValue(":mnHour", QVariant(QVariant::String));
							}else{
								query.bindValue(":mxHour", rd.m_maxHour.toInt());
								query.bindValue(":mnHour", rd.m_minHour.toInt());
							}
							if (rd.m_numReq.isEmpty()){
								query.bindValue(":nReq", QVariant(QVariant::String));
							}else{
								query.bindValue(":nReq", rd.m_numReq.toInt());
							}
							/*
							 * TODO: allow to have either/or total reqs or reqsph
							 *		that is, allow just numRPH if desired.
							 */
							if (rd.m_numRPH.isEmpty()){
								query.bindValue(":nRPH", QVariant(QVariant::String));
							}else{
								query.bindValue(":nRPH", rd.m_numRPH.toInt());
							}
							if (rd.m_email.isEmpty()){
								query.bindValue(":em", QVariant(QVariant::String));
							}else{
								query.bindValue(":em", rd.m_email);
							}
							if( !ExecQuery( query ) ){
								return false;
							}
						}// for pRemObj
					}
					else{
						errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQueryQAddRule).arg(query.lastError().text());
						qDebug("%s", qPrintable(errStr));
						QMessageBox::warning(this, QStringLiteral("IDS Editor"),
											 errStr, QMessageBox::Ok, QMessageBox::Ok);
						return false;
					}
				}
				else{
					//must be DEL
					qDebug() << "Deleting Tester:" << qsName;
					if( qsName == m_ActTesterOrig ){
						delActive = true;
					}
					if( query.prepare( strQueryDelTstr ) ){
						query.addBindValue(qsName);
						if( !ExecQuery( query ) ){
							return false;
						}
					}
					else{
						errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQueryDelTstr).arg(query.lastError().text());
						qDebug("%s", qPrintable(errStr));
						QMessageBox::warning(this, QStringLiteral("IDS Editor"),
											 errStr, QMessageBox::Ok, QMessageBox::Ok);
						return false;
					}
					RemoveTester(qsName); // this already done in EditTester, but not for original testers
				}
			} // DirtyRules
		} // Dirty() || DirtyRules()
		// show if dirty rules
	} // for m_Testers
	QString actQueryStr = Q_NULLPTR;
	if( delActive ){
		m_ActTester = Q_NULLPTR;
		m_ActTesterOrig = Q_NULLPTR;
		actQueryStr = strQueryDelAct;
	}
	else{
		if( m_ActTesterOrig != m_ActTester ){
			m_ActTesterOrig = m_ActTester;
			actQueryStr = strQueryModAct;
		}
	}
	if( !actQueryStr.isEmpty() ){
		if( query.prepare( strQueryModAct ) ){
			if( !delActive )
				query.addBindValue(m_ActTester);
			if( !ExecQuery( query ) ){
				return false;
			}
		}
		else{
			errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQueryModAct).arg(query.lastError().text());
			qDebug("%s", qPrintable(errStr));
			QMessageBox::warning(this, QStringLiteral("IDS Editor"),
								 errStr, QMessageBox::Ok, QMessageBox::Ok);
			return false;
		}
	}
	if( Active().isEmpty() ){
		qDebug() << "No Active Tester Set.";
	}else{
		qDebug() << "Active Tester Set To: " << Active();
	}
	m_saveErr = false;
	return true;
}

//------------------------------------------------------------------------------
// ExecQuery
//
bool IdsEditor::ExecQuery( QSqlQuery& query )
{
	QString strQuery;
	QString errStr;
	bool bRet = query.exec();
	if( !bRet ){
		strQuery = query.executedQuery();
		errStr = QStringLiteral("Query Error updating DB:\n%1\n%2").arg(query.lastError().text()).arg(strQuery);
		QMessageBox::warning(this, QStringLiteral("IDS Editor"),
							 errStr, QMessageBox::Ok, QMessageBox::Ok);
		return bRet;
	}
	else{
		//qDebug() << "numRowsAffected: " << query.numRowsAffected();
		/* there may be no, or many rules etc.
		if( query.numRowsAffected() != 1 ){
			qDebug() <<  query.lastQuery();
			strQuery = query.executedQuery();
			errStr = QStringLiteral("Query Error updating Testers:\n%1\n%2").arg(query.lastError().text()).arg(strQuery);
			QMessageBox::warning(this, QStringLiteral("IDS Editor"),
								 errStr, QMessageBox::Ok, QMessageBox::Ok);
			bRet = false;
		}*/
	}
	return bRet;
}

//------------------------------------------------------------------------------
// OnFileSaveAs
//
void IdsEditor::OnFileSaveAs()
{
	QString fileName = QFileDialog::getSaveFileName(this, QStringLiteral("New Business Rules Database"),
	m_dbFileName, QStringLiteral("Sqlite DB File (*.db)"));

	if (fileName.isEmpty())
		return;

	m_dbFileName = fileName;
	OnFileSave();
	//m_dbFileName = fileName; 3.28 why here?

	QSettings().setValue(SK_DB_FILE_NAME, m_dbFileName);
	m_dbFileNameLabel.setText(QDir::toNativeSeparators(m_dbFileName));
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

	if( !m_saveErr ){
		if( m_DBmods ){
			QMessageBox::StandardButton reply;
			reply = QMessageBox::question(this, "IDS Editor", "Save Changes?",
										  QMessageBox::Yes|QMessageBox::No);
			if (reply == QMessageBox::Yes) {
				if( !OnFileSave() )
				{
					QMessageBox::warning(this, QStringLiteral("IDS Editor"),
										 QStringLiteral("Unable to Save File: %1").arg(m_dbFileName),
										 QMessageBox::Ok,
										 QMessageBox::Ok);
				}
			}
		}
	}
	if( m_db.isOpen() ){
		m_db.close();
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
	if(	ui.cmbTesters->currentData() == ROLE_NEW_TESTER_KEY ){
		NewTester();
	}
	else{
		EditTester( ui.cmbTesters->currentText() );
	}
}

//------------------------------------------------------------------------------
// NewTester
//
void IdsEditor::NewTester(void)
{
	Tester tester;
	TesterEditor dlg(tester, true, this);
	if(QDialog::Accepted == dlg.exec() )
	{
		TESTER_HASH& rTesters = Testers();
		tester.Copy(dlg.GetTester());
		QString tstKey = tester.Name();
		if( rTesters.contains(tstKey))
			delete rTesters.take(tstKey);

		rTesters.insert(tstKey, new Tester(tester));
		UpdateObjectModel();
		Modded();
	}
}

//------------------------------------------------------------------------------
// EditTester
//
void IdsEditor::EditTester( QString qsName )
{
	//qDebug() << "EditTester: " << qsName;
	TESTER_HASH& rTesters = Testers();
	if( Tester* tester = rTesters.value(qsName, Q_NULLPTR))
	{
		TesterEditor dlg(*tester, false, this);
		if( QDialog::Accepted == dlg.exec())
		{
			const Tester& rTester = dlg.GetTester();
			if( rTester.Dirty() )
			{
				Modded();
				if( rTester.Op() == DEL )
				{
					if( Active() == qsName ){
						Active( Q_NULLPTR );
					}
					if( Original(qsName) ){
						tester->Op(DEL);// mark so will remove from DB on Save
					}
					else{
						RemoveTester(qsName); // else was newly added, so not in DB yet
					}
					TesterCombo()->removeItem( TesterCombo()->currentIndex() );
				}
				else
				{
					if( tester->Name() == rTester.Name() )
					{
						// Same Name...so just copy
						tester->Copy(rTester);
					}
					else
					{
						// Different Name so delete old one and add new one
						// this should only be possible if Tester is not an original
						delete rTesters.take(tester->Name()); // Removes the item with the key from the hash and returns the value associated with it.
						tester = new Tester(rTester);
						rTesters.insert(tester->Name(), tester);
					}
				}
				UpdateObjectModel();
			}
		}
		else{
			// if we haven't previously accepted changes,
			// clear the dirty flag since we cancelled.
			if( !tester->Modded() ){
				tester->Dirty(false);
			}
		}
	}
}

//------------------------------------------------------------------------------
// RemoveTester
//
void IdsEditor::RemoveTester(QString qsName)
{
	TESTER_HASH& rTesters = Testers();
	delete rTesters.take(qsName);
	m_DBmods = true;
}

//------------------------------------------------------------------------------
// OnTesterSelectionChanged
//
void IdsEditor::OnTesterSelectionChanged(int index)
{
	QString newText = ui.cmbTesters->itemText(index);
	//QString qs = QString("Current Tester by index: %1").arg(newText);
	//qDebug() << qs;
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
/*
 * Note: it might be better to update the SQL DB as we go rather than
 *		only in OnFileSave, but then user can't cancel out all changes
 *		when exiting.
 */
void IdsEditor::OnRuleDelete()
{
	QModelIndexList list = ui.RulesTreeView->selectionModel()->selectedIndexes();
	for (QModelIndex index : list)
	{
		if( index.isValid())
		{
			if( index.data(ROLE_REM_KEY).isValid())
			{
				DirtyRules( true );
				REMOBJ_HASH& rRemObjs = RemObjects();
				delete rRemObjs.take(index.data(ROLE_REM_KEY).toString());
				UpdateObjectModel();
			}
		}
	}
}

//------------------------------------------------------------------------------
// OnRuleNew
//
void IdsEditor::OnRuleNew()
{
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
		DirtyRules( true );
		UpdateObjectModel( remKey );
	}
}

//------------------------------------------------------------------------------
// OnRuleEdit
//
void IdsEditor::OnRuleEdit()
{
	QModelIndexList list = ui.RulesTreeView->selectionModel()->selectedIndexes();
	for (QModelIndex index : list)
	{
		EditRule(index);
		break; // Only want first one
	}
}

//------------------------------------------------------------------------------
// EditRule
//
void IdsEditor::EditRule(const QModelIndex& index)
{
	if( index.isValid())
	{
		if( index.data(ROLE_REM_KEY).isValid())
		{
			QString remKey = index.data(ROLE_REM_KEY).toString();
			REMOBJ_HASH& rRemObjs = RemObjects();
			if( RemObject* remObj = rRemObjs.value(remKey, Q_NULLPTR))
			{
				// need to get the one selected
				RuleEditor dlg(*remObj, this);
				if( QDialog::Accepted == dlg.exec())
				{
					if( dlg.Modded() )
					{
						if( remObj->Rem() == dlg.RemObj().Rem() )
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
						UpdateObjectModel( remObj->Rem() );
						DirtyRules( true );
					}
				}
				else{
					// need catch if they modded, then 'saved', then 'cancel'd
					if( dlg.Modded() && dlg.Saved() ){
						DirtyRules( true );
					}
				}
			}
		}
	}
}

//------------------------------------------------------------------------------
// OnRulesTreeViewDoubleClicked
//
void IdsEditor::OnRulesTreeViewDoubleClicked(const QModelIndex& index)
{
	EditRule(index);
}

//------------------------------------------------------------------------------
// OnToolBarVisibilityChanged
//
void IdsEditor::OnToolBarVisibilityChanged(bool visible)
{
	// Prevent user from hiding the main tool bar
	if( !visible) qobject_cast<QToolBar*>(sender())->setVisible(true);
}
