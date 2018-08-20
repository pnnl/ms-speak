//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: TimelineHeaderWidget
//

#include <QPainter>

#include "TimelineHeaderWidget.h"
#include "TimelineScene.h"

//------------------------------------------------------------------------------
// TimelineHeaderWidget
//
TimelineHeaderWidget::TimelineHeaderWidget(QWidget* parent)
  : QWidget(parent),
  m_color(Qt::darkGray)
{
  ui.setupUi(this);

  connect(ui.ClearBtn, SIGNAL(clicked()), &Timeline(), SLOT(OnClear()));
  connect(ui.PauseBtn, SIGNAL(clicked()), &Timeline(), SLOT(OnPause()));
  connect(ui.PlayBtn, SIGNAL(clicked()), &Timeline(), SLOT(OnPlay()));
  connect(ui.ResetBtn, SIGNAL(clicked()), &Timeline(), SLOT(OnReset()));
}
//------------------------------------------------------------------------------
// ~TimelineHeaderWidget
//
TimelineHeaderWidget::~TimelineHeaderWidget()
{
}
//-------------------------------------------------------------------------------
// SetTitle
//
void TimelineHeaderWidget::SetTitle(QString title, int pointSize)
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
void TimelineHeaderWidget::paintEvent(QPaintEvent* e)
{
	QPainter p(this);

	int w = width();
	int h = height();

	p.setPen(Qt::black);
	p.setBrush(m_color);
	p.drawRect(QRect(0, 0, w-1, h-1));
	QWidget::paintEvent(e);
}