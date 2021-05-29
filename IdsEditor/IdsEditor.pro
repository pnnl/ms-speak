# -------------------------------------------------------------------------------
#
#  Multi-Speak - Secure Protocol Enterprise Access Kit(MS_SPEAK)
#  Copyright © 2021, Battelle Memorial Institute
#  All rights reserved.
#  1.	Battelle Memorial Institute (hereinafter Battelle) hereby grants permission to any person or
#		entity lawfully obtaining a copy of this software and associated documentation files
#		(hereinafter “the Software”) to redistribute and use the Software in source and binary forms,
#		with or without modification.  Such person or entity may use, copy, modify, merge, publish,
#		distribute, sublicense, and/or sell copies of the Software, and may permit others to do so,
#		subject to the following conditions:
#		•	Redistributions of source code must retain the above copyright notice, this list of
#			conditions and the following disclaimers.
#		•	Redistributions in binary form must reproduce the above copyright notice, this list of
#			conditions and the following disclaimer in the documentation and/or other materials
#			provided with the distribution.
#		•	Other than as used herein, neither the name Battelle Memorial Institute or Battelle may
#			be used in any form whatsoever without the express written consent of Battelle.
#
#  2.	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
#		OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
#		AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BATTELLE OR CONTRIBUTORS
#		BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#		(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
#		OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#		CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
#		OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#
#  This material was prepared as an account of work sponsored by an agency of the United States Government.
#  Neither the United States  Government nor the United States Department of Energy, nor Battelle, nor
#  any of their employees, nor any jurisdiction or organization  that has cooperated in the development
#  of these materials, makes any warranty, express or implied, or assumes any legal liability or
#  responsibility for the accuracy, completeness, or usefulness or any information, apparatus, product,
#  software, or process disclosed, or represents that its use would not infringe privately owned rights.
#  Reference herein to any specific commercial product, process, or service by trade name, trademark,
#  manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or
#  favoring by the United States Government or any agency thereof, or Battelle Memorial Institute. The
#  views and opinions of authors expressed herein do not necessarily state or reflect those of the
#  United States Government or any agency thereof.
#									 PACIFIC NORTHWEST NATIONAL LABORATORY
#												operated by
#												  BATTELLE
#												  for the
#									  UNITED STATES DEPARTMENT OF ENERGY
#									   under Contract DE-AC05-76RL01830
#
#
#	This notice including this sentence must appear on any copies of this computer software.
#
# -------------------------------------------------------------------------------
#	History
#		2021 - Modified By: Carl Miller <carl.miller@pnnl.gov> from original by
#                  Lance Irvine, LMI Developments, LLC.
#		02.09.2021 CHM - Populate from Sqlite DB, remove Logging.
#-------------------------------------------------------------------------------
#
# Summary: IdsEditor.pro
#-------------------------------------------------------------------------------
# qDebug is also preprocessor-controlled, but it has its own special macro,
#		 QT_NO_DEBUG_OUTPUT.
# If you add that to your Release build defines, it will not print out.

TEMPLATE = app
TARGET = IdsEditor
DESTDIR = ../run
QT += core gui sql network
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG(debug, debug|release) {
	DEFINES += _DEBUG_
	DESTDIR = $${_PRO_FILE_PWD_}/../builds/Debug
	message("CONFIG is : " Debug)
}
CONFIG(release, debug|release) {
	DEFINES += QT_NO_DEBUG_OUTPUT
	DESTDIR = $${_PRO_FILE_PWD_}/../builds/Release
	message("CONFIG is : " Release)
	QMAKE_CXXFLAGS += -Ofast
}
CONFIG += c++11

# The following define makes your compiler emit warnings if you use
# any feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

#include(IdsEditor.pri)

# Default rules for deployment.
#qnx: target.path = /tmp/$${TARGET}/bin
#else: unix:!android: target.path = /opt/$${TARGET}/bin
#!isEmpty(target.path): INSTALLS += target

INCLUDEPATH += .

DEPENDPATH += .
MOC_DIR += GeneratedFiles
OBJECTS_DIR += obj
UI_DIR += GeneratedFiles
RCC_DIR += GeneratedFiles

HEADERS += IdsSettings.h \
	Rule.h \
	RuleConst.h \
	DbConst.h \
	IdsEditor.h \
	RuleEditor.h \
	TesterEditor.h

SOURCES += IdsEditor.cpp \
	main.cpp \
	Rule.cpp \
	RuleEditor.cpp \
	TesterEditor.cpp

FORMS += IdsEditor.ui \
	RuleEditor.ui \
	TesterEditor.ui

RESOURCES += IdsEditor.qrc



