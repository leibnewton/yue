# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:08:00 2016

@author: navicloud
"""

from datetime import datetime, time
from PyQt4 import QtGui, QtCore
import bs4
import yuetool_ui
import yue

class YueTool(QtGui.QDialog, yuetool_ui.Ui_Dialog):
    def __init__(self, parent = None):
        super(YueTool, self).__init__(parent)
        self.setupUi(self)
        self.yue = yue.Yue()
        yue.Yue.Debug = True

    def hideColumns(self, cols):
        # cols: column indexes start from 1
        hideColumnN = 'table td:nth-child(%d), table th:nth-child(%d) {display:none;}'
        return '\n'.join([hideColumnN % (col,col) for col in cols])

    @QtCore.pyqtSignature('')
    def on_pbRefresh_clicked(self):
        if self.rbOffDuty.isChecked():
            dateFrom = str(self.dateStart.date().toString("yyyy-MM-dd"))
            dateTo = str(self.dateEnd.date().toString("yyyy-MM-dd"))
            content = self.yue.GetKQ(dateFrom, dateTo)
            bdom = bs4.BeautifulSoup(content, 'lxml')

            # add style to hide uninterested columns from table here
            style = bdom.new_tag('style')
            style.append(self.hideColumns([3,6,7,8,9]))
            bdom.head.append(style)

            # remove contents except table
            body = bdom.body
            table = body.table.extract()
            body.clear()
            body.append(table)

            # remove rows in table if not overwork
            tds = table.select('td')
            for i in range(len(tds)/9):
                tstr = tds[9*i+4].text.strip()
                if tstr:
                    dstr = tds[9*i].text.strip()
                    dtstr = '%s %s'%(dstr, tstr)
                    dt = datetime.strptime(dtstr, '%Y-%m-%d %H:%M:%S')
                    ltime = time(8, 0)
                    rtime = self.timeRef.time().toPyTime()
                    if dt.weekday() <= 5 and not ltime<dt.time()<rtime: #weekday and over work
                        continue
                if yue.Yue.Debug: print 'remove', i, 'row', tstr
                tds[9*i].parent.decompose()

            content = bdom.prettify()
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
