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
//		02.09.2021 CHM - Populate from Sqlite DB, added DB_FILE_NAME.
//-------------------------------------------------------------------------------
// Summary: IdsSettings.h
//-------------------------------------------------------------------------------

#ifndef IDSSETTINGS_H
#define IDSSETTINGS_H

#include <QDir>
#include <QString>

const QString DB_CONNECTION_NAME = QStringLiteral("BizConn");
#ifdef Q_OS_WIN
const QString IDS_EDITOR_HOME_PATH = QStringLiteral("%1/.msspeak-ids").arg(QDir::homePath());
#else
const QString IDS_EDITOR_HOME_PATH = QStringLiteral("/home/msspeak"); // this should be a soft link
#endif
const QString DB_FILE_NAME = QStringLiteral("%1/%2").arg(IDS_EDITOR_HOME_PATH, QStringLiteral("BizRules.db"));
const QString IDS_EDITOR_DOCS_FOLDER = QStringLiteral("%1/docs").arg(IDS_EDITOR_HOME_PATH);
const QString IDS_EDITOR_HELP_PDF = QStringLiteral("%1/userguide.pdf").arg(IDS_EDITOR_DOCS_FOLDER);
const QString IDS_EDITOR_HELP_RESOURCE_PDF = QStringLiteral(":/IdsEditor/Resources/userguide.pdf");

//const QString SK_DB_HOST = QStringLiteral("sk_host");
//const QString SK_DB_FILE_NAME = QStringLiteral("sk_db_file");
const QString SK_MAIN_GEOMETRY = QStringLiteral("sk_main_geometry");
const QString SK_MAIN_STATE = QStringLiteral("sk_main_state");
const QString SK_RULE_GEOMETRY = QStringLiteral("sk_rule_geometry");
const QString SK_EDITOR_GEOMETRY = QStringLiteral("sk_edtr_geometry");

const int ROLE_RULE_KEY = Qt::UserRole + 3;
const int ROLE_REM_KEY = Qt::UserRole + 2;

const int ROLE_NEW_TESTER_KEY = Qt::UserRole + 4;
const int ROLE_TESTER_KEY = ROLE_NEW_TESTER_KEY + 1;

#endif // IDSSETTINGS_H
