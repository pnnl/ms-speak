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
// TesterEditor
//
TesterEditor::TesterEditor(IdsEditor* parent)
	: QDialog(parent),
	  m_parent(parent),
	  cmbTesters(m_parent->Testers()),
	  m_bWeather(false)
{
	ui.setupUi(this);

	RestoreGeometry();

	ui.edtZip->setInputMask( QString("99999;%1").arg(FILL_CHAR) );
	ui.edtAppId->setInputMask(  QString("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH;%1").arg(FILL_CHAR) );
	ui.WeatherFrame->setVisible(false);

	if(	cmbTesters->currentData() == ROLE_NEW_TESTER_KEY ){
		ui.edtName->setText("");
		ui.edtName->setEnabled(true);
	}
	else{
		ui.edtName->setText(cmbTesters->currentText());
		ui.edtName->setEnabled(false);
	}

	UpdateUi();

	connect(ui.edtName, SIGNAL(editingFinished()), this, SLOT(OnNameChanged()));
	connect(ui.edtAppId, SIGNAL(editingFinished()), this, SLOT(OnAppIdChanged()));
	connect(ui.edtZip, SIGNAL(editingFinished()), this, SLOT(OnZipChanged()));

	connect(ui.grpWeather, SIGNAL(toggled(bool)), this, SLOT(OnWeatherToggled(bool)));
	connect(ui.chkActive, SIGNAL(toggled(bool)), this, SLOT(OnActiveToggled(bool)));

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
// UpdateUi
//
void TesterEditor::UpdateUi()
{
	disconnect(ui.edtName, SIGNAL(editingFinished()), this, SLOT(OnNameChanged()));
	disconnect(ui.edtAppId, SIGNAL(editingFinished()), this, SLOT(OnAppIdChanged()));
	disconnect(ui.edtZip, SIGNAL(editingFinished()), this, SLOT(OnZipChanged()));
	// do something....
	connect(ui.edtName, SIGNAL(editingFinished()), this, SLOT(OnNameChanged()));
	connect(ui.edtAppId, SIGNAL(editingFinished()), this, SLOT(OnAppIdChanged()));
	connect(ui.edtZip, SIGNAL(editingFinished()), this, SLOT(OnZipChanged()));
}

//-------------------------------------------------------------------------------
// OnNameChanged
//
void TesterEditor::OnNameChanged(void)
{
	QString qs = ui.edtName->displayText();
	qDebug() << "Test Name Set to: " << qs;
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnAppIdChanged
//
void TesterEditor::OnAppIdChanged(void)
{
	QString qs = ui.edtAppId->displayText();
	qDebug() << "Application Id Set to: " << qs;
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnZipChanged
//
void TesterEditor::OnZipChanged(void)
{
	QString qs = ui.edtZip->displayText();
	qDebug() << "Zipcode Set to: " << qs;
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnActiveToggled
//
void TesterEditor::OnActiveToggled(bool checked)
{
	if (checked)
	{
		// ui.chkActive
	}
	else
	{
	}
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnWeatherToggled
//
void TesterEditor::OnWeatherToggled(bool checked)
{
	ui.WeatherFrame->setVisible(checked);
	if (checked)
	{
		m_bWeather = true;
	}
	else
	{
		m_bWeather = false;
	}
	UpdateUi();
}


//-------------------------------------------------------------------------------
// accept
//
void TesterEditor::accept()
{
	bool bOk = true;
	QString field = "Application Id";
	QString qs = ui.edtAppId->displayText();

	if( m_bWeather ){
		bOk = false;
		if( !qs.isEmpty() && !qs.contains(FILL_CHAR) ){
			field = "Zipcode";
			qs = ui.edtZip->displayText();
			if( !qs.isEmpty() && !qs.contains(FILL_CHAR) ){
				bOk = true;
			}
		}
	}

	if( bOk ){
		if(	cmbTesters->currentData() == ROLE_NEW_TESTER_KEY ){
			qs = ui.edtName->displayText();
			if( !qs.isEmpty() ){
				if(	cmbTesters->findText(qs,Qt::MatchFixedString) == -1 ){
					cmbTesters->insertItem(0, qs, ROLE_TESTER_KEY);
					cmbTesters->setCurrentIndex(0);
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
			// todo: how handle DELETE ?
			// void	removeItem(int index)
		}
	}
	if( !bOk ){
		qDebug() << "Rejected()";
		//done(Rejected);
		QString qs = QStringLiteral("Incomplete Field: %1").arg(field);
		QMessageBox::warning(this, QStringLiteral("IDS Editor"),
							 qs, QMessageBox::Ok, QMessageBox::Ok);
		return;
	}
	qDebug() << "accept()";
	done(Accepted);
}

//-------------------------------------------------------------------------------
// accept
//
void TesterEditor::reject()
{
	qDebug() << "reject(Reject)";
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
			qDebug() << "Ok Clicked";
			break;

		case QDialogButtonBox::Cancel:	// A "Cancel" button defined with the RejectRole.
			qDebug() << "Cancel Clicked";
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
