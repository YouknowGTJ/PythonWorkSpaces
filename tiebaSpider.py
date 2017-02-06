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

class HtmlToo:
    pass


class TiebaSpider:

        # 构造函数 , 初始化参数
        def __init__(self, url):
            # 默认只看楼主
            self.myurl = url + '?see_lz=1'
            pass

        # 寻找标题函数
        def total_page(self, page):
            urlsf="sdfs"
            pass

        # 抓取帖子内容函数
        def fetch_data(self):
            page = urllib2.urlopen(self.myurl).read().decode("utf-8")
            self.total_page(page)
            pass

        # 寻找标题函数
        def find_title(self):
            pass
            pass


print u"""#百度贴吧爬虫启动...
请输入帖子最后一串数字..
 """
# 获取帖子url , 用户需要输入尾部数字串
myurl = "http://tieba.baidu.com/p/" + str(raw_input("http://tieba.baidu.com/p/"))

spider = TiebaSpider(myurl)
spider.fetch_data()








