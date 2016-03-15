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
        self.setText('''<table cellpadding="4" cellspacing="0"
        style="border-width:1px;border-style:solid;border-color:red;">
        <tr><td>hello</td><td><a href="http://www.baidu.com/">Baidu</a></td></tr>
        <tr><td>hello</td><td><font color="red">world</font></td></tr>
        </table>''')
        self.yue = yue.Yue()
        self.yue.Login('2797', 'venus190597')

    @QtCore.pyqtSignature('')
    def on_pushButton_clicked(self):
        url = unicode(self.leUrl.text())
        page = self.yue.Open(url)
        content = self.yue.GetPageContent(page)
        self.setText(content)

    def setText(self,text):
        self.htmlBrowser.setText(text)

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    frm = YueDlg()
    frm.show()
    app.exec_()

if __name__ == '__main__':
    main()
