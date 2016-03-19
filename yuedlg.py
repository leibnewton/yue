# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:35:47 2016

@author: navicloud
"""
import time, io, traceback
from PyQt4 import QtCore, QtGui
import yuedlg_ui
import yue

class YueDlg(QtGui.QDialog, yuedlg_ui.Ui_Dialog):
    def __init__(self, parent=None):
        super(YueDlg, self).__init__(parent)
        self.setupUi(self)

        self.htmlBrowser.setOpenExternalLinks(True)
        self.yue = yue.Yue()
        content = self.yue.Login('2797', 'venus190597')
        if self.yue.IsLoginSucceed(content):
            self.assignText('<h2><font color="green">Login Successfully.</font></h2>')
        else:
            self.assignText(content)
        self.__formdata = {}
        self.__useFormData = False

    @QtCore.pyqtSignature('')
    def on_pushButton_clicked(self):
        url = unicode(self.leUrl.text())
        data = unicode(self.leParam.text())
        if data:
            data = eval(data)
        if self.__useFormData:
            if not data:
                data = self.__formdata
            else:
                for k in self.__formdata:
                    if k not in data:
                        data[k] = self.__formdata[k]
                print '-------------PAYLOAD----------------'
                print data
                print '------------------------------------'
        try:
            content = self.yue.Fetch(url, data)
            self.__formdata = self.yue.GetFormData(content)
            self.on_chkUseFormData_toggled(self.__useFormData)
        except Exception, e:
            content = '<h2><font color="red">%s</font></h2>' % e
            content += traceback.format_exc()
            self.__formdata = {}
        self.assignText(content)

        '''name = '/tmp/page%s.html'%time.time()
        with io.open(name, 'w', encoding='utf8') as f:
            f.write(content)
            print 'write to file: ', name'''

    @QtCore.pyqtSignature('bool')
    def on_chkUseFormData_toggled(self, checked):
        self.__useFormData = checked
        if self.__useFormData:
            print self.__formdata

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
