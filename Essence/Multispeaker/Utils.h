//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: Utils
//

#ifndef UTILS_H
#define UTILS_H

#include <QObject>
#include <QProcess>

class QComboBox;

class Utils : public QObject
{
  Q_OBJECT
public:
  Utils(QObject* parent);
  ~Utils();

  static QString DebugByteArrayToString(const QByteArray& data);

  static void InitHostCombo(QComboBox* combo);
  
  static QString ParseShortName(const QString& name);
  static QString ParseLongName(const QString& name);

  static QString ProcessErrorToString(QProcess::ProcessError error);
  static void CreatRootHomePath();

public:
protected:
private:
signals:
private slots:
};

#endif // UTILS_H
