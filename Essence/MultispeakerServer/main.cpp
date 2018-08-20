//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: MultiSpeakerServer
//
// Version: MultiSpeakerServerQt14.11.17 (Original Build)

#include "MultiSpeakerServer.h"
#include <QApplication>

int main(int argc, char* argv[])
{
  QApplication a(argc, argv);
  MultiSpeakerServer w;
  w.show();
  return a.exec();
}
