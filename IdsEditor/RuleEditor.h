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
//-------------------------------------------------------------------------------
//
// Summary: RuleEditor.h
//-------------------------------------------------------------------------------


#ifndef RULEEDITOR_H
#define RULEEDITOR_H

#include "ui_RuleEditor.h"

#include <QDialog>
#include <QHash>
#include <QStringList>

#include "Rule.h"
#include "IdsEditor.h"

class RuleEditor : public QDialog
{
	Q_OBJECT
	// You use the Q_OBJECT macro to tell the compiler that this class uses
	// its own signals and slots.
private:
	Ui::RuleEditor ui;

	RemObject m_ruleObject;
	IdsEditor *m_parent;
	REMOBJ_HASH& m_ruleObjects;
	DB_HASH& m_functions; // key is a function, value a list of endpoints
	DB_HASH& m_methods;   // key is an endpoint, value a list of methods
	bool	 m_bClosed;
	bool	 m_modded;
	bool	 m_tmpmodded;
	bool	 m_saved;

public:
	RuleEditor(const RemObject& ruleObj, IdsEditor* parent = Q_NULLPTR);
	~RuleEditor();

	const RemObject& RemObj() const { return m_ruleObject; }
	void Modded(bool b){ m_modded=b; }
	bool Modded(void){ return m_modded; }
	void Saved(bool b){ m_saved=b; }
	bool Saved(void){ return m_saved; }

protected:
	virtual void resizeEvent(QResizeEvent* e) { QWidget::resizeEvent(e); SaveGeometry(); }

private:
	void InitFunctions();
	void ChangeFunctionCombo();
	void RestoreGeometry();
	void SaveGeometry();
	void UpdateUi(bool b=false);

private slots:
	void OnEndPointComboChanged(int);
	void OnFunctionComboChanged(int);
	void OnMaxRequestsChanged(int);
	void OnMaxReqPHChanged(int);
	void OnMaxRequestsToggled(bool);
	void OnMaxTempChanged(int);
	void OnMaxTimeChanged(int);
	void OnMethodComboChanged(int);
	void OnMinTempChanged(int);
	void OnMinTimeChanged(int);
	void OnEmailChanged(void);

	void OnTempToggled(bool);
	void OnTimeToggled(bool);
	void OnEmailToggled(bool);

	void OnClickedBtn(QAbstractButton *);
	void accept();
	void reject();
};
#endif // RULEEDITOR_H
