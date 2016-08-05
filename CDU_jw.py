# -*- coding:utf-8 -*-
import webbrowser

__author__ = 'Jack Zhu'
import re, urllib, urllib2
import cookielib


class CDU_JW(object):
    def __init__(self):
        self.loginUrl = 'http://202.115.80.211/xs_main.aspx?xh=201310414616'
        # self.gradeUrl = 'http://202.115.80.211/xscj_gc.aspx?xh=201310414616&xm=ÖìÊÇÎÄ&gnmkdm=N121605'
        self.cookies = cookielib.LWPCookieJar()
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
            'Connection': 'keep-alive',
            'Cookie': 'ASP.NET_SessionId=sgvwsr5500t23t55ahi1s52h',
            'Host': '202.115.80.211',
            'Referer': 'http://202.115.80.211/default2.aspx',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        }
        self.postData = urllib.urlencode({
            ' __VIEWSTATE': 'dDwyODE2NTM0OTg7Oz6fTkswzvoC3jU9hyDj/HczY8+tQQ==',
            'txtUserName': '201310414616',
            'TextBox2': 'zsw19941202.',
            'ddlXN': '2015-2016',
            'ddlXQ': '2',
            'txtSecretCode': ''
        })
        self.gradeGetData = urllib.urlencode({
            # ' __VIEWSTATE': 'dDwxODI2NTc3MzMwO3Q8cDxsPHhoOz47bDwyMDEzMTA0MTQ2MTY7Pj47bDxpPDE+Oz47bDx0PDtsPGk8MT47aTwzPjtpPDU+O2k8Nz47aTw5PjtpPDExPjtpPDEzPjtpPDE2PjtpPDI2PjtpPDI3PjtpPDI4PjtpPDM1PjtpPDM3PjtpPDM5PjtpPDQxPjtpPDQ1Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzlrablj7fvvJoyMDEzMTA0MTQ2MTY7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWnk+WQje+8muacseaYr+aWhzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85a2m6Zmi77ya5L+h5oGv56eR5a2m5LiO5bel56iL5a2m6ZmiOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuJPkuJrvvJo7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOi9r+S7tuW3peeoiyjmnKwpOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzooYzmlL/nj63vvJrova/ku7Yo5pysKTEzLTY7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDIwMTMwNDE0Oz4+Oz47Oz47dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPFhOO1hOOz4+Oz47dDxpPDQ+O0A8XGU7MjAxNS0yMDE2OzIwMTQtMjAxNTsyMDEzLTIwMTQ7PjtAPFxlOzIwMTUtMjAxNjsyMDE0LTIwMTU7MjAxMy0yMDE0Oz4+Oz47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8d2luZG93LnByaW50KClcOzs+Pj47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8d2luZG93LmNsb3NlKClcOzs+Pj47Oz47dDxwPHA8bDxWaXNpYmxlOz47bDxvPHQ+Oz4+Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDQ+Oz47bDx0PDtsPGk8MD47aTwxPjs+O2w8dDw7bDxpPDA+O2k8MT47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjs+O2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjs+O2w8dDw7bDxpPDA+Oz47bDx0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjtpPDE+Oz47bDx0PDtsPGk8MD47PjtsPHQ8QDA8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs+Ozs7Ozs7Ozs7Oz47Oz47Pj47dDw7bDxpPDA+Oz47bDx0PEAwPHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjs+O2w8dDw7bDxpPDA+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPENEVTs+Pjs+Ozs+Oz4+Oz4+Oz4+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47Pj47PjeIYCYyQsRUULkNHcjhGTS/qFrM',
            'xh': '201310414616',
            'xm': '朱是文',
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
            # 获取登录内容
            print result.read().decode('gbk')
        except urllib2.HTTPError, e:
            print e.code

    # 获取成绩链接
    def getGradePage(self):
        head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': '222.24.19.201',
            'Cookie': 'ASP.NET_SessionId=sgvwsr5500t23t55ahi1s52h',
            'Origin': 'http://222.24.19.201',
            'Pragma': 'no-cache',
            'Referer': 'http://222.24.19.201/xs_main.aspx?xh=201310414616',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36'
        }
        loginUrl = 'http://202.115.80.211/xscj_gc.aspx?' + self.gradeGetData
        try:
            request = urllib2.Request(loginUrl, None, head)  # , self.gradeHeaders
            result = self.opener.open(request)
            self.getGrade()
            # print result.read().decode('gbk')
        except urllib2.HTTPError, e:
            print e.code

    def getGrade(self):
        gradeGetData = urllib.urlencode({
            ' __VIEWSTATE': 'dDwxODI2NTc3MzMwO3Q8cDxsPHhoOz47bDwyMDEzMTA0MTQ2MTY7Pj47bDxpPDE+Oz47bDx0PDtsPGk8MT47aTwzPjtpPDU+O2k8Nz47aTw5PjtpPDExPjtpPDEzPjtpPDE2PjtpPDI2PjtpPDI3PjtpPDI4PjtpPDM1PjtpPDM3PjtpPDM5PjtpPDQxPjtpPDQ1Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzlrablj7fvvJoyMDEzMTA0MTQ2MTY7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWnk+WQje+8muacseaYr+aWhzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85a2m6Zmi77ya5L+h5oGv56eR5a2m5LiO5bel56iL5a2m6ZmiOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuJPkuJrvvJo7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOi9r+S7tuW3peeoiyjmnKwpOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzooYzmlL/nj63vvJrova/ku7Yo5pysKTEzLTY7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDIwMTMwNDE0Oz4+Oz47Oz47dDx0PHA8cDxsPERhdGFUZXh0RmllbGQ7RGF0YVZhbHVlRmllbGQ7PjtsPFhOO1hOOz4+Oz47dDxpPDQ+O0A8XGU7MjAxNS0yMDE2OzIwMTQtMjAxNTsyMDEzLTIwMTQ7PjtAPFxlOzIwMTUtMjAxNjsyMDE0LTIwMTU7MjAxMy0yMDE0Oz4+Oz47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8d2luZG93LnByaW50KClcOzs+Pj47Oz47dDxwPDtwPGw8b25jbGljazs+O2w8d2luZG93LmNsb3NlKClcOzs+Pj47Oz47dDxwPHA8bDxWaXNpYmxlOz47bDxvPHQ+Oz4+Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDQ+Oz47bDx0PDtsPGk8MD47aTwxPjs+O2w8dDw7bDxpPDA+O2k8MT47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjs+O2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjs+O2w8dDw7bDxpPDA+Oz47bDx0PEAwPDs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjtpPDE+Oz47bDx0PDtsPGk8MD47PjtsPHQ8QDA8cDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+Pjs+Ozs7Ozs7Ozs7Oz47Oz47Pj47dDw7bDxpPDA+Oz47bDx0PEAwPHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Ozs7Ozs7Ozs+Ozs+Oz4+Oz4+O3Q8O2w8aTwwPjs+O2w8dDw7bDxpPDA+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPENEVTs+Pjs+Ozs+Oz4+Oz4+Oz4+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47Pj47PjeIYCYyQsRUULkNHcjhGTS/qFrM',
            # 'ddlXN': '2015-2016',
            # 'ddlXQ': '2',
            'Button2': '在校学习成绩查询'
        })
        head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': '222.24.19.201',
            'Cookie': 'ASP.NET_SessionId=sgvwsr5500t23t55ahi1s52h',
            'Origin': 'http://222.24.19.201',
            'Pragma': 'no-cache',
            'Referer': 'http://222.24.19.201/xs_main.aspx?' + self.gradeGetData,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36'
        }
        loginUrl = 'http://202.115.80.211/xscj_gc.aspx?' + self.gradeGetData
        try:
            request = urllib2.Request(loginUrl, gradeGetData, head)  # , self.gradeHeaders
            result = self.opener.open(request)
            # print result.read().decode('gbk')
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
            self.getGradePage()
        else:
            print u"验证码获取失败，请重试"


cdu_jw = CDU_JW()
cdu_jw.main()
