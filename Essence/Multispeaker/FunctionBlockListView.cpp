//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: FunctionBlockListView
//

#include "FunctionBlockListView.h"

//------------------------------------------------------------------------------
// FunctionBlockListView
//
FunctionBlockListView::FunctionBlockListView(QWidget* parent)
  : QListView(parent)
{
  setAcceptDrops(false);
  setDefaultDropAction(Qt::IgnoreAction);
  setDragEnabled(true);

  setSelectionBehavior(QAbstractItemView::SelectRows);
  setSelectionMode(QAbstractItemView::ExtendedSelection);
}
//------------------------------------------------------------------------------
// ~FunctionBlockListView
//
FunctionBlockListView::~FunctionBlockListView()
{
}
