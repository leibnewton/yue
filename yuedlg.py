# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:35:47 2016

@author: navicloud
"""
import urllib2
import lxml
from PyQt4 import QtCore, QtGui
import yuedlg_ui
import yue

class YueDlg(QtGui.QDialog, yuedlg_ui.Ui_Dialog):
    def __init__(self, parent=None):
        super(YueDlg, self).__init__(parent)
        self.setupUi(self)

        self.htmlBrowser.setOpenExternalLinks(True)
        """self.assignText('''<table cellpadding="4" cellspacing="0"
        style="border-width:1px;border-style:solid;border-color:red;">
        <tr><td>hello</td><td><a href="http://www.baidu.com/">Baidu</a></td></tr>
        <tr><td>hello</td><td><font color="red">world</font></td></tr>
        </table>''')"""
        self.yue = yue.Yue()
        content = self.yue.Login('2797', 'venus190597')
        if self.yue.IsLoginSucceed(content):
            self.assignText('<h2><font color="green">Login Successfully.</font></h2>')
        else:
            self.assignText(content)

    @QtCore.pyqtSignature('')
    def on_pushButton_clicked(self):
        url = unicode(self.leUrl.text())
        content = self.yue.Open(url)
        self.assignText(content)

    def assignText(self,text):
        self.htmlBrowser.setText(text)

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    frm = YueDlg()
    frm.show()
    app.exec_()

if __name__ == '__main__':
    main()
