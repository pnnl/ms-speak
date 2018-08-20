//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: FunctionBlockListView
//

#ifndef FUNCTIONBLOCKLISTVIEW_H
#define FUNCTIONBLOCKLISTVIEW_H

#include <QListView>

class FunctionBlockListView : public QListView
{
  Q_OBJECT
private:
  QModelIndex m_dragIndex;

public:
  FunctionBlockListView(QWidget* parent);
  ~FunctionBlockListView();
};

#endif // FUNCTIONBLOCKLISTVIEW_H
