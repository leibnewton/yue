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
        Dialog.resize(800, 600)
        Dialog.setMinimumSize(QtCore.QSize(720, 540))
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
        self.rbApplication = QtGui.QRadioButton(self.groupBox)
        self.rbApplication.setChecked(True)
        self.rbApplication.setObjectName(_fromUtf8("rbApplication"))
        self.verticalLayout.addWidget(self.rbApplication)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.rbOffDuty = QtGui.QRadioButton(self.groupBox)
        self.rbOffDuty.setChecked(False)
        self.rbOffDuty.setObjectName(_fromUtf8("rbOffDuty"))
        self.horizontalLayout_4.addWidget(self.rbOffDuty)
        self.dateStart = QtGui.QDateEdit(self.groupBox)
        self.dateStart.setDate(QtCore.QDate(2016, 3, 1))
        self.dateStart.setCalendarPopup(True)
        self.dateStart.setObjectName(_fromUtf8("dateStart"))
        self.horizontalLayout_4.addWidget(self.dateStart)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.dateEnd = QtGui.QDateEdit(self.groupBox)
        self.dateEnd.setDate(QtCore.QDate(2016, 4, 30))
        self.dateEnd.setCalendarPopup(True)
        self.dateEnd.setObjectName(_fromUtf8("dateEnd"))
        self.horizontalLayout_4.addWidget(self.dateEnd)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.timeRef = QtGui.QTimeEdit(self.groupBox)
        self.timeRef.setTime(QtCore.QTime(22, 0, 0))
        self.timeRef.setMinimumTime(QtCore.QTime(2, 0, 0))
        self.timeRef.setCurrentSection(QtGui.QDateTimeEdit.HourSection)
        self.timeRef.setObjectName(_fromUtf8("timeRef"))
        self.horizontalLayout_4.addWidget(self.timeRef)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
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
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmbType = QtGui.QComboBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbType.sizePolicy().hasHeightForWidth())
        self.cmbType.setSizePolicy(sizePolicy)
        self.cmbType.setObjectName(_fromUtf8("cmbType"))
        self.horizontalLayout.addWidget(self.cmbType)
        self.cmbReason = QtGui.QComboBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbReason.sizePolicy().hasHeightForWidth())
        self.cmbReason.setSizePolicy(sizePolicy)
        self.cmbReason.setEditable(True)
        self.cmbReason.setObjectName(_fromUtf8("cmbReason"))
        self.horizontalLayout.addWidget(self.cmbReason)
        self.pbApply = QtGui.QPushButton(self.frame)
        self.pbApply.setObjectName(_fromUtf8("pbApply"))
        self.horizontalLayout.addWidget(self.pbApply)
        self.verticalLayout_2.addWidget(self.frame)
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
        QtCore.QObject.connect(self.rbApplication, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frame.setShown)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "任务类型", None))
        self.rbOvtWork.setText(_translate("Dialog", "Work", None))
        self.rbApplication.setText(_translate("Dialog", "Application", None))
        self.rbOffDuty.setText(_translate("Dialog", "Excel", None))
        self.dateStart.setDisplayFormat(_translate("Dialog", "yy/MM/dd", None))
        self.label.setText(_translate("Dialog", "~", None))
        self.dateEnd.setDisplayFormat(_translate("Dialog", "yy/MM/dd", None))
        self.label_2.setText(_translate("Dialog", ">", None))
        self.timeRef.setDisplayFormat(_translate("Dialog", "hh:mm", None))
        self.pbRefresh.setText(_translate("Dialog", "刷新", None))
        self.pbRefresh.setShortcut(_translate("Dialog", "F5", None))
        self.pbApply.setText(_translate("Dialog", "申请", None))
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

