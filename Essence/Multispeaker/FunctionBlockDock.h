//-------------------------------------------------------------------------------
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//
//  Created By: Lance Irvine
//
//  Summary: FunctionBlockDock
//

#ifndef FUNCTIONBLOCKDOCK_H
#define FUNCTIONBLOCKDOCK_H

#include <QDockWidget>

class FunctionBlockDock : public QDockWidget
{
  Q_OBJECT
public:
  FunctionBlockDock(const QString& name, QWidget* parent=0);
  ~FunctionBlockDock();

protected:
  virtual void paintEvent(QPaintEvent* e);

private:
  QWidget* AddControlGroup(int index, const QString& title, const QStringList& names, QWidget* parent);

  void Collapse();
	void Collapse(int index);

	void Expand(int index);
  void Init();
  void InitDockTitleBar();
	void RestoreSplitterState();
	void SaveSplitterState();

private slots:
	void OnCollapsed(int index) {Collapse(index);}
	void OnExpanded(int index) {Expand(index);}
	void OnSplitterMoved(int pos, int index) {Q_UNUSED(pos); Q_UNUSED(index); SaveSplitterState();}
};

#endif // FUNCTIONBLOCKDOCK_H
