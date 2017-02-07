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


class HtmlToo:
    pass


class TiebaSpider:
        # 构造函数 , 初始化参数
        def __init__(self, url):
            # 默认只看楼主
            self.myurl = url + '?see_lz=1'
            self.page = 0
            self.title = ""
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
            pass

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


print u"""
#百度贴吧爬虫启动...
#请输入帖子最后一串数字..
 """

# 获取帖子url , 用户需要输入尾部数字串
myurl = "http://tieba.baidu.com/p/" + str(raw_input("http://tieba.baidu.com/p/"))

spider = TiebaSpider(myurl)
spider.collect_data()








