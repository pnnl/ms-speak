//-------------------------------------------------------------------------------
// This code created by LMI Developments, LLC
//
// Copyright 2019.  All Rights Reserved.
//
//  Created By: Lance Irvine
//
//  Radics
// 

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

  CreateHomeFolders();

  IdsEditor w;
  w.show();
  return a.exec();
}
