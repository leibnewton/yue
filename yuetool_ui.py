# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yuetool.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(571, 629)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.rbOvtWork = QtGui.QRadioButton(self.groupBox)
        self.rbOvtWork.setChecked(False)
        self.rbOvtWork.setObjectName(_fromUtf8("rbOvtWork"))
        self.verticalLayout.addWidget(self.rbOvtWork)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rbOffDuty = QtGui.QRadioButton(self.groupBox)
        self.rbOffDuty.setChecked(True)
        self.rbOffDuty.setObjectName(_fromUtf8("rbOffDuty"))
        self.horizontalLayout.addWidget(self.rbOffDuty)
        self.dateStart = QtGui.QDateEdit(self.groupBox)
        self.dateStart.setDate(QtCore.QDate(2016, 3, 1))
        self.dateStart.setCalendarPopup(True)
        self.dateStart.setObjectName(_fromUtf8("dateStart"))
        self.horizontalLayout.addWidget(self.dateStart)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.dateEnd = QtGui.QDateEdit(self.groupBox)
        self.dateEnd.setDate(QtCore.QDate(2016, 4, 30))
        self.dateEnd.setCalendarPopup(True)
        self.dateEnd.setObjectName(_fromUtf8("dateEnd"))
        self.horizontalLayout.addWidget(self.dateEnd)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.timeRef = QtGui.QTimeEdit(self.groupBox)
        self.timeRef.setTime(QtCore.QTime(22, 0, 0))
        self.timeRef.setMinimumTime(QtCore.QTime(2, 0, 0))
        self.timeRef.setCurrentSection(QtGui.QDateTimeEdit.HourSection)
        self.timeRef.setObjectName(_fromUtf8("timeRef"))
        self.horizontalLayout.addWidget(self.timeRef)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pbRefresh = QtGui.QPushButton(Dialog)
        self.pbRefresh.setObjectName(_fromUtf8("pbRefresh"))
        self.horizontalLayout_3.addWidget(self.pbRefresh)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.webView = QtWebKit.QWebView(Dialog)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout_2.addWidget(self.webView)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pbQuit = QtGui.QPushButton(Dialog)
        self.pbQuit.setObjectName(_fromUtf8("pbQuit"))
        self.horizontalLayout_2.addWidget(self.pbQuit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pbQuit, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.rbOffDuty, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.dateStart.setEnabled)
        QtCore.QObject.connect(self.rbOffDuty, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.dateEnd.setEnabled)
        QtCore.QObject.connect(self.rbOffDuty, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.timeRef.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "任务类型", None))
        self.rbOvtWork.setText(_translate("Dialog", "Work", None))
        self.rbOffDuty.setText(_translate("Dialog", "Excel", None))
        self.dateStart.setDisplayFormat(_translate("Dialog", "yy/MM/dd", None))
        self.label.setText(_translate("Dialog", "~", None))
        self.dateEnd.setDisplayFormat(_translate("Dialog", "yy/MM/dd", None))
        self.label_2.setText(_translate("Dialog", ">", None))
        self.timeRef.setDisplayFormat(_translate("Dialog", "hh:mm", None))
        self.pbRefresh.setText(_translate("Dialog", "刷新", None))
        self.pbRefresh.setShortcut(_translate("Dialog", "F5", None))
        self.pbQuit.setText(_translate("Dialog", "退出", None))
        self.pbQuit.setShortcut(_translate("Dialog", "Ctrl+Q", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

