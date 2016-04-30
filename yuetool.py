# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:08:00 2016

@author: navicloud
"""

from PyQt4 import QtGui, QtCore
import yuetool_ui
import yue

class YueTool(QtGui.QDialog, yuetool_ui.Ui_Dialog):
    def __init__(self, parent = None):
        super(YueTool, self).__init__(parent)
        self.setupUi(self)
        self.yue = yue.Yue()

    @QtCore.pyqtSignature('')
    def on_pbRefresh_clicked(self):
        print 'do Refresh'
        if self.rbOffDuty.isChecked():
            dateFrom = str(self.dateStart.date().toString("yyyy-MM-dd"))
            dateTo = str(self.dateEnd.date().toString("yyyy-MM-dd"))
            content = self.yue.GetKQ(dateFrom, dateTo)
            self.webView.setHtml(content)

    def showEvent(self, event):
        content = self.yue.Login('2797', 'venus190597')
        if self.yue.IsLoginSucceed(content):
            self.webView.setHtml('<h2><font color="green">Login Successfully.</font></h2>')
        else:
            self.webView.setHtml(content)

def main():
    app = QtGui.QApplication([])
    dlg = YueTool()
    dlg.show()
    app.exec_()

if __name__ == '__main__':
    main()
