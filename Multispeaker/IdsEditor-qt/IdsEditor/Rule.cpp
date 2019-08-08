//-------------------------------------------------------------------------------
// This code created by LMI Developments, LLC
//
// Copyright 2019.  All Rights Reserved.
//
//  Created By: Lance Irvine
//
//  Rule
// 

#include "Rule.h"

//-------------------------------------------------------------------------------
// Rule::Rule
//
Rule::Rule(const Rule& rule)
  : Name(rule.Name)
{
  for (QString key : rule.KeyValue.keys())
    KeyValue.insert(key, rule.KeyValue.value(key));
}
//-------------------------------------------------------------------------------
// Rule::Copy
//
void Rule::Copy(const Rule& rule)
{
  KeyValue.clear();
  Name = rule.Name;
  for (QString key : rule.KeyValue.keys())
    KeyValue.insert(key, rule.KeyValue.value(key));
}
//-------------------------------------------------------------------------------
// Rule::ToString
//
QString Rule::ToString() const
{
  QStringList strList;
  for (QString key : KeyValue.keys())
  {
    strList << QStringLiteral("%1 = %2")
      .arg(key)
      .arg(KeyValue.value(key));
  }
  return strList.join(QStringLiteral("\n"));
}
//-------------------------------------------------------------------------------
// RuleSection::RuleSection
//
RuleSection::RuleSection(const RuleSection& rs)
 : EndPoint(rs.EndPoint),
  Method(rs.Method)
{
  for (Rule* rule : rs.Rules)
    Rules.insert(rule->Name, new Rule(*rule));
}
//-------------------------------------------------------------------------------
// RuleSection::Copy
//
void RuleSection::Copy(const RuleSection& rs)
{
  EndPoint = rs.EndPoint;
  Method = rs.Method;
  qDeleteAll(Rules);
  Rules.clear();

  for (Rule* rule : rs.Rules)
    Rules.insert(rule->Name, new Rule(*rule));
}
//-------------------------------------------------------------------------------
// RuleSection::CreateRule
//
Rule* RuleSection::CreateRule(const QString& ruleName)
{
  Rule* rule = new Rule();
  if (ruleName == RULE_TYPE_MAX_VALUE)
  {
    rule->Name = ruleName;
    rule->KeyValue.insert(RULE_KEY_NUMREQ, QStringLiteral("0"));
  }
  else if (ruleName == RULE_TYPE_TEMP_RANGE)
  {
    rule->Name = ruleName;
    rule->KeyValue.insert(RULE_KEY_MAXTEMP, QStringLiteral("0"));
    rule->KeyValue.insert(RULE_KEY_MINTEMP, QStringLiteral("0"));
  }
  else if (ruleName == RULE_TYPE_TIME_RANGE)
  {
    rule->Name = ruleName;
    rule->KeyValue.insert(RULE_KEY_MAXTIME, QStringLiteral("0"));
    rule->KeyValue.insert(RULE_KEY_MINTIME, QStringLiteral("0"));
  }
  return rule;
}
//-------------------------------------------------------------------------------
// RuleSection::Section
//
QString RuleSection::Section() const
{
  return QStringLiteral("[%1@%2]")
    .arg(Method, EndPoint);
}
//-------------------------------------------------------------------------------
// RuleSection::ToString
//
QString RuleSection::ToString() const
{
  QStringList strList;
  strList << Section();
  for (Rule* rule : Rules)
    strList << rule->ToString();

  return strList.join(QStringLiteral("\n"));
}
