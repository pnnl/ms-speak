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
//		2021 - Carl Miller <carl.miller@pnnl.gov>.
//-------------------------------------------------------------------------------
//
// Summary: TesterEditor.cpp
//-------------------------------------------------------------------------------

#include <QDebug>
#include <QHash>
#include <QSettings>
#include <QVariant>
//#include <QRegularExpression>
#include <QMessageBox>

#include "IdsSettings.h"
#include "RuleConst.h"
#include "TesterEditor.h"

//-------------------------------------------------------------------------------
// Tester
Tester::Tester(const Tester& rt)
	: m_Name(rt.m_Name),
	  m_AppId(rt.m_AppId),
	  m_Zipcode(rt.m_Zipcode),
	  m_dirty(rt.m_dirty),
	  m_dirtyrules(rt.m_dirtyrules),
	  m_modded(rt.m_modded),
	  m_orig(rt.m_orig),
	  m_op(rt.m_op)
{
}
Tester::Tester(void)
	: m_dirty(false),
	  m_dirtyrules(false),
	  m_modded(false),
	  m_orig(false),
	  m_op(NIL)
{
}
//-------------------------------------------------------------------------------
// Copy
//
void Tester::Copy(const Tester& ts)
{
	m_Name = ts.m_Name;
	m_AppId = ts.m_AppId;
	m_Zipcode = ts.m_Zipcode;
	m_dirty = ts.m_dirty;
	m_dirtyrules = ts.m_dirtyrules;
	m_modded = ts.m_modded;
	m_orig = ts.m_orig;
	m_op = ts.m_op;
}

//-------------------------------------------------------------------------------
// Tester::ToString
//
QString Tester::ToString() const
{
	QStringList strList;
	strList << Name();
	strList << QStringLiteral("%1 = %2").arg("AppId").arg(AppId());
	strList << QStringLiteral("%1 = %2").arg("Zipcode").arg(m_Zipcode);
	strList << QStringLiteral("%1 = %2").arg("dirty").arg(m_dirty);
	strList << QStringLiteral("%1 = %2").arg("orig").arg(m_orig);
	strList << QStringLiteral("%1 = %2").arg("op").arg(m_op);
	//return strList.join(QStringLiteral("\n"));
	return strList.join(QStringLiteral(", "));
}

//-------------------------------------------------------------------------------
// TesterEditor
//
TesterEditor::TesterEditor(const Tester& tester, bool bnew,
						   IdsEditor* parent)
	: QDialog(parent),
	  m_tester(tester),
	  m_parent(parent),
	  m_TesterCombo(m_parent->TesterCombo())
{
	bool bSet=false;
	ui.setupUi(this);

	RestoreGeometry();

	ui.edtZip->setInputMask( QString("99999;%1").arg(FILL_CHAR) );
	ui.edtAppId->setInputMask(  QString("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH;%1").arg(FILL_CHAR) );

	if(	bnew ){
		ui.edtName->setText("");
		ui.edtName->setEnabled(true);
		ui.chkActive->setChecked(false);
		ui.btnDelete->setVisible(false);
	}
	else{
		ui.edtName->setText(m_tester.Name());
		ui.edtName->setEnabled(false);
		ui.edtAppId->setText(m_tester.AppId());
		ui.edtZip->setText(m_tester.Zip());
		ui.chkActive->setChecked( m_tester.Name() == m_parent->Active() );
		if( !m_tester.AppId().isEmpty() && !m_tester.Zip().isEmpty() ){
			bSet = true;
		}
		ui.btnDelete->setVisible(true);
	}

	m_act = ui.chkActive->isChecked();

	ui.grpWeather->setChecked(bSet);
	ui.WeatherFrame->setVisible(bSet);

	connect(ui.edtName, SIGNAL(editingFinished()), this, SLOT(OnNameChanged()));
	connect(ui.edtAppId, SIGNAL(editingFinished()), this, SLOT(OnAppIdChanged()));
	connect(ui.edtZip, SIGNAL(editingFinished()), this, SLOT(OnZipChanged()));

	connect(ui.edtAppId, SIGNAL(textEdited(QString)), this, SLOT(OnAppIdChanged(QString)));
	connect(ui.edtZip, SIGNAL(textEdited(QString)), this, SLOT(OnZipChanged(QString)));

	connect(ui.grpWeather, SIGNAL(toggled(bool)), this, SLOT(OnWeatherToggled(bool)));
	connect(ui.btnDelete, SIGNAL(clicked()), this, SLOT(OnDelete()));
	connect(ui.buttonBox, SIGNAL(accepted()), this, SLOT(accept()));
	connect(ui.buttonBox, SIGNAL(rejected()), this, SLOT(reject()));
	connect(ui.buttonBox, SIGNAL(clicked(QAbstractButton*)), this, SLOT(OnClickedBtn(QAbstractButton *)));
}

//-------------------------------------------------------------------------------
// ~TesterEditor
//
TesterEditor::~TesterEditor()
{
}

//-------------------------------------------------------------------------------
// RestoreGeometry
//
void TesterEditor::RestoreGeometry()
{
	restoreGeometry(QSettings().value(SK_EDITOR_GEOMETRY).toByteArray());
}

//-------------------------------------------------------------------------------
// SaveGeometry
//
void TesterEditor::SaveGeometry()
{
	QSettings().setValue(SK_EDITOR_GEOMETRY, saveGeometry());
}

//-------------------------------------------------------------------------------
// OnNameChanged
//
void TesterEditor::OnNameChanged(void)
{
	m_tester.Dirty(true);
}

//-------------------------------------------------------------------------------
// OnAppIdChanged
//
void TesterEditor::OnAppIdChanged(QString qs)
{
	if( !qs.isEmpty() )
		OnAppIdChanged();
}
void TesterEditor::OnAppIdChanged(void)
{
	m_tester.Dirty(true);
}

//-------------------------------------------------------------------------------
// OnZipChanged
//
void TesterEditor::OnZipChanged(QString qs)
{
	//qDebug() << "OnZipChanged: " << qs;
	if( !qs.isEmpty() )
		OnZipChanged();
}
void TesterEditor::OnZipChanged(void)
{
	m_tester.Dirty(true);
}

//-------------------------------------------------------------------------------
// OnWeatherToggled
//
void TesterEditor::OnWeatherToggled(bool checked)
{
	ui.WeatherFrame->setVisible(checked);
	m_tester.Dirty(true);
}

//-------------------------------------------------------------------------------
// setTesterData
//
void TesterEditor::setTesterData( QString qsName, QString qsAppid, QString qsZip, DBOP op )
{
	m_tester.Name( qsName );
	m_tester.AppId( qsAppid );
	m_tester.Zip( qsZip );
	m_tester.Op(op);
}

//------------------------------------------------------------------------------
// OnDelete
//
void TesterEditor::OnDelete()
{
	m_tester.Op(DEL);
	done(Accepted);
}

//-------------------------------------------------------------------------------
// accept
//
void TesterEditor::accept()
{
	QString qsName = ui.edtName->displayText();
	if( ui.chkActive->isChecked() ){
		 m_parent->Active(qsName);
	}
	else{ //  were we the Active Tester?
		if( qsName == m_parent->Active() ){
			m_parent->Active( Q_NULLPTR );
		}
	}

	if( m_tester.Dirty() ){ // notihng to do if all was done was toggle Active
		bool bOk = true;
		QString field = "Application Id";
		QString qsAppId = ui.edtAppId->displayText();
		QString qsZip = ui.edtZip->displayText();

		if( ui.grpWeather->isChecked() ){
			bOk = false;
			if( !qsAppId.isEmpty() && !qsAppId.contains(FILL_CHAR) ){
				field = "Zipcode";
				if( !qsZip.isEmpty() && !qsZip.contains(FILL_CHAR) ){
					bOk = true;
				}
			}
		}
		else{
			if( qsAppId.contains(FILL_CHAR) ){
				qsAppId = "";
			}
			if( qsZip.contains(FILL_CHAR) ){
				qsZip = "";
			}
		}
		if( bOk ){
			if(	m_TesterCombo->currentData() == ROLE_NEW_TESTER_KEY ){
				if( !qsName.isEmpty() ){
					if(	m_TesterCombo->findText(qsName,Qt::MatchFixedString) == -1 ){
						m_TesterCombo->insertItem(0, qsName, ROLE_TESTER_KEY);
						m_TesterCombo->setCurrentIndex(0);
						// check to see if orignal of same name was previously
						// deleted and now is being added back
						if( m_parent->Original(qsName) ){
							setTesterData( qsName, qsAppId, qsZip, MOD);
						}
						else{
							setTesterData( qsName, qsAppId, qsZip, ADD);
						}
					} // MatchFixedString
					else{
						field = "Tester Already Exists";
						bOk = false;
					}
				} // name isEmpty
				else{
					field = "Tester Name";
					bOk = false;
				}
			} // new
			else{
				setTesterData( qsName, qsAppId, qsZip, MOD );
			}
		}
		if( !bOk ){
			//done(Rejected);
			QString qs = QStringLiteral("Incomplete Field: %1").arg(field);
			QMessageBox::warning(this, QStringLiteral("IDS Editor"),
								 qs, QMessageBox::Ok, QMessageBox::Ok);
			return;
		}
	}
	else{
		if( m_act != ui.chkActive->isChecked() ){
			// if activeTester state is different than when we started
			// mark dirty for save to DB
			 //m_tester.Dirty(true);
			 m_parent->Modded(false);
		}
	}

	done(Accepted);
}

//-------------------------------------------------------------------------------
// reject
//
void TesterEditor::reject()
{
	done(Rejected);
}

//-------------------------------------------------------------------------------
// OnClicked
//
void TesterEditor::OnClickedBtn(QAbstractButton *button)
{
	QDialogButtonBox::StandardButton stdBtn = ui.buttonBox->standardButton(button);
	switch(stdBtn)
	{
		case QDialogButtonBox::Ok:		// An "OK" button defined with the AcceptRole.
			//qDebug() << "Ok Clicked";
			break;

		case QDialogButtonBox::Cancel:	// A "Cancel" button defined with the RejectRole.
			//qDebug() << "Cancel Clicked";
			break;

		case QDialogButtonBox::Open:	// An "Open" button defined with the AcceptRole.
		case QDialogButtonBox::Close:	// A "Close" button defined with the RejectRole.
		case QDialogButtonBox::Save:	// A "Save" button defined with the AcceptRole.
		case QDialogButtonBox::Discard:	// A "Discard" or "Don't Save" button, depending on the platform, defined with the DestructiveRole.
		case QDialogButtonBox::Apply:	// An "Apply" button defined with the ApplyRole.
		case QDialogButtonBox::Reset:	// A "Reset" button defined with the ResetRole.
		case QDialogButtonBox::RestoreDefaults:	// A "Restore Defaults" button defined with the ResetRole.
		case QDialogButtonBox::Help:	// A "Help" button defined with the HelpRole.
		case QDialogButtonBox::SaveAll:	// A "Save All" button defined with the AcceptRole.
		case QDialogButtonBox::Yes:		// A "Yes" button defined with the YesRole.
		case QDialogButtonBox::YesToAll:// A "Yes to All" button defined with the YesRole.
		case QDialogButtonBox::No:		// A "No" button defined with the NoRole.
		case QDialogButtonBox::NoToAll:	// A "No to All" button defined with the NoRole.
		case QDialogButtonBox::Abort:	// An "Abort" button defined with the RejectRole.
		case QDialogButtonBox::Retry:	// A "Retry" button defined with the AcceptRole.
		case QDialogButtonBox::Ignore:	// An "Ignore" button defined with the AcceptRole.
		case QDialogButtonBox::NoButton:// An invalid button.
		default:
			qDebug() << "Unsupported Button Clicked";
		   break;
	}
}
