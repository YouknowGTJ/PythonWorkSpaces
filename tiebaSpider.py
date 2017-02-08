# -*- coding: utf-8 -*-
# ---------------------------------------
#   程序：百度贴吧爬虫
#   版本：1.0
#   作者：gtj
#   日期：2017-02-06
#   语言：Python 2.7
#   操作：输入网址后自动只看楼主并保存到本地文件
#   功能：将楼主发布的内容打包txt存储到本地。
# ---------------------------------------

import urllib2
import re

# ----------- 处理页面上的各种标签 -----------
class HTML_Tool:
    # 用非 贪婪模式 匹配 \t 或者 \n 或者 空格 或者 超链接 或者 图片
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")
    # 用非 贪婪模式 匹配 任意<>标签
    EndCharToNoneRex = re.compile("<.*?>")
    # 用非 贪婪模式 匹配 任意<p>标签
    BgnPartRex = re.compile("<p.*?>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    CharToNextTabRex = re.compile("<td>")

    # 将一些html的符号实体转变为原始符号
    replaceTab = [("<", "<"), (">", ">"), ("&", "&"), ("&", "\""), (" ", " ")]

    def replace_char(self, x):
        x = self.BgnCharToNoneRex.sub("", x)
        x = self.BgnPartRex.sub("\n    ", x)
        x = self.CharToNewLineRex.sub("\n", x)
        x = self.CharToNextTabRex.sub("\t", x)
        x = self.EndCharToNoneRex.sub("", x)

        for t in self.replaceTab:
            x = x.replace(t[0], t[1])
        return x

class TiebaSpider:
        # 构造函数 , 初始化参数
        def __init__(self, url):
            # 默认只看楼主
            self.myurl = url + '?see_lz=1'
            self.page = 0
            self.title = ""
            self.data = []
            self.htmlTool = HTML_Tool()
            pass

        # 寻找标题函数  .  <span class="red">163</span>
        def total_page(self, content):
            if content is None:
                return
            match = re.search(r'class="red">(\d+?)</span>', content, re.S)
            if match:
                page = int(match.group(1))
                print u'爬虫报告：楼主内容一共有%d'% page
            else:
                page = 0
                print u'爬虫报告:楼主未发布任何内容'
            return page

        # 抓取帖子内容函数
        def collect_data(self):
            content = urllib2.urlopen(self.myurl).read().decode("utf-8")
            # 抓取帖子总页数
            self.page = self.total_page(content)
            # 抓取标题
            self.title = self.find_title(content)
            # 保存内容
            self.save_content(self.title, self.page)
            pass

        def save_content(self, title, page):
            self.get_data(self.myurl, page)
            try:
                with open('content.txt', 'w+') as txt:
                    txt.writelines(self.data)
            except Exception, e:
                print u'爬虫报告：保存文本文档时遇到了一些错误哦...'
                print e
            print u'爬虫报告：文件已下载到本地并打包成txt文件'
            print u'请按任意键退出...'
            raw_input()

        # 寻找标题函数
        def find_title(self, content):
            if content is None:
                return
            match = re.search(r'<title>(.*?)</title>', content, re.S)
            if match:
                title = match.group(1)
            else:
                title = u'暂无标题'
            print u'爬虫报告：标题是 ' + title
            return title

        def get_data(self, url, total_page):
            if url is None:
                return
            url += "？pn="
            for i in range(total_page):
                print u'爬虫报告： %d 号爬虫正在努力爬取...'%i
                respond = urllib2.urlopen((url + str(i))).read()
                self.deal_content(respond.decode("utf-8"))

        def deal_content(self, content):
            if content is None:
                return
            # <div id="post_content_103512131842" class="d_post_content j_d_post_content ">
            result = re.findall(r'<div id="post_content_.*?>(.*?)</div>',
                                content, re.S)
            if result is None:
                return
            for item in result:
                data = self.htmlTool.replace_char(item.replace("\n", " ").encode('utf-8'))
                self.data.append(data + "\n")

print u"""
#百度贴吧爬虫启动...
#请输入帖子最后一串数字..
 """

# 获取帖子url , 用户需要输入尾部数字串
myurl = "http://tieba.baidu.com/p/" + str(raw_input("http://tieba.baidu.com/p/"))
spider = TiebaSpider(myurl)
spider.collect_data()








