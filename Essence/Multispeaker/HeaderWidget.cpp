//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: HeaderWidget
//
#include <QMouseEvent>
#include <QPainter>

#include "HeaderWidget.h"

//------------------------------------------------------------------------------
// HeaderWidget
//
HeaderWidget::HeaderWidget(QWidget* parent)
	: QWidget(parent),
  m_color(Qt::darkGray),
	m_isExpanded(true)
{
	ui.setupUi(this);
	setMouseTracking(true);
	ui.IconLabel->setMouseTracking(true);
	SetIcon(m_isExpanded);

  connect(ui.AddBtn, SIGNAL(clicked()), this, SIGNAL(Add()));
  connect(ui.DelBtn, SIGNAL(clicked()), this, SIGNAL(Delete()));
}
//------------------------------------------------------------------------------
// ~HeaderWidget
//
HeaderWidget::~HeaderWidget()
{
}
//-------------------------------------------------------------------------------
// SetTitle
//
void HeaderWidget::SetTitle(QString title, int pointSize)
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
//------------------------------------------------------------------------------
// ShowAddDelete
//
void HeaderWidget::ShowAddDelete(bool doShow)
{
  ui.AddBtn->setVisible(doShow);
  ui.DelBtn->setVisible(doShow);
}
//-------------------------------------------------------------------------------
// mouseDoubleClickEvent
//
void HeaderWidget::mouseDoubleClickEvent(QMouseEvent* e)
{
	QWidget::mouseDoubleClickEvent(e); 
	if (isEnabled())
	{
		m_isExpanded = !m_isExpanded;
		SetIcon(m_isExpanded);
		if (m_isExpanded)
			emit Expanded();
		else
			emit Collapsed();
	}
}
//-------------------------------------------------------------------------------
// mouseMoveEvent
//
void HeaderWidget::mouseMoveEvent(QMouseEvent* e)
{
	QWidget::mouseMoveEvent(e); 
	if (isEnabled() && ui.IconLabel->rect().contains(e->pos()))
		setCursor(Qt::PointingHandCursor);
	else
		setCursor(Qt::ArrowCursor);
}
//-------------------------------------------------------------------------------
// mouseReleaseEvent
//
void HeaderWidget::mouseReleaseEvent(QMouseEvent* e)
{
	QWidget::mouseReleaseEvent(e); 
	if (isEnabled() && ui.IconLabel->rect().contains(e->pos()))
	{
		m_isExpanded = !m_isExpanded;
		SetIcon(m_isExpanded);
		if (m_isExpanded)
			emit Expanded();
		else
			emit Collapsed();
	}
}
//-------------------------------------------------------------------------------
// paintEvent
//
void HeaderWidget::paintEvent(QPaintEvent* e)
{
	QPainter p(this);

	int w = width();
	int h = height();

	p.setPen(Qt::black);
	p.setBrush(m_color);
	p.drawRect(QRect(0, 0, w-1, h-1));
	QWidget::paintEvent(e);
}
//-------------------------------------------------------------------------------
// SetIcon
//
void HeaderWidget::SetIcon(bool isExpanded)
{
	int size = ui.TitleLabel->font().pointSize();
  QPixmap pix(size, size);
  pix.fill(Qt::transparent);
  QPainter p(&pix);

  p.setRenderHint(QPainter::Antialiasing, true);
  p.setPen(Qt::white);
  p.setBrush(Qt::white);

  QPolygonF poly;
  if (isExpanded)
    poly << QPointF(0,0) << QPointF(size, 0) << QPointF((qreal)size / 2.0, size) << QPointF(0,0);
  else
    poly << QPointF(0,0) << QPointF(0, size) << QPointF(size, (qreal)size / 2.0) << QPointF(0,0);

  p.drawPolygon(poly);

  ui.IconLabel->setPixmap(pix);
}

