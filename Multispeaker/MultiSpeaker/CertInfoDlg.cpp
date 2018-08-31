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
// Summary: CertInfoDlg.cpp
//-------------------------------------------------------------------------------

#include <QSslCertificate>

#include "CertInfoDlg.h"

//------------------------------------------------------------------------------
// CertInfoDlg
//
CertInfoDlg::CertInfoDlg(QWidget* parent)
  : QDialog(parent)
{
  ui.setupUi(this);
  QList<int> sizes;
  sizes << 10 << 75 << 2000;
  ui.MySplitter->setSizes(sizes);
  connect(ui.buttonBox, SIGNAL(accepted()), this, SLOT(accept()));
  connect(ui.buttonBox, SIGNAL(rejected()), this, SLOT(reject()));
  connect(ui.CertificationPathView, SIGNAL(currentRowChanged(int)), this, SLOT(OnCurrentRowChanged(int)));
}
//------------------------------------------------------------------------------
// ~CertInfoDlg
//
CertInfoDlg::~CertInfoDlg()
{
}
//------------------------------------------------------------------------------
// SetCertificateChain
//
void CertInfoDlg::SetCertificateChain(const QList<QSslCertificate>& chain)
{
  m_chain.clear();
  m_chain = chain;
  ui.CertificationPathView->clear();

  for (int i = 0; i < m_chain.size(); i++)
  {
    const QSslCertificate &cert = chain.at(i);
    ui.CertificationPathView->addItem(QString("%1%2 (%3)").arg(!i ? QString() : "Issued by: ")
      .arg(cert.subjectInfo(QSslCertificate::Organization).join(", "))
      .arg(cert.subjectInfo(QSslCertificate::CommonName).join(", ")));
    }
  ui.CertificationPathView->setCurrentRow(0);
}
//------------------------------------------------------------------------------
// SetCipherInfo
//
void CertInfoDlg::SetCipherInfo(QSslCipher& cipher)
{
  QString cipherStr = QString("%1, %2 (%3/%4)")
    .arg(cipher.authenticationMethod())
    .arg(cipher.name())
    .arg(cipher.usedBits())
    .arg(cipher.supportedBits());
  ui.CipherEdit->setText(cipherStr);
}
//------------------------------------------------------------------------------
// UpdateCertInfo
//
void CertInfoDlg::UpdateCertInfo(int idx)
{
  ui.CertificateInfoView->clear();
  if (idx >= 0 && idx < m_chain.size()) 
  {
    const QSslCertificate& cert = m_chain.at(idx);
    QStringList lines;
    lines << tr("Organization: %1").arg(cert.subjectInfo(QSslCertificate::Organization).join(", "))
    << tr("Subunit: %1").arg(cert.subjectInfo(QSslCertificate::OrganizationalUnitName).join(", "))
    << tr("Country: %1").arg(cert.subjectInfo(QSslCertificate::CountryName).join(", "))
    << tr("Locality: %1").arg(cert.subjectInfo(QSslCertificate::LocalityName).join(", "))
    << tr("State/Province: %1").arg(cert.subjectInfo(QSslCertificate::StateOrProvinceName).join(", "))
    << tr("Common Name: %1").arg(cert.subjectInfo(QSslCertificate::CommonName).join(", "))
    << QString()
    << tr("Issuer Organization: %1").arg(cert.issuerInfo(QSslCertificate::Organization).join(", "))
    << tr("Issuer Unit Name: %1").arg(cert.issuerInfo(QSslCertificate::OrganizationalUnitName).join(", "))
    << tr("Issuer Country: %1").arg(cert.issuerInfo(QSslCertificate::CountryName).join(", "))
    << tr("Issuer Locality: %1").arg(cert.issuerInfo(QSslCertificate::LocalityName).join(", "))
    << tr("Issuer State/Province: %1").arg(cert.issuerInfo(QSslCertificate::StateOrProvinceName).join(", "))
    << tr("Issuer Common Name: %1").arg(cert.issuerInfo(QSslCertificate::CommonName).join(", "));
    foreach (QString line, lines)
      ui.CertificateInfoView->addItem(line);
  } 
  else 
    ui.CertificateInfoView->clear();
}
