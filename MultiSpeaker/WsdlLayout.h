//WsdlLayout.h
#ifndef WSDLLAYOUT_H
#define WSDLLAYOUT_H

#include <QWidget>
#include <QPixmap>

#include "ui_WsdlLayout.h"

class WsdlLayout : public QDialog
{
    Q_OBJECT

public:
    explicit WsdlLayout(QWidget *parent = 0);
    ~WsdlLayout();

private:
	Ui::WsdlLayout ui;
};

#endif // WSDLLAYOUT_H
