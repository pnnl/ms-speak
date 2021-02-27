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
//		02.09.2021 CHM - Populate from Sqlite DB, added m_dbFileName.
//-------------------------------------------------------------------------------
//
// Summary: IdsEditor.h
//-------------------------------------------------------------------------------

#ifndef IDSEDITOR_H
#define IDSEDITOR_H

#include "ui_IdsEditor.h"

#include <QMainWindow>
#include <QLabel>
#include <QShortcut>
#include <QStandardItemModel>
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlError>

class RemObject;
/*
 * In general, recommend to use contains() and value() rather than operator[]()
 * for looking up a key in a hash. The reason is that operator[]() silently inserts an
 * item into the hash if no item exists with the same key (unless the hash is const).
 */
#define DB_HASH QHash<QString, QStringList>
#define REMOBJ_HASH QHash<QString, RemObject*>  // rem, object
#define REMOBJ_HHASH QHash<QString, REMOBJ_HASH>

class IdsEditor : public QMainWindow
{
	Q_OBJECT
private:
	Ui::IdsEditorClass ui;
	QShortcut m_clearSettingsShortcut;
	QString   m_dbFileName;
	QLabel    m_dbFileNameLabel;
	QStandardItemModel m_RemObjModel;
	//REMOBJ_HASH m_RemObjs;	// Key is rem Name
	REMOBJ_HHASH m_RemObjs; // key is a tester, value a hash of rem objects
	DB_HASH m_functions;	// key is a function, value a hash of endpoints
	DB_HASH m_methods;		// key is an endpoint, value a list of methods
	QSqlDatabase m_db;
	QString m_currTester;
	QStringList m_origs;
	QStringList m_mods;
	QStringList m_adds;
	QStringList m_dels;
	bool m_prompt;

public:
	IdsEditor(QWidget* parent = Q_NULLPTR);
	~IdsEditor();
	void ClearHHash();
	void UpdateObjectModel();
	REMOBJ_HHASH& RemObjHash() { return m_RemObjs; }
	bool NoCurr() { return m_currTester.isEmpty(); }
	QString Curr() { return m_currTester; }
	REMOBJ_HASH& RemObjects() { return m_RemObjs[m_currTester]; }
	QComboBox *Testers() { return ui.cmbTesters; }
	DB_HASH& Functions() { return m_functions; }
	DB_HASH& Methods() { return m_methods; }
	void Mods( bool add , QString qs ){ if( add ) m_mods<<qs; else m_mods.removeAll(qs); }
	void Adds( bool add , QString qs ){ if( add ) m_adds<<qs; else m_adds.removeAll(qs); }
	void Dels( bool add , QString qs ){ if( add ) m_dels<<qs; else m_dels.removeAll(qs); }

	bool Mods( QString qs ){ if( m_mods.contains(qs,Qt::CaseInsensitive) )
			return true; else return false; }
	bool Adds( QString qs ){ if( m_adds.contains(qs,Qt::CaseInsensitive) )
			return true; else return false; }
	bool Dels( QString qs ){ if( m_dels.contains(qs,Qt::CaseInsensitive) )
			return true; else return false; }
protected:
	virtual void closeEvent(QCloseEvent* e);
	virtual void resizeEvent(QResizeEvent* e) { QMainWindow::resizeEvent(e); SaveGeometry(); }

private:
	void CreateLogDock();
	void Edit(const QModelIndex&);

	QModelIndex ModelIndexByKeyAndRole(const QString&, int);

	void InitCombo();
	bool ReadDbFile(const QString& fileName, QString&);
	bool LoadRules( QSqlDatabase&, QString& );
	void RestoreGeometry();
	void RestoreState();
	QStandardItem* RuleItem(const QString&);
	void SaveGeometry();
	void SaveState();
	QStandardItem* RemItem(const QString&);

private slots:
	void OnAbout();
	void OnAboutQt();
	void OnClearSettings();
	void OnFileOpen();
	bool OnFileSave();
	void OnHelp();
	void OnQuit() { close(); }
	void OnInitCombo() { InitCombo(); }
	//void OnReadDbFile() { ReadDbFile(m_dbFileName);}
	void OnReadDbFile() { OnFileOpen(); m_prompt = true;}
	void OnRestoreState() { RestoreState(); }
	void OnRuleDelete();
	void OnRuleEdit();
	void OnRuleNew();
	void OnRulesTreeViewDoubleClicked(const QModelIndex&);
	void OnToolBarVisibilityChanged(bool);
	//void OnHostEditReturn();
	//void OnHostEditFinished();
	//void OnHostTextChanged(QString);
	void OnEditTester();
	void OnTesterSelectionChanged(int);

};
#endif // IDSEDITOR_H
