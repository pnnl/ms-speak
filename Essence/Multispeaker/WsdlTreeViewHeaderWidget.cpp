//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WsdlTreeViewHeaderWidget
//

#include <QPainter>

#include "WsdlTreeViewHeaderWidget.h"

//------------------------------------------------------------------------------
// WsdlTreeViewHeaderWidget
//
WsdlTreeViewHeaderWidget::WsdlTreeViewHeaderWidget(QWidget* parent)
  : QWidget(parent),
  m_color(Qt::darkGray)
{
  ui.setupUi(this);
  connect(ui.InfoBtn, SIGNAL(clicked()), this, SIGNAL(InfoToggled()));
  connect(ui.SaveBtn, SIGNAL(clicked()), this, SIGNAL(SaveClicked()));
}
//------------------------------------------------------------------------------
// ~WsdlTreeViewHeaderWidget
//
WsdlTreeViewHeaderWidget::~WsdlTreeViewHeaderWidget()
{
}
//-------------------------------------------------------------------------------
// SetTitle
//
void WsdlTreeViewHeaderWidget::SetTitle(QString title, int pointSize)
{
	ui.TitleLabel->setText(title);
	if (pointSize)
	{
		QFont f(ui.TitleLabel->font()); 
		f.setPointSize(pointSize);
		ui.TitleLabel->setFont(f);
	}
	ui.TitleLabel->setStyleSheet("QLabel {background-color: transparent; color: white;}");
}
//-------------------------------------------------------------------------------
// paintEvent
//
void WsdlTreeViewHeaderWidget::paintEvent(QPaintEvent* e)
{
	QPainter p(this);

	int w = width();
	int h = height();

	p.setPen(Qt::black);
	p.setBrush(m_color);
	p.drawRect(QRect(0, 0, w-1, h-1));
	QWidget::paintEvent(e);
}
