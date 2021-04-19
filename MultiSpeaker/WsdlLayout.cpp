//WsdlLayout.cpp
#include "WsdlLayout.h"

WsdlLayout::WsdlLayout(QWidget *parent) :
	QDialog(parent)
{
	ui.setupUi(this);
	QPixmap *mypix = new QPixmap(":/MultiSpeaker/Resources/WsdlLayout.png");
	ui.Xtree->setPixmap(*mypix);
	delete mypix;

	ui.WsdlText->setText("WSDL File Could Not Be Located.\n"
						 "Your Schema Hierarchy must be similar to the above.");
}

WsdlLayout::~WsdlLayout()
{
}
