# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yuedlg.ui'
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
        Dialog.resize(634, 477)
        Dialog.setMinimumSize(QtCore.QSize(600, 450))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leUrl = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leUrl.sizePolicy().hasHeightForWidth())
        self.leUrl.setSizePolicy(sizePolicy)
        self.leUrl.setObjectName(_fromUtf8("leUrl"))
        self.gridLayout.addWidget(self.leUrl, 0, 0, 1, 1)
        self.leParam = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leParam.sizePolicy().hasHeightForWidth())
        self.leParam.setSizePolicy(sizePolicy)
        self.leParam.setObjectName(_fromUtf8("leParam"))
        self.gridLayout.addWidget(self.leParam, 1, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.htmlBrowser = QtGui.QTextBrowser(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.htmlBrowser.sizePolicy().hasHeightForWidth())
        self.htmlBrowser.setSizePolicy(sizePolicy)
        self.htmlBrowser.setObjectName(_fromUtf8("htmlBrowser"))
        self.verticalLayout.addWidget(self.htmlBrowser)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.leUrl.setPlaceholderText(_translate("Dialog", "input URL here", None))
        self.leParam.setPlaceholderText(_translate("Dialog", "Additional params", None))
        self.pushButton.setText(_translate("Dialog", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

