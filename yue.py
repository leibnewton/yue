#! /usr/bin/env python
# -*- coding:utf-8 -*-

import cookielib, urllib, urllib2
import bs4

class Yue(object):
    ORIGIN = "http://oa-center.storm"
    def Login(self,usr,pwd):
      cookiejar = cookielib.CookieJar()
      self.urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
      viewState = '/wEPDwUJNDIzOTY1MjU5DxYEHg5NdXN0Q2hlY2tSaWdodGgeClBhZ2VVc2VySURlFgICAQ9kFgICBQ8PZBYCHgxBVVRPQ09NUExFVEUFA29mZmRkV1Hchudp6r72LgVP7TF2g2n4bIY='
      stateGen = 'E19C8057'
      btnLogin = '确定'
      loginPage = Yue.ORIGIN + "/Programs/login/login.aspx"
      values = {'tbUserName' :usr
               ,'tbPassword' :pwd
               ,'__VIEWSTATE':viewState
               #,'__VIEWSTATEGENERATOR':stateGen
               ,'btnLogin':''
               }
      #url = self.urlOpener.open(loginPage)
      url = self.Post(loginPage, values)
      page = url.read()
      res  = True
      if 'MainWindow.aspx' in page:
        print 'Login Succeeded!'
      else:
        res = False
        print 'Login Failed...\n', page
      return res

    def Open(self,url):
        page = self.urlOpener.open(url)
        return page

    def Post(self, url, data=None):
        if not data:
            return self.Open(url)
        if not type(data) is str:
            data = urllib.urlencode(data)
        request = urllib2.Request(url, data)
        # These headers are not requisite, but for the sake of security.
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36')
        request.add_header('Referer', url)
        request.add_header('Origin',  Yue.ORIGIN)
        #request.add_header('Accept-Encoding', 'gzip, deflate')
        #request.add_header('Accept-Language', 'zh-CN,zh;q=0.8')
        page = self.urlOpener.open(request)  # Our cookiejar automatically receives the cookies
        return page

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
            print '<Unknown charset>'
        return content

if __name__ == '__main__':
  Login('2797', 'vens1997')

