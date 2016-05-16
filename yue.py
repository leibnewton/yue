#! /usr/bin/env python
# -*- coding:utf-8 -*-

import cookielib, urllib, urllib2
import bs4, HTMLParser
from urlparse import urlparse, urljoin

class StateExtracter(HTMLParser.HTMLParser):
    VIEWSTATE = '__VIEWSTATE'
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.__result = {}

    def feed(self, data):
        #print 'fed content of length: ', len(data)
        self.__result = {}
        return HTMLParser.HTMLParser.feed(self, data)

    def handle_starttag(self, tag, attrs):
        if tag == 'input':
            dattrs = dict(attrs)
            try:
                if dattrs['type'] not in ('submit', 'button'):
                    self.__result[str(dattrs['name'])] = str(dattrs['value']) #filter not ascii
            except: pass

    def GetResult(self, key):
        return self.__result.get(key, '')

    @property
    def result(self): # provide shallow copy
        return dict(self.__result)

class Yue(object):
    ORIGIN = 'http://172.26.10.41' #"http://oa-center.storm"  #
    ViewStates = {}
    Debug = False

    def __init__(self):
        self.__stateExtracter = StateExtracter()
        cookiejar = cookielib.CookieJar()
        self.urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

    def Login(self,usr,pwd):
      loginPage = urljoin(Yue.ORIGIN, "/Programs/login/login.aspx")
      values = {'tbUserName' :usr
               ,'tbPassword' :pwd
               ,'btnLogin':''}
      content = self._Post(loginPage, values)
      return content

    def GetKQ(self, dateFrom, dateTo):
        '''dateFrom & dateTo are strings in yyyy-mm-dd format'''
        url = '/Programs/KQ/EmployeeInfoStatistic.aspx'
        data = {'InfoSelect': 'RadioButtonPUNCH_CARD_INFO',
                'TimeSelect': 'RadioButtonDATE_SELECT',
                'TextBoxDATE_FROM': dateFrom,
                'TextBoxDATE_TO': dateTo}
        if Yue.Debug:
            print '-------------PAYLOAD----------------'
            print data
            print '------------------------------------'
        content = self.Fetch(url, data)
        return content

    def GetJBSQ(self, dateFrom, dateTo):
        '''return a dict:date to info.
        dateFrom & dateTo are strings in yyyy-mm-dd format'''
        url = '/Programs/KQ/EmployeeRequestOvertime.aspx'
        formdata = {'btnQuery':''}
        content = self.Fetch(url, formdata) #记录查找

        formdata = self.GetFormData(content)
        formdata['RecordSelect'] = 'RadioButtonALL'
        formdata['TextBoxDATE_FROM_SEARCH'] = dateFrom
        formdata['TextBoxDATE_TO_SEARCH'] = dateTo
        formdata['btnQuery'] = ''
        content = self.Fetch(url, formdata) #查找指定范围内所有记录

        formdata = self.GetFormData(content)
        jbsq = {'':['----', '----', '----', '']}
        count = 0
        while True:
            bdom = bs4.BeautifulSoup(content, 'lxml')
            total = bdom.select_one('#lblMsg')
            totalparts = total.text.split()
            if len(totalparts) == 1:
                if Yue.Debug: print 'no records in specified date range'
                break
            count = int(totalparts[1])
            table = bdom.select_one('#GridViewLINE')
            tds = table.select('td')
            key = tds[0].text.strip()  #起始日期
            values = []
            values.append(tds[2].text.strip())  #起始时间
            values.append(tds[3].text.strip())  #终止时间
            status = bdom.select_one('#LabelFLAG_VALUE')
            reason = bdom.select_one('#TextBoxREASON')
            values.append(status.text)     #当前状态
            values.append(reason['value']) #加班事由
            jbsq[key] = values
            btnPrev   = bdom.select_one('#btnPrev')
            if 'disabled' in btnPrev.attrs:
                if Yue.Debug: print 'no more records'
                break
            formdata['btnPrev'] = ''
            content  = self.Fetch(url, formdata) #获取下条记录
            formdata = self.GetFormData(content)
        return jbsq

    def IsLoginSucceed(self, content):
        return 'MainWindow.aspx' in content

    def SetViewState(self, url, data):
        stateKey = self.RegulateUrl(url)[1]
        if not Yue.ViewStates.has_key(stateKey):
            content = self._Open(url)
            self.UpdateViewState(url, content)
        value = Yue.ViewStates[stateKey]
        if value: # set VIEWSTATE
            data[StateExtracter.VIEWSTATE] = value

    def UpdateViewState(self, url, content):
        self.__stateExtracter.feed(content)
        stateKey = self.RegulateUrl(url)[1]
        value = self.__stateExtracter.GetResult(StateExtracter.VIEWSTATE)
        if value:
            origlen = len(Yue.ViewStates.get(stateKey, ''))
            Yue.ViewStates[stateKey] = value
            if Yue.Debug: print '%s viewstate: %d -> %d' % (stateKey, origlen, len(value))

    def RegulateUrl(self, url):
        o = urlparse(url)
        ## mismath between url and 'Origin' Header would cause a
        ## failure to get page
        url = urljoin(Yue.ORIGIN, o.path)
        return (url, o.path)

    def Fetch(self, url, data=None):
        url = self.RegulateUrl(url)[0]
        if not data:
            return self._Open(url)
        else:
            return self._Post(url, data)

    def _Open(self,url):
        page = self.urlOpener.open(url)
        content = self.GetPageContent(page)
        return content

    def _Post(self, url, data):
        if not data.has_key(StateExtracter.VIEWSTATE):
            self.SetViewState(url, data)
        data = urllib.urlencode(data)
        request = urllib2.Request(url, data)
        # These headers are not requisite, but for the sake of security.
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36')
        request.add_header('Referer', url)
        request.add_header('Origin',  Yue.ORIGIN)
        #request.add_header('Accept-Encoding', 'gzip, deflate')
        #request.add_header('Accept-Language', 'zh-CN,zh;q=0.8')
        page = self.urlOpener.open(request)  # Our cookiejar automatically receives the cookies
        content = self.GetPageContent(page)
        #self.UpdateViewState(url, content)
        return content

    def GetPageContent(self, page):
        content = page.read()
        charset = page.headers.getparam('charset')
        if not charset:
            doc = bs4.UnicodeDammit(content, is_html=True)
            charset = doc.original_encoding
        #print charset
        if charset:
            content = content.decode(charset) #content = QtCore.QString.fromUtf8(content)
        else:
            if Yue.Debug: print '<Unknown charset>'
        return content

    def GetFormData(self, content):
        '''extract form data except buttons'''
        self.__stateExtracter.feed(content)
        return self.__stateExtracter.result

if __name__ == '__main__':
    pass

