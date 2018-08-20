//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: FunctionBlockDockTitleBar
//

#include <QDockWidget>
#include <QPainter>

#include "FunctionBlockDockTitleBar.h"

//------------------------------------------------------------------------------
// FunctionBlockDockTitleBar
//
FunctionBlockDockTitleBar::FunctionBlockDockTitleBar(QWidget* parent)
  : QWidget(parent)
{
  ui.setupUi(this);
  ui.CloseBtn->setIcon(style()->standardIcon(QStyle::SP_TitleBarCloseButton));

  connect(ui.CloseBtn, SIGNAL(clicked()), this, SIGNAL(Close()));
  connect(ui.FloatBtn, SIGNAL(clicked()), this, SLOT(OnFloatBtn()));
}
//------------------------------------------------------------------------------
// ~FunctionBlockDockTitleBar
//
FunctionBlockDockTitleBar::~FunctionBlockDockTitleBar()
{
}
//-------------------------------------------------------------------------------
// SetFloating
//
void FunctionBlockDockTitleBar::SetFloating(bool isFloating)
{
  if (QDockWidget* w = qobject_cast<QDockWidget*>(parent()))
  {
    w->setFloating(isFloating);
    if (isFloating)
      ui.FloatBtn->setIcon(style()->standardIcon(QStyle::SP_TitleBarMinButton));
    else
      ui.FloatBtn->setIcon(style()->standardIcon(QStyle::SP_TitleBarNormalButton));
  }
}
//-------------------------------------------------------------------------------
// SetTitle
//
void FunctionBlockDockTitleBar::SetTitle(QString title, int pointSize)
{
  ui.TitleLabel->setText(title);
  if (pointSize)
  {
    QFont f(ui.TitleLabel->font()); 
    f.setPointSize(pointSize);
    ui.TitleLabel->setFont(f);
  }
	ui.TitleLabel->setStyleSheet("QLabel {background-color: transparent; color: black;}");
}
//-------------------------------------------------------------------------------
// paintEvent
//
void FunctionBlockDockTitleBar::paintEvent(QPaintEvent* e)
{
  QWidget::paintEvent(e);
  QPainter p(this);

  p.setPen(Qt::transparent);
  p.setBrush(Qt::transparent);
  p.drawRect(QRect(0, 0, width()-1, height()-1));
  p.end();
}
//-------------------------------------------------------------------------------
// OnFloatBtn
//
void FunctionBlockDockTitleBar::OnFloatBtn() 
{
  if (QDockWidget* w = qobject_cast<QDockWidget*>(parent()))
    SetFloating(!w->isFloating());
}