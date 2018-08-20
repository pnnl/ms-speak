//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: MultiSpeaker
//

#include <QApplication>


#include "MultiSpeaker.h"

int main(int argc, char* argv[])
{
  QCoreApplication::setOrganizationName("PNNL");
  QCoreApplication::setOrganizationDomain("pnnl.gov");
  QCoreApplication::setApplicationName("MultiSpeaker");

  QApplication a(argc, argv);

  MultiSpeaker w;
  w.show();
  return a.exec();
}
