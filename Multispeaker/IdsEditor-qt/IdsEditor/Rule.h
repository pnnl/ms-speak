//-------------------------------------------------------------------------------
// This code created by LMI Developments, LLC
//
// Copyright 2019.  All Rights Reserved.
//
//  Created By: Lance Irvine
//
//  Rule
// 

#ifndef RULE_H
#define RULE_H

#include <QHash>
#include <QString>

#include "RuleConst.h"

class Rule
{
public:
  QString Name; // Name of rule
  QHash<QString, QString> KeyValue;
public:
  Rule() {}
  Rule(const Rule& rule);
  ~Rule() {}
  void Copy(const Rule& rule);
  QString ToString() const;
};

class RuleSection
{
public:
  QHash<QString, Rule*> Rules; // key is Rule Name, Mem owned here
  QString EndPoint;
  QString Method;

public:
  RuleSection() {}
  RuleSection(const RuleSection& rs);
  ~RuleSection() { qDeleteAll(Rules); }

  void Copy(const RuleSection& rs);

  static Rule* CreateRule(const QString& ruleName);

  QString Section() const;
  QString ToString() const;
};

#endif // RULE_H