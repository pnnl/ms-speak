//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: Host
//

#include "Host.h"

//------------------------------------------------------------------------------
// Host
//
Host::Host(int id, const QString& name, QObject* parent)
  : QObject(parent),
  m_appFlags(Apache),
  m_id(id),
  m_name(name)
{
}
//------------------------------------------------------------------------------
// Host
//
Host::Host(const Host& host)
  : QObject(),
  m_appFlags(host.m_appFlags),
  m_id(host.m_id),
  m_name(host.m_name)
{
}
//------------------------------------------------------------------------------
// ~Host
//
Host::~Host()
{
}
//------------------------------------------------------------------------------
// Copy
//
void Host::Copy(const Host& host)
{
  m_appFlags = host.m_appFlags;
  m_id = host.m_id;
  m_name = host.m_name;
}