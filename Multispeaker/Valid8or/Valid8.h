
#ifndef VALID8_H
#define VALID8_H

#include <QWidget>
#include <QtGui>
//#include <QtXmlPatterns>
#include <QDialog>
#include <QProcess>

#include "ui_Valid8.h"
#include "ui_ProgressWidget.h"

enum class JReturns {
	EXCEPTION=5,
	VALID8_FAIL=4,
	INIT_FAIL=3,
	INITXSD_FAIL=2,
	FAIL=1,
	SUCCESS=0
};
//------------------------------------------------------------------------------
// Valid8or
//
class Valid8or :  public QDialog
{
    Q_OBJECT
private:
	Ui::Valid8 ui;
	QString m_SchemaRoot;
	QString m_EndPoint;
	QString m_XmlFilename;
	bool    m_initialized{false};         // True if windows finished initializing
	bool    m_byteArray{false};
	QTemporaryFile m_file;

public:
    Valid8or(QString Endpoint, QString fileName, QWidget* parent=Q_NULLPTR  );
	Valid8or(const QByteArray& msg, QWidget* parent=Q_NULLPTR );

private Q_SLOTS:
    void validate();
    void textChanged();
	void OnAccept();
	void resetXsd();
	//void resetXml();
	void closeEvent(QCloseEvent *event) override;
	void valid8Done(QString m);

private:
	void selectSchema();
    void loadXml();
	bool initialize(QWidget* parent);
	void initializeWidgets();
};

#endif
