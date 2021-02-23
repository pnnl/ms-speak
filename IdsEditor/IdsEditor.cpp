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
	setWindowTitle(QStringLiteral("IDS Editor %1").arg(SOFTWARE_VERSION));
	RestoreGeometry();

	ui.RulesTreeView->setModel(&m_sectionModel);
	ui.RulesTreeView->setHeaderHidden(true);
	ui.RulesTreeView->setSelectionBehavior(QAbstractItemView::SelectRows);
	ui.RulesTreeView->setSelectionMode(QAbstractItemView::SingleSelection);
	ui.RulesTreeView->setEditTriggers(QAbstractItemView::NoEditTriggers);

	statusBar()->addWidget(&m_dbFileNameLabel);
	m_dbFileNameLabel.setText(QDir::toNativeSeparators(m_dbFileName));

	ui.DeleteBtn->setEnabled(false);
	ui.EditBtn->setEnabled(false);
	ui.NewBtn->setEnabled(false);
	ui.btnAddTester->setEnabled(false);
	ui.cmbTesters->setEnabled(false);
	//ui.cmbTesters->setEditable(false);

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
	connect(ui.btnAddTester, SIGNAL(clicked()), this, SLOT(OnAddTester()));

	QTimer::singleShot(100, this, SLOT(OnRestoreState())); // Restore State after Docks Created
	QTimer::singleShot(100, this, SLOT(OnReadDbFile()));
	QTimer::singleShot(150, this, SLOT(OnInitCombo()));
}
//-------------------------------------------------------------------------------
// ~IdsEditor
//
IdsEditor::~IdsEditor()
{
	qDeleteAll(m_sections);
	m_sections.clear();
}

//------------------------------------------------------------------------------
// Edit
//
void IdsEditor::Edit(const QModelIndex& index)
{
	if( index.isValid())
	{
		if( index.data(ROLE_SECTION_KEY).isValid())
		{
			QString sectionKey = index.data(ROLE_SECTION_KEY).toString();
			if( RuleSection* section = m_sections.value(sectionKey, Q_NULLPTR))
			{
				RuleEditor dlg(*section, this); // m_sections
				if( QDialog::Accepted == dlg.exec())
				{
					if( section->Section() == dlg.Section().Section())
					{
						// Same Section...so just copy
						section->Copy(dlg.Section());
					}
					else
					{
						// Different Section so delete old one and add new one
						delete m_sections.take(section->Section());
						section = new RuleSection(dlg.Section());
						m_sections.insert(section->Section(), section);
					}
					UpdateSectionModel();
				}
			}
		}
	}
}

//------------------------------------------------------------------------------
// ModelIndexByKeyAndRole
//
QModelIndex IdsEditor::ModelIndexByKeyAndRole(const QString& section, int role)
{
	QModelIndex idx;
	if( QStandardItem* item = m_sectionModel.item(0))
		idx = item->index();

	QModelIndexList idxList = m_sectionModel.match(idx, role, section, 1, Qt::MatchExactly | Qt::MatchRecursive | Qt::MatchWrap);
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
		QString tester;
		strQuery = QStringLiteral("SELECT %1 FROM %2").arg("*", DB_TABLE_TESTERS );
		query.prepare(strQuery);
		if( !query.exec()){
			errStr = QStringLiteral("Error preparing querying '%1':\n%2").arg(strQuery).arg(query.lastError().text());
			qDebug("%s", qPrintable(errStr));
			m_db.close();
			return bRet;
		}
		while( query.next() ){
			tester =  query.value(1).toString();
			qDebug() << "Tester: " << tester;
			ui.cmbTesters->addItem(tester);
		}
		ui.cmbTesters->setCurrentIndex(0);

		bRet = LoadRules( m_db,errStr );
		m_db.close();
		UpdateSectionModel();
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

	qDeleteAll(m_sections);
	m_sections.clear();
	/*
	QSettings ini(fileName, QSettings::IniFormat);
	QString sectionKey;
	QString key;
	QString value;
	for (QString iniKey : ini.allKeys())
	{
		sectionKey = QStringLiteral("[%1]").arg(iniKey.left(iniKey.indexOf(QStringLiteral("/"))));

		if( sectionKey.startsWith(SETTINGS_GROUP))
		{
			key = iniKey.right(iniKey.length() - iniKey.indexOf(QStringLiteral("/")) - 1);
			if( key == SETTINGS_LOG_FILE)
				m_logFileName = ini.value(iniKey).toString();
			continue;
		}

		if( !m_sections.contains(sectionKey))
			m_sections.insert(sectionKey, new RuleSection());

		if( RuleSection* section = m_sections.value(sectionKey, Q_NULLPTR))
		{
			section->Method = iniKey.left(iniKey.indexOf(QStringLiteral("@")));
			section->EndPoint = iniKey.mid(iniKey.indexOf(QStringLiteral("@")) + 1, iniKey.indexOf(QStringLiteral("/")) - iniKey.indexOf(QStringLiteral("@")) - 1);
			key = iniKey.right(iniKey.length() - iniKey.indexOf(QStringLiteral("/")) - 1);
			value = ini.value(iniKey).toString();

			if( key == RULE_KEY_NUMREQ)
			{
				if( !section->Rules.contains(RULE_TYPE_MAX_VALUE))
					section->Rules.insert(RULE_TYPE_MAX_VALUE, new Rule());

				if( Rule* rule = section->Rules.value(RULE_TYPE_MAX_VALUE, Q_NULLPTR))
				{
					rule->Name = RULE_TYPE_MAX_VALUE;
					rule->KeyValue.insert(key, value);
				}
			}
			else if( key == RULE_KEY_MAXTEMP || key == RULE_KEY_MINTEMP)
			{
				if( !section->Rules.contains(RULE_TYPE_TEMP_RANGE))
					section->Rules.insert(RULE_TYPE_TEMP_RANGE, new Rule());

				if( Rule* rule = section->Rules.value(RULE_TYPE_TEMP_RANGE, Q_NULLPTR))
				{
					rule->Name = RULE_TYPE_TEMP_RANGE;
					rule->KeyValue.insert(key, value);
				}
			}
			else if( key == RULE_KEY_MAXTIME || key == RULE_KEY_MINTIME)
			{
				if( !section->Rules.contains(RULE_TYPE_TIME_RANGE))
					section->Rules.insert(RULE_TYPE_TIME_RANGE, new Rule());

				if( Rule* rule = section->Rules.value(RULE_TYPE_TIME_RANGE, Q_NULLPTR))
				{
					rule->Name = RULE_TYPE_TIME_RANGE;
					rule->KeyValue.insert(key, value);
				}
			}
		}
	}
	*/

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
	UpdateSectionModel();
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
	return m_sectionModel.itemFromIndex(ModelIndexByKeyAndRole(ruleKey, ROLE_RULE_KEY));
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
// SectionItem
//
QStandardItem* IdsEditor::SectionItem(const QString& ruleKey)
{
	return m_sectionModel.itemFromIndex(ModelIndexByKeyAndRole(ruleKey, ROLE_SECTION_KEY));
}

//------------------------------------------------------------------------------
// UpdateSectionModel
//
void IdsEditor::UpdateSectionModel()
{
	m_sectionModel.clear();
	for (RuleSection* section : m_sections)
	{
		QStandardItem* sectionItem = new QStandardItem(section->Section());
		sectionItem->setData(section->Section(), ROLE_SECTION_KEY);
		m_sectionModel.appendRow(sectionItem);
		for (Rule* rule : section->Rules)
		{
			QStandardItem* ruleItem = new QStandardItem(rule->ToString());
			ruleItem->setData(section->Section(), ROLE_SECTION_KEY);
			ruleItem->setData(rule->ToString(), ROLE_RULE_KEY);
			sectionItem->appendRow(ruleItem);
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
		UpdateSectionModel();
		QSettings().setValue(SK_DB_FILE_NAME, m_dbFileName);
		m_dbFileNameLabel.setText(QDir::toNativeSeparators(m_dbFileName));
		ui.DeleteBtn->setEnabled(true);
		ui.EditBtn->setEnabled(true);
		ui.NewBtn->setEnabled(true);
		ui.btnAddTester->setEnabled(true);
		ui.cmbTesters->setEnabled(true);
	}
	else{
		ui.DeleteBtn->setEnabled(false);
		ui.EditBtn->setEnabled(false);
		ui.NewBtn->setEnabled(false);
		ui.btnAddTester->setEnabled(false);
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
	qDebug() << "Saving Rules For Tester " << m_Tester;
// WriteIniFile
	// Rules
	// "ChangeCustomerData::CB_Server\nnumReq = 2\nminTemp = 20\nmaxTemp = 30\nmaxHour = 20\nminHour = 10"
	for (RuleSection* section : m_sections)
		qDebug() << section->ToString() << Qt::endl << Qt::endl;
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
// OnAddTester
void IdsEditor::OnAddTester()
{
	//QString qs;
	QString newText = ui.cmbTesters->currentText();
	int index = ui.cmbTesters->findText(newText); // findData
	if(  index == -1 ){ // -1 for not found
		//qs = QString("Address added to Tester list: %1").arg(newText);
		ui.cmbTesters->addItem(newText);
		//m_Host = QHostAddress(ui.cmbTesters->currentText());
		m_Tester = ui.cmbTesters->currentText();
	}
	/*else{
		qs = QString("%1 already in list").arg(newText);
	}
	statusBar()->showMessage(qs);
	qDebug() << qs;*/
}

//------------------------------------------------------------------------------
// OnTesterSelectionChanged
//
void IdsEditor::OnTesterSelectionChanged(int index)
{
	QString newText = ui.cmbTesters->itemText(index);
	/*QString qs = QString(" Tester Changed to %1").arg(newText);
	qDebug() << qs;
	statusBar()->showMessage(qs);*/
	//m_Host = QHostAddress(ui.cmbTesters->currentText());
	m_Tester = ui.cmbTesters->currentText();
}

//------------------------------------------------------------------------------
// OnRuleDelete
//
void IdsEditor::OnRuleDelete()
{
	QModelIndexList list = ui.RulesTreeView->selectionModel()->selectedIndexes();
	for (QModelIndex index : list)
	{
		if( index.isValid())
		{
			if( index.data(ROLE_SECTION_KEY).isValid())
			{
				delete m_sections.take(index.data(ROLE_SECTION_KEY).toString());
				UpdateSectionModel();
			}
		}
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
		Edit(index);
		break; // Only want first one
	}
}

//------------------------------------------------------------------------------
// OnRuleNew
//
void IdsEditor::OnRuleNew()
{
	RuleSection section;
	RuleEditor dlg(section, this);// m_sections,
	if(QDialog::Accepted == dlg.exec() )
	{
		section.Copy(dlg.Section());
		QString sectionKey = section.Section();
		if( m_sections.contains(sectionKey))
			delete m_sections.take(sectionKey);

		m_sections.insert(sectionKey, new RuleSection(section));
		UpdateSectionModel();
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
