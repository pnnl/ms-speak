//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: WidgetContainer
//

#ifndef WIDGETCONTAINER_H
#define WIDGETCONTAINER_H

#include <QList>
#include <QScrollArea>

class WidgetContainer : public QScrollArea
{
  Q_OBJECT
private:
  QString m_saveRestoreKey;

public:
  WidgetContainer(const QString& saveRestoreKey, QWidget* parent=0);
  ~WidgetContainer();

  void SetWidgets(QList<QWidget*> list);

private:
  void Collapse(bool doSaveState=true);
	void Collapse(int index, bool doSaveState=true);
	void Expand(bool doSaveState=true);
	void Expand(int index, bool doSaveState=true);
	void RestoreSplitterState();
	void SaveSplitterState();

private slots:
	void OnCollapsed(int index) {Collapse(index);}
	void OnExpanded(int index) {Expand(index);}
	void OnSplitterMoved(int pos, int index) {Q_UNUSED(pos); Q_UNUSED(index); SaveSplitterState();}
};

#endif // WIDGETCONTAINER_H
