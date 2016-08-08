# -*- coding:utf-8 -*-
__author__ = 'Jack Zhu'

import re, urllib, urllib2
import webbrowser
import cookielib


class CDU(object):
    # 初始化方法
    def __init__(self):
        self.BaseUrl = 'http://202.115.80.211/default2.aspx'
        # 选择成绩的url
        self.gradeUrl = 'http://202.115.80.211/xscj_gc.aspx?xh=201310414616&xm=%D6%EC%CA%C7%CE%C4&gnmkdm=N121605'
        # 按学年选择成绩的URL
        self.ageGradeUrl = 'http://202.115.80.211/xscj_gc.aspx?xh=201310414616&xm=%D6%EC%CA%C7%CE%C4&gnmkdm=N121605'
        self.user_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        self.CaptchaUrl = 'http://202.115.80.211/'
        self.cookies = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        # 登陆界面的header
        self.loginHeaders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
            'Connection': 'keep-alive',
            'Cookie': 'ASP.NET_SessionId=dtaqlz45ql5tihyshux4rx45',
            'Host': '202.115.80.211',
            'Referer': 'http://202.115.80.211/default2.aspx',
            'user-Agent': self.user_Agent,
        }
        # 登陆过后选择选项header
        self.gradeHeaders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
            'Connection': 'keep-alive',
            'Cookie': 'ASP.NET_SessionId=dtaqlz45ql5tihyshux4rx45',
            'Host': '202.115.80.211',
            'Referer': 'http://202.115.80.211/xs_main.aspx?xh=201310414616',
            'user-Agent': self.user_Agent,
        }
        # 获取成绩header
        self.gradeGetHeaders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
            'Connection': 'keep-alive',
            'Cookie': 'ASP.NET_SessionId=dtaqlz45ql5tihyshux4rx45',
            'Host': '202.115.80.211',
            'Referer': 'http://202.115.80.211/xscj_gc.aspx?xh=201310414616&xm=%D6%EC%CA%C7%CE%C4&gnmkdm=N121605',
            'user-Agent': self.user_Agent,
        }
        self.login_PostData = urllib.urlencode({
            '__VIEWSTATE': self.get_VIEWSTATE(self.get_LoginPage()),
            'txtUserName': '201310414616',
            'TextBox2': 'zsw19941202.',
            'txtSecretCode': self.openCodePage(),
            'RadioButtonList1': '',
            'Button1': '',
            'lbLanguage': '',
            'hidPdrs': '',
            'hidsc': '',
        })
        # 建立历年成绩界面URL的data
        self.postData_Gra = urllib.urlencode({
            '__VIEWSTATE': 'dDwxODI2NTc3MzMwO3Q8cDxsPHhoOz47bDwyMDEzMTA0MTQ2MTY7Pj47bDxpPDE+Oz47bDx0PDtsPGk8MT47aTwzPjtpPDU+O2k8Nz47aTw5PjtpPDExPjtpPDEzPjtpPDE2PjtpPDI2PjtpPDI3PjtpPDI4PjtpPDM1PjtpPDM3PjtpPDM5PjtpPDQxPjtpPDQ1Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzlrablj7fvvJoyMDEzMTA0MTQ2MTY7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWnk+WQje+8muacseaYr+aWhzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85a2m6Zmi77ya5L+h5oGv56eR5a2m5LiO5bel56iL5a2m6ZmiOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuJPkuJrvvJo7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOi9r+S7tuW3peeoiyjmnKwpOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzooYzmlL/nj63vvJrova/ku7Yo5pysKTEzLTY7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDIwMTMwNDE0Oz4+Oz47Oz47dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPFhOO1hOOz4+Oz47dDxpPDQ+O0A8XGU7MjAxNS0yMDE2OzIwMTQtMjAxNTsyMDEzLTIwMTQ7PjtAPFxlOzIwMTUtMjAxNjsyMDE0LTIwMTU7MjAxMy0yMDE0Oz4+Oz47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8d2luZG93LnByaW50KClcOzs+Pj47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8d2luZG93LmNsb3NlKClcOzs+Pj47Oz47dDxwPHA8bDxWaXNpYmxlOz47bDxvPHQ+Oz4+Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDQ+Oz47bDx0PDtsPGk8MD47aTwxPjs+O2w8dDw7bDxpPDA+O2k8MT47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjs+O2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjs+O2w8dDw7bDxpPDA+Oz47bDx0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjtpPDE+Oz47bDx0PDtsPGk8MD47PjtsPHQ8QDA8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs+Ozs7Ozs7Ozs7Oz47Oz47Pj47dDw7bDxpPDA+Oz47bDx0PEAwPHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjs+O2w8dDw7bDxpPDA+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPENEVTs+Pjs+Ozs+Oz4+Oz4+Oz4+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47Pj47PqRjhAp6iIWF3g4a7aKz27WH7lS7',
            'ddlXN': '2013-2014',
            'ddlXQ': '1',
            'button1': '%B0%B4%D1%A7%C6%DA%B2%E9%D1%AF'
        })

    # 获取_VIEWSTATE参数
    def get_VIEWSTATE(self, page):
        pattern = re.compile(
                '<input type="hidden" name="__VIEWSTATE" value="(.*?)" />', re.S)
        result = re.search(pattern, page)
        # self.login_PostData['__VIEWSTATE'] = result.group(1)
        if result:
            return result.group(1)
        else:
            return False

    # 获取登录页面
    def get_LoginPage(self):
        try:
            request = urllib2.Request(self.BaseUrl)
            result = self.opener.open(request)
            return result.read().decode('gbk', 'ignore')
        except urllib2.URLError, e:
            print '错误原因：', e.reason
            return None

    def getCode(self, page):
        # 得到验证码的图片
        pattern = re.compile('<img id="icode" src="(.*?)" onclick.*?>', re.S)
        # 匹配的结果
        matchResult = re.search(pattern, page)
        # 已经匹配得到内容，并且验证码图片链接不为空
        if matchResult and matchResult.group(1):
            return matchResult.group(1)
        else:
            print u"没有找到验证码内容"
            return False

    def openCodePage(self):
        identCode = self.getCode(self.get_LoginPage())
        # 得到了验证码的链接
        if not identCode == False:
            print u"--------验证码获取成功!------------"
            print u"--请在浏览器中输入您看到的验证码!--"
            webbrowser.open_new_tab('http://202.115.80.211/' + identCode)
            # 手动输入验证码
            code = raw_input("----请输入浏览器中看到的验证码:----\n")
            # 将验证码的信息赋值给postData
            return code
            # 验证码链接为空，无效验证码
        else:
            print u"验证码获取失败，请重试"

    def getPage(self):
        request = urllib2.Request(self.BaseUrl, self.login_PostData, self.loginHeaders)
        request2 = urllib2.Request(self.gradeUrl, headers=self.gradeHeaders)
        request3 = urllib2.Request(self.ageGradeUrl, self.postData_Gra, self.gradeGetHeaders)
        result = self.opener.open(request)
        result = self.opener.open(request2)
        result = self.opener.open(request3)
        print result.read().decode('gbk')

    # 保存信息
    def save(self):
        pass

    # 主运行方法
    def main(self):
        # is_get_VIEW = self.get_VIEWSTATE(LoginPage)
        # identCode = self.getCode(LoginPage)
        self.getPage()


cdu = CDU()
cdu.main()
