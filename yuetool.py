# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:08:00 2016

@author: navicloud
"""

from datetime import datetime, time, date
from dateutil.relativedelta import relativedelta
from time import sleep
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
        self.cmbType.addItems([u'智能判断', u'平日加班', u'双休日加班'])
        self.yue = yue.Yue()
        yue.Yue.Debug = True
        self.waitToApply = {}
        self.on_rbApplication_toggled(True)

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
            if value == u'已经批准':
              tdnew['style'] += ';color:green;'
            row.append(tdnew)

    def addCheckBox(self, row, td, chkbox, key):
        tdnew = copy.copy(td)
        tdnew.clear()
        chknew = copy.copy(chkbox)
        chknew['key'] = key
        tdnew.append(chknew)
        row.append(tdnew)

    @QtCore.pyqtSignature('bool')
    def on_rbApplication_toggled(self, checked):
        if checked:
            self.pbApply.setEnabled(True if self.waitToApply else False)

    @QtCore.pyqtSignature('')
    def on_pbRefresh_clicked(self):
        self.waitToApply = {}
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
            jbsq, reasons = self.yue.GetJBSQ(dateFrom, dateTo)
            if reasons:
                self.cmbReason.clear()
                self.cmbReason.addItems(reasons)

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
            #chkbox['checked'] = 'checked'
            tds = table.select('td')
            for i in range(len(tds)/9):
                row = tds[9*i].parent
                s_dstart = tds[9*i].text.strip()
                s_tstart = tds[9*i+3].text.strip()
                s_dtstart= '%s %s'%(s_dstart, s_tstart)
                s_dend   = s_dstart
                s_tend   = tds[9*i+4].text.strip()
                s_dtend  = '%s %s'%(s_dend, s_tend)
                if s_tstart and s_tend:
                    dtstart = datetime.strptime(s_dtstart, '%Y-%m-%d %H:%M:%S')
                    dtend   = datetime.strptime(s_dtend, '%Y-%m-%d %H:%M:%S')
                    if dtend < dtstart:
                        dtend  = dtend + relativedelta(days=1)
                        s_dend = dtend.strftime('%Y-%m-%d')
                    if dtstart.weekday() >= 5 or dtend > dtstart + relativedelta(hours=9.6) or (dtstart.time() > time(10, 0, 59) and dtend.time() > time(18, 35, 0)): #weekend or normal work
                        # add data columns: start, end, status, checkbox
                        if s_dstart in jbsq: # and jbsq[s_dstart][2] != u'退回':
                            self.addCells(row, tds[9*i], jbsq[s_dstart]+[''])
                        else:
                            self.addCells(row, tds[9*i], yue.Yue.EMPTYJBSQ)
                            self.addCheckBox(row, tds[9*i], chkbox, s_dstart)
                            self.waitToApply[s_dstart] = (dtstart, dtend)
                        continue
                if yue.Yue.Debug: print 'remove', i, 'row', s_dtend if s_tend else s_dtstart
                row.decompose()
            self.on_rbApplication_toggled(True)

        content = bdom.prettify()
        self.webView.setHtml(content)

    @QtCore.pyqtSignature('')
    def on_pbApply_clicked(self):
        frame = self.webView.page().mainFrame()
        result = frame.evaluateJavaScript('getSelected()')
        selected = str(result.toString()).split(',')
        if yue.Yue.Debug: print selected
        reason = unicode(self.cmbReason.currentText())
        strategy = self.cmbType.currentIndex()
        leftcnt = len(selected) - 1
        for item in selected:
            dates = self.waitToApply[item]
            if self.yue.AddJBSQ(dates[0], dates[1], reason, strategy) and leftcnt > 0:
                sleep(1.0)
                leftcnt -= 1
        self.on_pbRefresh_clicked()

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
