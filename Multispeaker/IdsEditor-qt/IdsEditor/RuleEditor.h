//-------------------------------------------------------------------------------
// This code created by LMI Developments, LLC
//
// Copyright 2019.  All Rights Reserved.
//
//  Created By: Lance Irvine
//
//  RuleEditor
// 

#ifndef RULEEDITOR_H
#define RULEEDITOR_H

#include "ui_RuleEditor.h"

#include <QDialog>
#include <QHash>
#include <QStringList>

#include "Rule.h"

class RuleEditor : public QDialog
{
  Q_OBJECT
private:
  Ui::RuleEditor ui;
  
  QHash<QString, QStringList*> m_methods;
  RuleSection m_ruleSection;

public:
  RuleEditor(const RuleSection& ruleSection, QWidget* parent = Q_NULLPTR);
  ~RuleEditor();

  const RuleSection& Section() const { return m_ruleSection; }

protected:
  virtual void resizeEvent(QResizeEvent* e) { QWidget::resizeEvent(e); SaveGeometry(); }

private:
  void InitCombos();
  void InitMethods();
  void RestoreGeometry();
  void SaveGeometry();
  void UpdateUi();

private slots:
  void OnEndPointComboChanged(int index);
  void OnFunctionComboChanged(int index);
  void OnIniGroupToggled(bool checked);
  void OnMaxRequestsChanged(int value);
  void OnMaxRequestsToggled(bool checked);
  void OnMaxTempChanged(int value);
  void OnMaxTimeChanged(int value);
  void OnMethodComboChanged(int index);
  void OnMinTempChanged(int value);
  void OnMinTimeChanged(int value);

  void OnTempToggled(bool checked);
  void OnTimeToggled(bool checked);
};
#endif // RULEEDITOR_H