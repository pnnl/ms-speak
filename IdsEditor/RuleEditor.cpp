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
//		02.12.2021 CHM - Populate from Sqlite DB.
//-------------------------------------------------------------------------------
//
// Summary: RuleEditor.cpp
//-------------------------------------------------------------------------------

#include <QDebug>
#include <QHash>
#include <QSettings>
#include <QVariant>
//#include <QRegularExpression>
#include <QMessageBox>

#include "IdsSettings.h"
#include "RuleConst.h"
#include "RuleEditor.h"

//-------------------------------------------------------------------------------
// RuleEditor
//
RuleEditor::RuleEditor(const RemObject& ruleObj, IdsEditor* parent)
	: QDialog(parent),
	  m_ruleObject(ruleObj),
	  m_parent(parent),
	  m_ruleObjects(parent->RemObjects()),
	  m_functions(parent->Functions()),
	  m_methods(parent->Methods()),
	  m_bClosed(false),
	  m_modded(false),
	  m_tmpmodded(false),
	  m_saved(false)
{
	ui.setupUi(this);

	RestoreGeometry();

	ui.MaxRequestsFrame->setVisible(false);
	ui.TempFrame->setVisible(false);
	ui.TimeFrame->setVisible(false);
	ui.EmailFrame->setVisible(false);

	InitFunctions();
	UpdateUi(true);

	/*QRegularExpression mailREX("\\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[A-Z]{2,4}\\b");
	QValidator *validator = new QRegularExpressionValidator(mailREX, this);
	ui.Email->setValidator(validator);*/

	// Group Toggle connections before SetRule
	connect(ui.MaxRequestsGroup, SIGNAL(toggled(bool)), this, SLOT(OnMaxRequestsToggled(bool)));
	connect(ui.TempGroup, SIGNAL(toggled(bool)), this, SLOT(OnTempToggled(bool)));
	connect(ui.TimeGroup, SIGNAL(toggled(bool)), this, SLOT(OnTimeToggled(bool)));
	connect(ui.EmailGroup, SIGNAL(toggled(bool)), this, SLOT(OnEmailToggled(bool)));

	connect(ui.Email, SIGNAL(editingFinished()), this, SLOT(OnEmailChanged()));
	connect(ui.EndPointCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnEndPointComboChanged(int)));
	connect(ui.FunctionCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnFunctionComboChanged(int)));
	connect(ui.MethodCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnMethodComboChanged(int)));
	connect(ui.MaxRequestsSpin, SIGNAL(valueChanged(int)), this, SLOT(OnMaxRequestsChanged(int)));
	connect(ui.MaxReqPHSpin, SIGNAL(valueChanged(int)), this, SLOT(OnMaxReqPHChanged(int)));
	connect(ui.MaxTempSlider, SIGNAL(valueChanged(int)), ui.MaxTempSpin, SLOT(setValue(int)));
	connect(ui.MaxTempSlider, SIGNAL(valueChanged(int)), this, SLOT(OnMaxTempChanged(int)));

	/*
	 * With a QSpinbox Qt Internal code uses a timer on clicks/presses. If you step through in debugger
	 * you exceed the timeout and get bad/double behaviour.
	 *
	 * Simplest: change all connect() to QSpinbox click/key to pass Qt::QueuedConnection as last
	 * parameter for connection type, not default Qt::DirectConnection.
	 *
	 * the double call only happens on spinners that also have a slider
	 */
	connect(ui.MaxTempSpin, SIGNAL(valueChanged(int)), ui.MaxTempSlider, SLOT(setValue(int)));
	connect(ui.MaxTempSpin, SIGNAL(valueChanged(int)), this, SLOT(OnMaxTempChanged(int)));
	connect(ui.MinTempSlider, SIGNAL(valueChanged(int)), ui.MinTempSpin, SLOT(setValue(int)));
	connect(ui.MinTempSlider, SIGNAL(valueChanged(int)), this, SLOT(OnMinTempChanged(int)));
	connect(ui.MinTempSpin, SIGNAL(valueChanged(int)), ui.MinTempSlider, SLOT(setValue(int)));
	connect(ui.MinTempSpin, SIGNAL(valueChanged(int)), this, SLOT(OnMinTempChanged(int)));

	connect(ui.MaxTimeSlider, SIGNAL(valueChanged(int)), ui.MaxTimeSpin, SLOT(setValue(int)));
	connect(ui.MaxTimeSlider, SIGNAL(valueChanged(int)), this, SLOT(OnMaxTimeChanged(int)));
	connect(ui.MaxTimeSpin, SIGNAL(valueChanged(int)), ui.MaxTimeSlider, SLOT(setValue(int)));
	connect(ui.MaxTimeSpin, SIGNAL(valueChanged(int)), this, SLOT(OnMaxTimeChanged(int)));
	connect(ui.MinTimeSlider, SIGNAL(valueChanged(int)), ui.MinTimeSpin, SLOT(setValue(int)));
	connect(ui.MinTimeSlider, SIGNAL(valueChanged(int)), this, SLOT(OnMinTimeChanged(int)));
	connect(ui.MinTimeSpin, SIGNAL(valueChanged(int)), ui.MinTimeSlider, SLOT(setValue(int)));
	connect(ui.MinTimeSpin, SIGNAL(valueChanged(int)), this, SLOT(OnMinTimeChanged(int)));

	connect(ui.buttonBox, SIGNAL(accepted()), this, SLOT(accept()));
	connect(ui.buttonBox, SIGNAL(rejected()), this, SLOT(reject()));

	connect(ui.buttonBox, SIGNAL(clicked(QAbstractButton*)), this, SLOT(OnClickedBtn(QAbstractButton *)));
}

//-------------------------------------------------------------------------------
// ~RuleEditor
//
RuleEditor::~RuleEditor()
{
}

//-------------------------------------------------------------------------------
// InitFunctions
//
void RuleEditor::InitFunctions()
{
	QStringList qsl = QStringList();
	QHash<QString, QStringList>::const_iterator it = m_functions.constBegin();
	for (it = m_functions.constBegin(); it != m_functions.constEnd(); ++it)
		qsl << it.key();
	qsl.sort();
	QStringList::const_iterator it2;
	for (it2 = qsl.constBegin(); it2 != qsl.constEnd(); ++it2){
		ui.FunctionCombo->addItem(*it2,m_functions[*it2]);
	}
}

//-------------------------------------------------------------------------------
// RestoreGeometry
//
void RuleEditor::RestoreGeometry()
{
	restoreGeometry(QSettings().value(SK_RULE_GEOMETRY).toByteArray());
}

//-------------------------------------------------------------------------------
// SaveGeometry
//
void RuleEditor::SaveGeometry()
{
	QSettings().setValue(SK_RULE_GEOMETRY, saveGeometry());
}

//-------------------------------------------------------------------------------
// UpdateUi
//
void RuleEditor::UpdateUi( bool init )
{
	if( !init )
		m_tmpmodded = true;

	QString function = m_ruleObject.m_Function;
	// Set up the combos based on rule
	disconnect(ui.EndPointCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnEndPointComboChanged(int)));
	disconnect(ui.FunctionCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnFunctionComboChanged(int)));
	disconnect(ui.MethodCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnMethodComboChanged(int)));
	disconnect(ui.Email, SIGNAL(editingFinished()), this, SLOT(OnEmailChanged()));

	ui.MethodCombo->clear();
	ui.EndPointCombo->clear();
	ui.FunctionCombo->setCurrentIndex(ui.FunctionCombo->findText(function));

	// EndPoint
	QStringList endPointList = ui.FunctionCombo->currentData().toStringList();
	for( const QString & ep : qAsConst(endPointList) )
		ui.EndPointCombo->addItem(ep, m_methods.value(ep));

	int idx = ui.EndPointCombo->findText( m_ruleObject.m_EndPoint);
	if (idx < 0)
	{
		ui.EndPointCombo->setCurrentIndex(0); // First one
		m_ruleObject.m_EndPoint = ui.EndPointCombo->currentText();
	}
	else
	{
		ui.EndPointCombo->setCurrentIndex(idx);
	}

	// Method
	QStringList methodList = ui.EndPointCombo->currentData().toStringList();
	for( const QString & method : qAsConst(methodList))
		ui.MethodCombo->addItem(method);

	idx = ui.MethodCombo->findText( m_ruleObject.m_Method);
	if (idx < 0)
	{
		ui.MethodCombo->setCurrentIndex(0); // First one
		m_ruleObject.m_Method = ui.MethodCombo->currentText();
	}
	else
	{
		ui.MethodCombo->setCurrentIndex(idx);
	}

	connect(ui.EndPointCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnEndPointComboChanged(int)));
	connect(ui.FunctionCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnFunctionComboChanged(int)));
	connect(ui.MethodCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnMethodComboChanged(int)));
	connect(ui.Email, SIGNAL(editingFinished()), this, SLOT(OnEmailChanged()));

	// Check for rules
	for (Rule* rule : m_ruleObject.Rules)
	{
		if (rule->Name == RULE_TYPE_MAX_VALUE)
		{
			ui.MaxRequestsGroup->setChecked(true);
			ui.MaxRequestsFrame->setVisible(true);
			ui.MaxRequestsSpin->setValue(rule->KeyValue.value(RULE_KEY_NUMREQ).toInt());

			QHash<QString, QString>::iterator i = rule->KeyValue.find(RULE_KEY_NUMRPH);
			if (i != rule->KeyValue.end()) {
				ui.MaxReqPHSpin->setValue(rule->KeyValue.value(RULE_KEY_NUMRPH).toInt());
			}
		}
		else if (rule->Name == RULE_TYPE_TEMP_RANGE)
		{
			ui.TempGroup->setChecked(true);
			ui.TempFrame->setVisible(true);
			ui.MaxTempSpin->setValue(rule->KeyValue.value(RULE_KEY_MAXTEMP).toInt());
			ui.MaxTempSlider->setValue(rule->KeyValue.value(RULE_KEY_MAXTEMP).toInt());
			ui.MinTempSpin->setValue(rule->KeyValue.value(RULE_KEY_MINTEMP).toInt());
			ui.MinTempSlider->setValue(rule->KeyValue.value(RULE_KEY_MINTEMP).toInt());
		}
		else if (rule->Name == RULE_TYPE_TIME_RANGE)
		{
			ui.TimeGroup->setChecked(true);
			ui.TimeFrame->setVisible(true);
			ui.MaxTimeSpin->setValue(rule->KeyValue.value(RULE_KEY_MAXTIME).toInt());
			ui.MaxTimeSlider->setValue(rule->KeyValue.value(RULE_KEY_MAXTIME).toInt());
			ui.MinTimeSpin->setValue(rule->KeyValue.value(RULE_KEY_MINTIME).toInt());
			ui.MinTimeSlider->setValue(rule->KeyValue.value(RULE_KEY_MINTIME).toInt());
		}
		else if (rule->Name == RULE_TYPE_EMAIL)
		{
			ui.EmailGroup->setChecked(true);
			/* As far as I know, QtCreator makes functions italic that are either
			 *		Virtual methods (e.g. "virtual void foo();" ), or
			 *		methods that are derived from a base class and then overridden
			 *			in the child class (however, i'm not sure if it only happens
			 *			if they are derived "virtual", or if there are other corner cases where
			 *			overridden methods are not italic)
			 */
			ui.EmailFrame->setVisible(true);
			ui.Email->setText(rule->KeyValue.value(RULE_KEY_EMAIL));
		}
	}
}

//-------------------------------------------------------------------------------
// OnFunctionComboChanged
//
void RuleEditor::OnFunctionComboChanged(int index)
{
	Q_UNUSED(index);
	QString function = ui.FunctionCombo->currentText();
	m_ruleObject.m_Function = function;
	m_ruleObject.m_EndPoint = m_functions[function].first();
	m_ruleObject.m_Method = m_methods.value( m_ruleObject.m_EndPoint).first();
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnEndPointComboChanged
//
void RuleEditor::OnEndPointComboChanged(int index)
{
	if (ui.EndPointCombo->count() <= 0)
		return;

	m_ruleObject.m_EndPoint = ui.EndPointCombo->itemText(index);
	m_ruleObject.m_Method = m_methods.value( m_ruleObject.m_EndPoint).first();
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnMethodComboChanged
//
void RuleEditor::OnMethodComboChanged(int index)
{
	Q_UNUSED(index);
	if (ui.MethodCombo->count() <= 0)
		return;
	m_ruleObject.m_Method = ui.MethodCombo->currentText();
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnEmailChanged
//
void RuleEditor::OnEmailChanged(void)
{
	QString qs = ui.Email->displayText();
	//qDebug() << "Email Address Set to: " << qs;
	m_ruleObject.Rules.value(RULE_TYPE_EMAIL)->KeyValue.insert(RULE_KEY_EMAIL, qs);
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnMaxRequestsChanged
//
void RuleEditor::OnMaxRequestsChanged(int value)
{
	//qDebug() << "OnMaxRequestsChanged: " << value;
	if( value < ui.MaxReqPHSpin->value() )
	{
		ui.MaxReqPHSpin->setValue(value);
	}
	m_ruleObject.Rules.value(RULE_TYPE_MAX_VALUE)->KeyValue.insert(RULE_KEY_NUMREQ, QString::number(value));
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnMaxReqPHChanged
//
void RuleEditor::OnMaxReqPHChanged(int value)
{
	//qDebug() << "OnMaxReqPHChanged: " << value;
	if( value > ui.MaxRequestsSpin->value() )
	{
		ui.MaxRequestsSpin->setValue(value);
	}
	if( value > 0 )
	{
		m_ruleObject.Rules.value(RULE_TYPE_MAX_VALUE)->KeyValue.insert(RULE_KEY_NUMRPH, QString::number(value));
	}
	else{
		m_ruleObject.Rules.value(RULE_TYPE_MAX_VALUE)->KeyValue.remove(RULE_KEY_NUMRPH);
		ui.MaxReqPHSpin->setValue(0);
	}
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnMaxTempChanged
//
void RuleEditor::OnMaxTempChanged(int value)
{
	//qDebug() << "OnMaxTempChanged: " << value;
	if (value < ui.MinTempSlider->value() || value < ui.MinTempSpin->value())
	{
		ui.MinTempSlider->setValue(value);
		ui.MinTempSpin->setValue(value);
	}
	m_ruleObject.Rules.value(RULE_TYPE_TEMP_RANGE)->KeyValue.insert(RULE_KEY_MAXTEMP, QString::number(value));
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnMinTempChanged
//
void RuleEditor::OnMinTempChanged(int value)
{
	//qDebug() << "OnMinTempChanged: " << value;
	if (value > ui.MaxTempSlider->value() || value > ui.MaxTempSpin->value())
	{
		ui.MaxTempSlider->setValue(value);
		ui.MaxTempSpin->setValue(value);
	}
	m_ruleObject.Rules.value(RULE_TYPE_TEMP_RANGE)->KeyValue.insert(RULE_KEY_MINTEMP, QString::number(value));
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnMaxTimeChanged
//
void RuleEditor::OnMaxTimeChanged(int value)
{
	//qDebug() << "OnMaxTimeChanged: " << value;
	if (value < ui.MinTimeSlider->value() || value < ui.MinTimeSpin->value())
	{
		ui.MinTimeSlider->setValue(value);
		ui.MinTimeSpin->setValue(value);
	}
	m_ruleObject.Rules.value(RULE_TYPE_TIME_RANGE)->KeyValue.insert(RULE_KEY_MAXTIME, QString::number(value));
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnMinTimeChanged
//
void RuleEditor::OnMinTimeChanged(int value)
{
	//qDebug() << "OnMinTimeChanged: " << value;
	if (value > ui.MaxTimeSlider->value() || value > ui.MaxTimeSpin->value())
	{
		ui.MaxTimeSlider->setValue(value);
		ui.MaxTimeSpin->setValue(value);
	}
	m_ruleObject.Rules.value(RULE_TYPE_TIME_RANGE)->KeyValue.insert(RULE_KEY_MINTIME, QString::number(value));
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnMaxRequestsToggled
//
void RuleEditor::OnMaxRequestsToggled(bool checked)
{
	ui.MaxRequestsFrame->setVisible(checked);
	if (checked)
	{
		Rule* rule = RemObject::CreateRule(RULE_TYPE_MAX_VALUE);
		rule->KeyValue.insert(RULE_KEY_NUMREQ, QString::number(ui.MaxRequestsSpin->value()));
		if( ui.MaxReqPHSpin->value() > 0 ){
			rule->KeyValue.insert(RULE_KEY_NUMRPH, QString::number(ui.MaxReqPHSpin->value()));
		}
		m_ruleObject.Rules.insert(RULE_TYPE_MAX_VALUE, rule);
	}
	else
	{
		delete m_ruleObject.Rules.take(RULE_TYPE_MAX_VALUE);
	}
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnTempToggled
//
void RuleEditor::OnTempToggled(bool checked)
{
	ui.TempFrame->setVisible(checked);
	if (checked)
	{
		Rule* rule = RemObject::CreateRule(RULE_TYPE_TEMP_RANGE);
		rule->KeyValue.insert(RULE_KEY_MAXTEMP, QString::number(ui.MaxTempSpin->value()));
		rule->KeyValue.insert(RULE_KEY_MINTEMP, QString::number(ui.MinTempSpin->value()));
		m_ruleObject.Rules.insert(RULE_TYPE_TEMP_RANGE, rule);
	}
	else
	{
		delete m_ruleObject.Rules.take(RULE_TYPE_TEMP_RANGE);
	}
	UpdateUi();
}

//-------------------------------------------------------------------------------
// OnTimeToggled
//
void RuleEditor::OnTimeToggled(bool checked)
{
	ui.TimeFrame->setVisible(checked);
	if (checked)
	{
		Rule* rule = RemObject::CreateRule(RULE_TYPE_TIME_RANGE);
		rule->KeyValue.insert(RULE_KEY_MAXTIME, QString::number(ui.MaxTimeSpin->value()));
		rule->KeyValue.insert(RULE_KEY_MINTIME, QString::number(ui.MinTimeSpin->value()));
		m_ruleObject.Rules.insert(RULE_TYPE_TIME_RANGE, rule);
	}
	else
	{
		delete m_ruleObject.Rules.take(RULE_TYPE_TIME_RANGE);
	}
	UpdateUi();
}


//-------------------------------------------------------------------------------
// OnEmailToggled
//
void RuleEditor::OnEmailToggled(bool checked)
{
	ui.EmailFrame->setVisible(checked);
	if (checked)
	{
		Rule* rule = RemObject::CreateRule(RULE_TYPE_EMAIL);
		rule->KeyValue.insert(RULE_KEY_EMAIL, ui.Email->displayText());
		m_ruleObject.Rules.insert(RULE_TYPE_EMAIL, rule);
	}
	else
	{
		delete m_ruleObject.Rules.take(RULE_TYPE_EMAIL);
	}
	UpdateUi();
}

//-------------------------------------------------------------------------------
// accept - only called on click of 'Save'
//
void RuleEditor::accept()
{
	if( m_tmpmodded )
	{
		//qDebug() << "accept()::m_modded";
		// m_ruleObject.Copy(Section());
		QString objectKey = m_ruleObject.Rem();
		if ( m_ruleObjects.contains(objectKey)){
			//qDebug() << "accept() delete " << objectKey;
			delete m_ruleObjects.take(objectKey);
		}
		m_ruleObjects.insert(objectKey, new RemObject( m_ruleObject));
		m_tmpmodded = false;
		m_modded = true;
		m_parent->Modded(true);
		m_parent->UpdateObjectModel(objectKey);
	}
	//else{
	//	qDebug() << "accept():: NOT modded";
	//}
}

//-------------------------------------------------------------------------------
// accept
//
void RuleEditor::reject()
{
	//qDebug() << "reject()";
	if( m_bClosed ){
		//qDebug() << "reject(Accepted)";
		accept();
		done(Accepted);
	}
	else{
		//qDebug() << "reject(Reject)";
		done(Rejected);
	}
}

//-------------------------------------------------------------------------------
// OnClicked
//
void RuleEditor::OnClickedBtn(QAbstractButton *button)
{
	QDialogButtonBox::StandardButton stdBtn = ui.buttonBox->standardButton(button);
	switch(stdBtn)
	{
		case QDialogButtonBox::Cancel:	// A "Cancel" button defined with the RejectRole.
			//qDebug() << "Cancel Clicked";
			break;
		case QDialogButtonBox::Close:	// A "Close" button defined with the RejectRole.
			//qDebug() << "Close Clicked";
			m_bClosed = true;
			break;
		case QDialogButtonBox::Save:	// A "Save" button defined with the AcceptRole.
			//qDebug() << "Save Clicked";
			//QDialog::reject();
			m_saved = true;
			break;

		case QDialogButtonBox::Ok:		// An "OK" button defined with the AcceptRole.
		case QDialogButtonBox::Open:	// An "Open" button defined with the AcceptRole.
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
