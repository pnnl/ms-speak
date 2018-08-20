//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HeaderContainerWidget
//

#include "HeaderContainerWidget.h"

//------------------------------------------------------------------------------
// HeaderContainerWidget
//
HeaderContainerWidget::HeaderContainerWidget(int index, const QString& title, QWidget* parent)
  : QWidget(parent),
  m_index(index)
{
  ui.setupUi(this);

  // Header
  ui.Header->SetTitle(title);
  ui.Header->ShowAddDelete(false);

  Expand();

	connect(ui.Header, SIGNAL(Collapsed()), this, SLOT(OnCollapsed()));
	connect(ui.Header, SIGNAL(Expanded()), this, SLOT(OnExpanded()));
}
//------------------------------------------------------------------------------
// ~HeaderContainerWidget
//
HeaderContainerWidget::~HeaderContainerWidget()
{
}
