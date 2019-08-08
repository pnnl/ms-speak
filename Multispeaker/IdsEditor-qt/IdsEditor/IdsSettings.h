//-------------------------------------------------------------------------------
// This code created by LMI Developments, LLC
//
// Copyright 2019.  All Rights Reserved.
//
//  Created By: Lance Irvine
//
//  IdsSettings
// 

#ifndef IDSSETTINGS_H
#define IDSSETTINGS_H

#include <QDir>
#include <QString>

const QString IDS_EDITOR_HOME_PATH = QStringLiteral("%1/.msspeak-ids").arg(QDir::homePath());
const QString INI_FILE_NAME = QStringLiteral("%1/%2").arg(IDS_EDITOR_HOME_PATH, QStringLiteral("BizRules.cfg"));
const QString IDS_EDITOR_DOCS_FOLDER = QStringLiteral("%1/docs").arg(IDS_EDITOR_HOME_PATH);
const QString IDS_EDITOR_HELP_PDF = QStringLiteral("%1/userguide.pdf").arg(IDS_EDITOR_DOCS_FOLDER);
const QString IDS_EDITOR_HELP_RESOURCE_PDF = QStringLiteral(":/IdsEditor/Resources/userguide.pdf");
const QString LOG_FILE_NAME = QStringLiteral("%1/%2").arg(IDS_EDITOR_HOME_PATH, QStringLiteral("srv_msp.log"));

const QString SK_INI_FILE_NAME = QStringLiteral("sk_ini_file");
const QString SK_LOG_FILE_NAME = QStringLiteral("sk_log_file");
const QString SK_MAIN_GEOMETRY = QStringLiteral("sk_main_geometry");
const QString SK_MAIN_STATE = QStringLiteral("sk_main_state");
const QString SK_RULE_GEOMETRY = QStringLiteral("sk_rule_geometry");

const int ROLE_RULE_KEY = Qt::UserRole + 3;
const int ROLE_SECTION_KEY = Qt::UserRole + 2;

#endif // IDSSETTINGS_H