//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: Host
//

#ifndef HOST_H
#define HOST_H

#include <QObject>

class Host : public QObject
{
  Q_OBJECT
public:
  enum AppFlagEnum {NoApp = 0, Apache = 0x1, FireFox = 0x2, Terminal = 0x4, WireShark = 0x8};

private:
  int m_appFlags;
  int m_id;
  QString m_name;

public:
  Host(int id, const QString& name, QObject* parent=0);
  Host(const Host& host);
  ~Host();

  bool AppFlag(Host::AppFlagEnum appFlag) const {return (m_appFlags & appFlag);}
  int AppFlags() const {return m_appFlags;}
  void Copy(const Host& host);
  int Id() const {return m_id;}
  QString Name() const {return m_name;}

  void SetAppFlag(Host::AppFlagEnum appFlag) {m_appFlags |= appFlag;}
  void SetAppFlags(int flags) {m_appFlags = flags;}
  void SetId(int id) {m_id = id;}
  void SetName(const QString& name) {m_name = name;}
};

#endif // HOST_H
