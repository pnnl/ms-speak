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
// Summary: main.cpp
//-------------------------------------------------------------------------------

#include <QApplication>
#include <QDebug>
#include <QDir>
#include <QFile>

#include "IdsEditor.h"
#include "IdsSettings.h"

//------------------------------------------------------------------------------
// WriteDefaultResourceFile
//
void WriteDefaultResourceFile(const QString& src, const QString& dst)
{
	// Save default file from resources to a physical file
	QFile file(src);
	QFile::FileError error = file.error();
	if (error != QFile::NoError)
	{
		qCritical() << src << error;
		qCritical() << QStringLiteral("Can't Open Default File from Resource, %1").arg(src);
	}
	else
	{
		file.copy(dst);
		if (error != QFile::NoError)
		{
			qCritical() << dst << error;
			qCritical() << QStringLiteral("Copying default file, %1, failed.\n\n%2").arg(dst).arg(error);
		}
		else
		{
			if (!QFile::setPermissions(dst, QFile::ReadOwner | QFile::WriteOwner))
				qCritical() << QStringLiteral("Set Permissions Failed after Copying default file, %1").arg(dst);
		}
	}
}
//------------------------------------------------------------------------------
// CreateHomeFolders
//
void CreateHomeFolders()
{
	// .msspeak-ids
	QDir home(IDS_EDITOR_HOME_PATH);
	if (!home.exists())
	{
		if (!home.mkdir(IDS_EDITOR_HOME_PATH))
			qCritical() << QStringLiteral("Can not create directory structure for ") << QDir::toNativeSeparators(IDS_EDITOR_HOME_PATH);
	}

	// .msspeak-ids/docs
	QDir docs(IDS_EDITOR_DOCS_FOLDER);
	if (!docs.exists())
	{
		if (!docs.mkdir(IDS_EDITOR_DOCS_FOLDER))
			qCritical() << QStringLiteral("Can not create directory structure for ") << IDS_EDITOR_DOCS_FOLDER;
	}
	if (docs.exists())
		WriteDefaultResourceFile(IDS_EDITOR_HELP_RESOURCE_PDF, IDS_EDITOR_HELP_PDF); // Always write file
}
//------------------------------------------------------------------------------
// main
//
int main(int argc, char *argv[])
{
	QApplication a(argc, argv);

	QCoreApplication::setOrganizationName(QStringLiteral("MSSPEAK-IDS"));
	QCoreApplication::setOrganizationDomain(QStringLiteral("MSSPEAK-IDS.com"));
	QCoreApplication::setApplicationName(QStringLiteral("IdsEditor"));
	
	QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling); // 5.20.2021, AA_DisableHighDpiScaling
	
	CreateHomeFolders();
	int ret;
	{
		IdsEditor w;
		w.show();
		ret = a.exec();
	}
	/*
	 * The SqlDatabase object needs to go out of scope before you can call
	 * removeDatabase, else get:
	 *		QSqlDatabasePrivate::removeDatabase: connection 'BizConn' is still
	 *			in use, all queries will cease to work.
	 *
	 *	Both "m_db" and any "query" are destroyed because they are now out of scope
	 */
	QSqlDatabase::removeDatabase(DB_CONNECTION_NAME);
	return ret;
}
