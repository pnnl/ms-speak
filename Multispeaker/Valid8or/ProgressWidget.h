/*-------------------------------------------------------------------------------

  Multi-Speak - Secure Protocol Enterprise Access Kit(MS_SPEAK)
  Copyright © 2018, Battelle Memorial Institute
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
//		2018 - Created By: Carl Miller <carl.miller@pnnl.gov>
//-------------------------------------------------------------------------------
//
// Summary: ProgressWidget.h
//-------------------------------------------------------------------------------

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
	void    valid8Xml(QString s, QString cp, QString e, QString x);

signals:
	void valid8Done(QString m);

private:
	struct OperationInfo {
		QString  output;        // Operation progress output
		QString  elapsedTime;   // Elapsed time
		double   progress{0.0}; // Current value for progress
	};
	
	void    valid8XmlFinishedi(const int iExitCode);
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
