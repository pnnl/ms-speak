/*-------------------------------------------------------------------------------

  Multi-Speak - Secure Protocol Enterprise Access Kit(MS_SPEAK)
  Copyright © 2018, Battelle Memorial Institute
  All rights reserved.
  1.	Battelle Memorial Institute (hereinafter Battelle) hereby grants permission to any person or
		entity lawfully obtaining a copy of this software and associated documentation files
		(hereinafter “the Software”) to redistribute and use the Software in source and binary forms,
		with or without modification.  Such person or entity may use, copy, modify, merge, publish,
		distribute, sublicense, and/or sell copies of the Software, and may permit others to do so,
		subject to the following conditions:
		•	Redistributions of source code must retain the above copyright notice, this list of
			conditions and the following disclaimers.
		•	Redistributions in binary form must reproduce the above copyright notice, this list of
			conditions and the following disclaimer in the documentation and/or other materials
			provided with the distribution.
		•	Other than as used herein, neither the name Battelle Memorial Institute or Battelle may
			be used in any form whatsoever without the express written consent of Battelle.

  2.	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
		OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
		AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BATTELLE OR CONTRIBUTORS
		BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
		(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
		OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
		CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
		OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


  This material was prepared as an account of work sponsored by an agency of the United States Government.
  Neither the United States  Government nor the United States Department of Energy, nor Battelle, nor
  any of their employees, nor any jurisdiction or organization  that has cooperated in the development
  of these materials, makes any warranty, express or implied, or assumes any legal liability or
  responsibility for the accuracy, completeness, or usefulness or any information, apparatus, product,
  software, or process disclosed, or represents that its use would not infringe privately owned rights.
  Reference herein to any specific commercial product, process, or service by trade name, trademark,
  manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or
  favoring by the United States Government or any agency thereof, or Battelle Memorial Institute. The
  views and opinions of authors expressed herein do not necessarily state or reflect those of the
  United States Government or any agency thereof.
									 PACIFIC NORTHWEST NATIONAL LABORATORY
											    operated by
												  BATTELLE
											      for the
									  UNITED STATES DEPARTMENT OF ENERGY
									   under Contract DE-AC05-76RL01830


    This notice including this sentence must appear on any copies of this computer software.
*/
//-------------------------------------------------------------------------------
//	History
//		2017 - Created By: Lance Irvine.
//		2018 - Modified By: Carl Miller <carl.miller@pnnl.gov>
//-------------------------------------------------------------------------------
//
// Summary: HeaderWidget.cpp
//-------------------------------------------------------------------------------

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

