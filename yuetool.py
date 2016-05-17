# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:08:00 2016

@author: navicloud
"""

from datetime import datetime, time, date
from dateutil.relativedelta import relativedelta
import copy
from PyQt4 import QtGui, QtCore
import bs4
import yuetool_ui
import yue

class YueTool(QtGui.QDialog, yuetool_ui.Ui_Dialog):
    ScriptCode="""function getSelected()
{
  var chx = document.querySelectorAll('input[type=checkbox]');
  var selected = [];
  for(var i=0; i<chx.length; i++){
    if(chx[i].checked){
      selected.push(chx[i].getAttribute('key'));
    }
  }
  return selected.toString();
}"""
    def __init__(self, parent = None):
        super(YueTool, self).__init__(parent)
        self.setupUi(self)
        self.cmbType.addItem(u'智能判断')
        self.cmbType.addItem(u'平日加班')
        self.cmbType.addItem(u'双休日加班')
        self.yue = yue.Yue()
        yue.Yue.Debug = True

    def hideColumns(self, cols):
        # cols: column indexes start from 1
        hideColumnN = 'table td:nth-child(%d), table th:nth-child(%d) {display:none;}'
        return '\n'.join([hideColumnN % (col,col) for col in cols])

    def addColumns(self, table, colnames):
        header = table.find('tr')
        th = header.find('th')
        for colname in colnames:
            thnew = copy.copy(th)
            thnew.string = colname
            header.append(thnew)

    def addCells(self, row, td, values):
        for value in values:
            tdnew = copy.copy(td)
            tdnew.string = value
            row.append(tdnew)

    def addCheckBox(self, row, td, chkbox, key):
        tdnew = copy.copy(td)
        tdnew.clear()
        chknew = copy.copy(chkbox)
        chknew['key'] = key
        tdnew.append(chknew)
        row.append(tdnew)

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
                    if not ltime<dt.time()<rtime: # over work [and weekday] (dt.weekday() <= 5)
                        continue
                if yue.Yue.Debug: print 'remove', i, 'row', tstr
                tds[9*i].parent.decompose()

        elif self.rbApplication.isChecked():
            start = today = date.today()
            if today.day < 11:
                start = today - relativedelta(months=1)
            start = date(start.year, start.month, 1)
            dateFrom = start.strftime('%Y-%m-%d')
            dateTo   = today.strftime('%Y-%m-%d')
            jbsq = self.yue.GetJBSQ(dateFrom, dateTo)

            content = self.yue.GetKQ(dateFrom, dateTo)
            bdom = bs4.BeautifulSoup(content, 'lxml')

            # add style to hide uninterested columns from table here
            style = bdom.new_tag('style')
            style.append(self.hideColumns([3,6,7,8,9]))
            bdom.head.append(style)

            # add scripts to get checkbox selected states
            script = bdom.new_tag('script')
            script.append(YueTool.ScriptCode)
            bdom.head.append(script)

            table = bdom.body.table.extract()
            bdom.body.clear()
            bdom.body.append(table)

            # add header columns: start, end, status, checkbox
            self.addColumns(table, [u'起始时间', u'终止时间', u'目前状态', u'添加申请'])

            chkbox = bdom.new_tag('input')
            chkbox['type'] = 'checkbox'
            chkbox['checked'] = 'checked'
            tds = table.select('td')
            for i in range(len(tds)/9):
                row = tds[9*i].parent
                s_tstart = tds[9*i+3].text.strip()
                s_dstart = tds[9*i].text.strip()
                if s_tstart:
                    s_dtstart  = '%s %s'%(s_dstart, s_tstart)
                    dtstart    = datetime.strptime(s_dtstart, '%Y-%m-%d %H:%M:%S')

                    s_tend  = tds[9*i+4].text.strip()
                    s_dend  = s_dstart
                    s_dtend = '%s %s'%(s_dend, s_tend)
                    dtend   = datetime.strptime(s_dtend, '%Y-%m-%d %H:%M:%S')
                    if dtend < dtstart:
                        dtend  = dtend + relativedelta(days=1)
                        s_dend = dtend.strftime('%Y-%m-%d')
                    if dtstart.weekday() >= 5 or dtend > dtstart + relativedelta(hours=9.6): #weekend or normal work
                        # add data columns: start, end, status, checkbox
                        if s_dstart in jbsq:
                            self.addCells(row, tds[9*i], jbsq[s_dstart][:3]+[''])
                        else:
                            self.addCells(row, tds[9*i], jbsq[''][:3])
                            self.addCheckBox(row, tds[9*i], chkbox, s_dstart)
                        continue
                if yue.Yue.Debug: print 'remove', i, 'row', s_dtend if s_tstart else s_dstart
                row.decompose()

        content = bdom.prettify()
        self.webView.setHtml(content)

    @QtCore.pyqtSignature('')
    def on_pbApply_clicked(self):
        frame = self.webView.page().mainFrame()
        result = frame.evaluateJavaScript('getSelected()')
        selected = str(result.toString()).split(',')
        print selected

    def showEvent(self, event):
        with open('passwd', 'r') as f:
            text = f.read()
            text = text.split()
            if len(text) < 2:
                print 'please provide username and password in "passwd" file'
                return
            usr, pwd = text[:2]
        content = self.yue.Login(usr, pwd)
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
