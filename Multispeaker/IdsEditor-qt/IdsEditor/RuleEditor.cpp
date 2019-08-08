//-------------------------------------------------------------------------------
// This code created by LMI Developments, LLC
//
// Copyright 2019.  All Rights Reserved.
//
//  Created By: Lance Irvine
//
//  RuleEditor
// 

#include <QDebug>
#include <QHash>
#include <QSettings>
#include <QVariant>

#include "IdsSettings.h"
#include "RuleConst.h"
#include "RuleEditor.h"

//-------------------------------------------------------------------------------
// RuleEditor
//
RuleEditor::RuleEditor(const RuleSection& ruleSection, QWidget* parent)
  : QDialog(parent),
  m_ruleSection(ruleSection)
{
  ui.setupUi(this);

  RestoreGeometry();
  
  ui.BottomFrame->setVisible(true);
  ui.IniPlainTextEdit->setVisible(false);
  ui.MaxRequestsFrame->setVisible(false);
  ui.TempFrame->setVisible(false);
  ui.TimeFrame->setVisible(false);

  InitMethods(); // init the m_methods hash
  InitCombos();
  UpdateUi();

  // Group Toggle connections before SetRule
  connect(ui.MaxRequestsGroup, SIGNAL(toggled(bool)), this, SLOT(OnMaxRequestsToggled(bool)));
  connect(ui.TempGroup, SIGNAL(toggled(bool)), this, SLOT(OnTempToggled(bool)));
  connect(ui.TimeGroup, SIGNAL(toggled(bool)), this, SLOT(OnTimeToggled(bool)));

  connect(ui.EndPointCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnEndPointComboChanged(int)));
  connect(ui.FunctionCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnFunctionComboChanged(int)));
  connect(ui.MethodCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnMethodComboChanged(int)));
  connect(ui.IniGroup, SIGNAL(toggled(bool)), this, SLOT(OnIniGroupToggled(bool)));

  connect(ui.MaxRequestsSpin, SIGNAL(valueChanged(int)), this, SLOT(OnMaxRequestsChanged(int)));

  connect(ui.MaxTempSlider, SIGNAL(valueChanged(int)), ui.MaxTempSpin, SLOT(setValue(int)));
  connect(ui.MaxTempSlider, SIGNAL(valueChanged(int)), this, SLOT(OnMaxTempChanged(int)));
  connect(ui.MaxTempSpin, SIGNAL(valueChanged(int)), ui.MaxTempSlider, SLOT(setValue(int)));
  connect(ui.MaxTempSpin, SIGNAL(valueChanged(int)), this, SLOT(OnMaxTempChanged(int)));
  connect(ui.MinTempSlider, SIGNAL(valueChanged(int)), ui.MinTempSpin, SLOT(setValue(int)));
  connect(ui.MinTempSlider, SIGNAL(valueChanged(int)), this, SLOT(OnMinTempChanged(int)));
  connect(ui.MinTempSpin, SIGNAL(valueChanged(int)), ui.MinTempSlider, SLOT(setValue(int)));
  connect(ui.MinTempSpin, SIGNAL(valueChanged(int)), this, SLOT(OnMinTempChanged(int)));

  connect(ui.MaxTimeSlider, SIGNAL(valueChanged(int)), ui.MaxTimeSpin, SLOT(setValue(int)));
  connect(ui.MaxTimeSlider, SIGNAL(valueChanged(int)), this, SLOT(OnMaxTimeChanged(int)));
  connect(ui.MaxTimeSpin, SIGNAL(valueChanged(int)), ui.MaxTimeSlider, SLOT(setValue(int)));
  connect(ui.MaxTimeSpin, SIGNAL(valueChanged(int)), this, SLOT(OnMaxTimeChanged(int)));
  connect(ui.MinTimeSlider, SIGNAL(valueChanged(int)), ui.MinTimeSpin, SLOT(setValue(int)));
  connect(ui.MinTimeSlider, SIGNAL(valueChanged(int)), this, SLOT(OnMinTimeChanged(int)));
  connect(ui.MinTimeSpin, SIGNAL(valueChanged(int)), ui.MinTimeSlider, SLOT(setValue(int)));
  connect(ui.MinTimeSpin, SIGNAL(valueChanged(int)), this, SLOT(OnMinTimeChanged(int)));

  connect(ui.buttonBox, SIGNAL(accepted()), this, SLOT(accept()));
  connect(ui.buttonBox, SIGNAL(rejected()), this, SLOT(reject()));
}
//-------------------------------------------------------------------------------
// ~RuleEditor
//
RuleEditor::~RuleEditor()
{
}
//-------------------------------------------------------------------------------
// InitCombos
//
void RuleEditor::InitCombos()
{
  ui.FunctionCombo->addItem(CUSTOMER_BILLING, CUSTOMER_BILLING_ENDPOINT_LIST);
  ui.FunctionCombo->addItem(METERING_MANAGEMENT, METERING_MANAGEMENT_ENDPOINT_LIST);
  ui.FunctionCombo->addItem(OUTAGE_MANAGEMENT, OUTAGE_MANAGEMENT_ENDPOINT_LIST);
}
//-------------------------------------------------------------------------------
// InitMethods
//
void RuleEditor::InitMethods()
{
  m_methods.insert(CB_SERVER, &CB_METHOD_LIST);
  m_methods.insert(MDM_SERVER, &MDM_METHOD_LIST);
  m_methods.insert(PG_SERVER, &PG_METHOD_LIST);
  m_methods.insert(CD_SERVER, &CD_METHOD_LIST);
  m_methods.insert(MR_SERVER, &MR_METHOD_LIST);
  m_methods.insert(OD_SERVER, &OD_METHOD_LIST);
}
//-------------------------------------------------------------------------------
// RestoreGeometry
//
void RuleEditor::RestoreGeometry()
{
  restoreGeometry(QSettings().value(SK_RULE_GEOMETRY).toByteArray());
}
//-------------------------------------------------------------------------------
// SaveGeometry
//
void RuleEditor::SaveGeometry()
{
  QSettings().setValue(SK_RULE_GEOMETRY, saveGeometry());
}
//-------------------------------------------------------------------------------
// UpdateUi
//
void RuleEditor::UpdateUi()
{
  // Deduce what the function is based on rule
  QString function = CUSTOMER_BILLING;
  if (METERING_MANAGEMENT_ENDPOINT_LIST.contains(m_ruleSection.EndPoint))
    function = METERING_MANAGEMENT;
  else if (OUTAGE_MANAGEMENT_ENDPOINT_LIST.contains(m_ruleSection.EndPoint))
    function = OUTAGE_MANAGEMENT;

  // Set up the combos based on rule
  disconnect(ui.EndPointCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnEndPointComboChanged(int)));
  disconnect(ui.FunctionCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnFunctionComboChanged(int)));
  disconnect(ui.MethodCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnMethodComboChanged(int)));
  ui.MethodCombo->clear();
  ui.EndPointCombo->clear();
  ui.FunctionCombo->setCurrentIndex(ui.FunctionCombo->findText(function));

  // EndPoint
  QStringList endPointList = ui.FunctionCombo->currentData().toStringList();
  for (QString ep : endPointList)
    ui.EndPointCombo->addItem(ep, *m_methods.value(ep));

  int idx = ui.EndPointCombo->findText(m_ruleSection.EndPoint);
  if (idx < 0)
  {
    ui.EndPointCombo->setCurrentIndex(0); // First one
    m_ruleSection.EndPoint = ui.EndPointCombo->currentText();
  }
  else
  {
    ui.EndPointCombo->setCurrentIndex(idx);
  }

  // Method
  for (QString method : ui.EndPointCombo->currentData().toStringList())
    ui.MethodCombo->addItem(method);

  idx = ui.MethodCombo->findText(m_ruleSection.Method);
  if (idx < 0)
  {
    ui.MethodCombo->setCurrentIndex(0); // First one
    m_ruleSection.Method = ui.MethodCombo->currentText();
  }
  else
  {
    ui.MethodCombo->setCurrentIndex(idx);
  }

  connect(ui.EndPointCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnEndPointComboChanged(int)));
  connect(ui.FunctionCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnFunctionComboChanged(int)));
  connect(ui.MethodCombo, SIGNAL(currentIndexChanged(int)), this, SLOT(OnMethodComboChanged(int)));

  // Check for rules
  for (Rule* rule : m_ruleSection.Rules)
  {
    if (rule->Name == RULE_TYPE_MAX_VALUE)
    {
      ui.MaxRequestsGroup->setChecked(true);
      ui.MaxRequestsFrame->setVisible(true);
      ui.MaxRequestsSpin->setValue(rule->KeyValue.value(RULE_KEY_NUMREQ).toInt());
    }
    else if (rule->Name == RULE_TYPE_TEMP_RANGE)
    {
      ui.TempGroup->setChecked(true);
      ui.TempFrame->setVisible(true);
      ui.MaxTempSpin->setValue(rule->KeyValue.value(RULE_KEY_MAXTEMP).toInt());
      ui.MaxTempSlider->setValue(rule->KeyValue.value(RULE_KEY_MAXTEMP).toInt());
      ui.MinTempSpin->setValue(rule->KeyValue.value(RULE_KEY_MINTEMP).toInt());
      ui.MinTempSlider->setValue(rule->KeyValue.value(RULE_KEY_MINTEMP).toInt());
    }
    else if (rule->Name == RULE_TYPE_TIME_RANGE)
    {
      ui.TimeGroup->setChecked(true);
      ui.TimeFrame->setVisible(true);
      ui.MaxTimeSpin->setValue(rule->KeyValue.value(RULE_KEY_MAXTIME).toInt());
      ui.MaxTimeSlider->setValue(rule->KeyValue.value(RULE_KEY_MAXTIME).toInt());
      ui.MinTimeSpin->setValue(rule->KeyValue.value(RULE_KEY_MINTIME).toInt());
      ui.MinTimeSlider->setValue(rule->KeyValue.value(RULE_KEY_MINTIME).toInt());
    }
  }

  ui.IniPlainTextEdit->clear();
  ui.IniPlainTextEdit->appendPlainText(m_ruleSection.ToString());
}
//-------------------------------------------------------------------------------
// OnEndPointComboChanged
//
void RuleEditor::OnEndPointComboChanged(int index)
{
  if (ui.EndPointCombo->count() <= 0)
    return;

  m_ruleSection.EndPoint = ui.EndPointCombo->itemText(index);
  m_ruleSection.Method = m_methods.value(m_ruleSection.EndPoint)->first();

  UpdateUi();
}
//-------------------------------------------------------------------------------
// OnFunctionComboChanged
//
void RuleEditor::OnFunctionComboChanged(int index)
{
  Q_UNUSED(index);
  QString function = ui.FunctionCombo->currentText();

  if (function == CUSTOMER_BILLING)
    m_ruleSection.EndPoint = CUSTOMER_BILLING_ENDPOINT_LIST.first();
  else if (function == METERING_MANAGEMENT)
    m_ruleSection.EndPoint = METERING_MANAGEMENT_ENDPOINT_LIST.first();
  else if (function == OUTAGE_MANAGEMENT)
    m_ruleSection.EndPoint = OUTAGE_MANAGEMENT_ENDPOINT_LIST.first();

  m_ruleSection.Method = m_methods.value(m_ruleSection.EndPoint)->first();

  qDebug() << "OnFunctionComboChanged";
  UpdateUi();
}
//-------------------------------------------------------------------------------
// OnIniGroupToggled
//
void RuleEditor::OnIniGroupToggled(bool checked)
{
  ui.IniPlainTextEdit->setVisible(checked);
  ui.BottomFrame->setVisible(!checked);
}
//-------------------------------------------------------------------------------
// OnMaxRequestsChanged
//
void RuleEditor::OnMaxRequestsChanged(int value)
{
  m_ruleSection.Rules.value(RULE_TYPE_MAX_VALUE)->KeyValue.insert(RULE_KEY_NUMREQ, QString::number(value));
  UpdateUi();
}
//-------------------------------------------------------------------------------
// OnMaxRequestsToggled
//
void RuleEditor::OnMaxRequestsToggled(bool checked)
{
  ui.MaxRequestsFrame->setVisible(checked);
  if (checked)
  {
    Rule* rule = RuleSection::CreateRule(RULE_TYPE_MAX_VALUE);
    rule->KeyValue.insert(RULE_KEY_NUMREQ, QString::number(ui.MaxRequestsSpin->value()));
    m_ruleSection.Rules.insert(RULE_TYPE_MAX_VALUE, rule);
  }
  else
  {
    delete m_ruleSection.Rules.take(RULE_TYPE_MAX_VALUE);
  }
  UpdateUi();
}
//-------------------------------------------------------------------------------
// OnMaxTempChanged
//
void RuleEditor::OnMaxTempChanged(int value)
{
  m_ruleSection.Rules.value(RULE_TYPE_TEMP_RANGE)->KeyValue.insert(RULE_KEY_MAXTEMP, QString::number(value));
  UpdateUi();
}
//-------------------------------------------------------------------------------
// OnMaxTimeChanged
//
void RuleEditor::OnMaxTimeChanged(int value)
{
  m_ruleSection.Rules.value(RULE_TYPE_TIME_RANGE)->KeyValue.insert(RULE_KEY_MAXTIME, QString::number(value));
  UpdateUi();
}
//-------------------------------------------------------------------------------
// OnMethodComboChanged
//
void RuleEditor::OnMethodComboChanged(int index)
{
  Q_UNUSED(index);
  if (ui.MethodCombo->count() <= 0)
    return;
  m_ruleSection.Method = ui.MethodCombo->currentText();
  UpdateUi();
}
//-------------------------------------------------------------------------------
// OnMinTempChanged
//
void RuleEditor::OnMinTempChanged(int value)
{
  m_ruleSection.Rules.value(RULE_TYPE_TEMP_RANGE)->KeyValue.insert(RULE_KEY_MINTEMP, QString::number(value));
  UpdateUi();
}
//-------------------------------------------------------------------------------
// OnMinTimeChanged
//
void RuleEditor::OnMinTimeChanged(int value)
{
  m_ruleSection.Rules.value(RULE_TYPE_TIME_RANGE)->KeyValue.insert(RULE_KEY_MINTIME, QString::number(value));
  UpdateUi();
}
//-------------------------------------------------------------------------------
// OnTempToggled
//
void RuleEditor::OnTempToggled(bool checked)
{
  ui.TempFrame->setVisible(checked);
  if (checked)
  {
    Rule* rule = RuleSection::CreateRule(RULE_TYPE_TEMP_RANGE);
    rule->KeyValue.insert(RULE_KEY_MAXTEMP, QString::number(ui.MaxTempSpin->value()));
    rule->KeyValue.insert(RULE_KEY_MINTEMP, QString::number(ui.MinTempSpin->value()));
    m_ruleSection.Rules.insert(RULE_TYPE_TEMP_RANGE, rule);
  }
  else
  {
    delete m_ruleSection.Rules.take(RULE_TYPE_TEMP_RANGE);
  }
  UpdateUi();
}
//-------------------------------------------------------------------------------
// OnTimeToggled
//
void RuleEditor::OnTimeToggled(bool checked)
{
  ui.TimeFrame->setVisible(checked);
  if (checked)
  {
    Rule* rule = RuleSection::CreateRule(RULE_TYPE_TIME_RANGE);
    rule->KeyValue.insert(RULE_KEY_MAXTIME, QString::number(ui.MaxTimeSpin->value()));
    rule->KeyValue.insert(RULE_KEY_MINTIME, QString::number(ui.MinTimeSpin->value()));
    m_ruleSection.Rules.insert(RULE_TYPE_TIME_RANGE, rule);
  }
  else
  {
    delete m_ruleSection.Rules.take(RULE_TYPE_TIME_RANGE);
  }
  UpdateUi();
}


