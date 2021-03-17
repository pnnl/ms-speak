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
	//return strList.join(QStringLiteral("\n"));
	return strList.join(QStringLiteral(", "));
}

//-------------------------------------------------------------------------------
// RemObject::RemObject
//
RemObject::RemObject(const RemObject& rs)
	: m_Function(rs.m_Function),
	  m_EndPoint(rs.m_EndPoint),
	  m_Method(rs.m_Method)
{
	for (Rule* rule : rs.Rules)
		Rules.insert(rule->Name, new Rule(*rule));
}

//-------------------------------------------------------------------------------
// RemObject::Copy
//
void RemObject::Copy(const RemObject& rs)
{
	m_Function = rs.m_Function;
	m_EndPoint = rs.m_EndPoint;
	m_Method = rs.m_Method;
	qDeleteAll(Rules);
	Rules.clear();

	for (Rule* rule : rs.Rules)
		Rules.insert(rule->Name, new Rule(*rule));
}

//-------------------------------------------------------------------------------
// RemObject::CreateRule
//
Rule* RemObject::CreateRule(const QString& ruleName)
{
	Rule* rule = new Rule();
	if (ruleName == RULE_TYPE_MAX_VALUE)
	{
		rule->Name = ruleName;
		rule->KeyValue.insert(RULE_KEY_NUMREQ, QStringLiteral("0"));
		rule->KeyValue.insert(RULE_KEY_NUMRPH, QStringLiteral("0"));
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
	else if (ruleName == RULE_TYPE_EMAIL)
	{
		rule->Name = ruleName;
		rule->KeyValue.insert(RULE_KEY_EMAIL, QStringLiteral(""));
	}
	return rule;
}

//-------------------------------------------------------------------------------
// RemObject::Rem
//
QString RemObject::Rem() const
{
	//return QStringLiteral("[%1@%2]").arg(Method, EndPoint);
	//return QStringLiteral("%1::%2").arg(Method, EndPoint);
	//return QStringLiteral("%1::%2").arg(EndPoint, Method);
	return QStringLiteral("%1::%2").arg(m_EndPoint, m_Method);
}

//-------------------------------------------------------------------------------
// RemObject::ToString
//
QString RemObject::ToString() const
{
	QStringList strList;
	strList << Rem();
	for (Rule* rule : Rules)
		strList << rule->ToString();

	return strList.join(QStringLiteral("\n"));
}
