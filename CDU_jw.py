# -*- coding:utf-8 -*-
import webbrowser

__author__ = 'Jack Zhu'
import re, urllib, urllib2
import cookielib


class CDU_JW(object):
    def __init__(self):
        self.loginUrl = 'http://202.115.80.211/xs_main.aspx?xh=201310414616'
        self.cookies = cookielib.LWPCookieJar()
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
            'Connection': 'keep-alive',
            'Cookie': 'ASP.NET_SessionId=2z0sgl45rhnj55i0ayxy2jbe',
            'Host': '202.115.80.211',
            'Referer': 'http://202.115.80.211/default2.aspx',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        }
        self.postData = urllib.urlencode({
            ' __VIEWSTATE': 'dDwyODE2NTM0OTg7Oz6QI9jKiRNTC7s1M9cmt9rrpHNI5A==',
            'txtUserName': '201310414616',
            'TextBox2': 'zsw19941202.',
            'txtSecretCode': ''
        })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    def getCode(self, page):
        # 得到验证码的图片
        pattern = re.compile('<img id="icode" src="(.*?)" onclick.*?>', re.S)
        # 匹配的结果
        matchResult = re.search(pattern, page)
        # 已经匹配得到内容，并且验证码图片链接不为空
        if matchResult and matchResult.group(1):
            print matchResult.group(1)
            return matchResult.group(1)
        else:
            print u"没有找到验证码内容"
            return False

    # 获取登录界面
    def getPage(self):
        request = urllib2.Request(self.loginUrl)
        result = self.opener.open(request)
        # 打印登录内容
        return result.read().decode('gbk')

    # 获取登录之后的页面
    def loginPage(self):
        try:
            request = urllib2.Request(self.loginUrl, self.postData, self.headers)
            result = self.opener.open(request)
            print 1111
            # 打印登录内容
            print result.read().decode('gbk')
        except urllib2.HTTPError, e:
            print e.code

    def main(self):
        page = self.getPage()
        idenCode = self.getCode(page)
        # 得到了验证码的链接
        if not idenCode == False:
            print u"验证码获取成功"
            print u"请在浏览器中输入您看到的验证码"
            webbrowser.open_new_tab('http://202.115.80.211/' + idenCode)
            # 手动输入验证码
            code = raw_input("请输入浏览器中看到的验证码")
            # 将验证码的信息赋值给header
            self.headers['txtSecretCode'] = code
            print self.headers['txtSecretCode']
            self.loginPage()
            # 验证码链接为空，无效验证码
        else:
            print u"验证码获取失败，请重试"


cdu_jw = CDU_JW()
cdu_jw.main()
