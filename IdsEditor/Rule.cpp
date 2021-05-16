//-------------------------------------------------------------------------------
// This code created by LMI Developments, LLC
//
// Copyright 2019.  All Rights Reserved.
//
//  Created By: Lance Irvine
//
//  Rule
// 
#include <QDebug>

#include "Rule.h"

//-------------------------------------------------------------------------------
// RuleData::RuleData
//
RuleData::RuleData(void)
{
	clear();
}

//-------------------------------------------------------------------------------
// RuleData::clear
//
void RuleData::clear(void)
{
	m_Tester = DB_NO_VALUE;
	m_Function = DB_NO_VALUE;
	m_Endpoint = DB_NO_VALUE;
	m_Method = DB_NO_VALUE;
	m_email = DB_NO_VALUE;
	m_maxTemp = DB_NO_VALUE;
	m_minTemp = DB_NO_VALUE;
	m_maxHour = DB_NO_VALUE;
	m_minHour = DB_NO_VALUE;
	m_numReq = DB_NO_VALUE;
	m_numRPH = DB_NO_VALUE;
}

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
	rule->Name = ruleName;
	if (ruleName == RULE_TYPE_MAX_REQ)
	{
		rule->KeyValue.insert(RULE_KEY_NUMREQ, QStringLiteral("0"));
	}
	else if (ruleName == RULE_TYPE_MAX_RPH)
	{
		rule->KeyValue.insert(RULE_KEY_NUMRPH, QStringLiteral("1"));
	}
	else if (ruleName == RULE_TYPE_TEMP_RANGE)
	{
		rule->KeyValue.insert(RULE_KEY_MAXTEMP, QStringLiteral("1"));
		rule->KeyValue.insert(RULE_KEY_MINTEMP, QStringLiteral("0"));
	}
	else if (ruleName == RULE_TYPE_TIME_RANGE)
	{
		rule->KeyValue.insert(RULE_KEY_MAXTIME, QStringLiteral("1"));
		rule->KeyValue.insert(RULE_KEY_MINTIME, QStringLiteral("0"));
	}
	else if (ruleName == RULE_TYPE_EMAIL)
	{
		rule->KeyValue.insert(RULE_KEY_EMAIL, QStringLiteral(""));
	}
	return rule;
}

//-------------------------------------------------------------------------------
// RemObject::getData
//
void RemObject::getData( RuleData& rd, QString tstr )
{
	rd.clear();

	rd.m_Tester = tstr;
	rd.m_Function = m_Function;
	rd.m_Endpoint = m_EndPoint;
	rd.m_Method   = m_Method;

	for (Rule* rule : Rules){
		if (rule->Name == RULE_TYPE_MAX_REQ)
		{
			rd.m_numReq = rule->KeyValue[RULE_KEY_NUMREQ];
		}
		else if (rule->Name == RULE_TYPE_MAX_RPH)
		{
			rd.m_numRPH = rule->KeyValue[RULE_KEY_NUMRPH];
		}
		else if (rule->Name == RULE_TYPE_TEMP_RANGE)
		{
			rd.m_maxTemp = rule->KeyValue[RULE_KEY_MAXTEMP];
			rd.m_minTemp = rule->KeyValue[RULE_KEY_MINTEMP];
		}
		else if (rule->Name == RULE_TYPE_TIME_RANGE)
		{
			rd.m_maxHour = rule->KeyValue[RULE_KEY_MAXTIME];
			rd.m_minHour = rule->KeyValue[RULE_KEY_MINTIME];
		}
		else if (rule->Name == RULE_TYPE_EMAIL)
		{
			rd.m_email = rule->KeyValue[RULE_KEY_EMAIL];
		}
	}
	return;
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
