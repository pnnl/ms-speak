// DEAD FILE
////-------------------------------------------------------------------------------
//// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
//// Operated by Battelle for the U.S. Department of Energy
////
////  Created By: Lance Irvine
////
////  Summary: Method
////
//
//#ifndef METHOD_H
//#define METHOD_H
//
//#include <QObject>
//
//#include "KeyValueList.h"
//
//class Method : public QObject
//{
//  Q_OBJECT
//private:
//  QString m_comment;
//  int m_dstHostId;
//  QString m_name;
//
//  KeyValueList m_requestParams;
//  KeyValueList m_responseParams;
//
//  int m_srcHostId;
//
//public:
//  Method(const QString& name, int srcHostId, int dstHostId, QObject* parent=0);
//  Method(const Method& method, QObject* parent=0);
//  ~Method();
//
//  int DstHostId() const {return m_dstHostId;}
//  QString Name() const {return m_name;}
//
//  KeyValueList& RequestParams() {return m_requestParams;}
//  const KeyValueList& RequestParams() const {return m_requestParams;}
//
//  KeyValueList& ResponseParams() {return m_responseParams;}
//  const KeyValueList& ResponseParams() const {return m_responseParams;}
//
//  void SetRequestParams(const KeyValueList& kv) {m_requestParams.Copy(kv);}
//  void SetResponseParams(const KeyValueList& kv) {m_responseParams.Copy(kv);}
//
//  int SrcHostId() const {return m_srcHostId;}
//
////private:
////  Q_DISABLE_COPY(Method);
//};
//
//#endif // METHOD_H
