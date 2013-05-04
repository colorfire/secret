#!/usr/bin/python

import codecs
import re
import urllib
import HTMLParser

#fl = codecs.open('265.html', encoding='gb2312')
fl = urllib.urlopen('http://www.265.com/Qiche_Qipei/')
s = fl.read()
urls = re.findall(r'<a(.+?)href=(?:"|\')?((?:https?://|/)[^\'"]+)(?:"|\')?(.*?)>(.+?)</a>',s.decode('gb2312'))
for url in urls:
    print '{"label":"%s", "href":"%s"},' % (url[3], url[1])


class HtmlStructureHandle(HTMLParser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
    def handle_endtag(self, tag):
        print tag
    def handle_data(self, data):
        print data


def parseWithReg(s):
    urls = re.findall(r'<a(.+?)href=(?:"|\')?((?:https?://|/)[^\'"]+)(?:"|\')?(.*?)>(.+?)</a>',s)
    result = None
    for url in urls:
        result += '{"label":"%s", "href":"%s"},\n' % (url[3], url[1])
    return result

def parseWithLib(s):
    parser = new HtmlStructureHandle()
    return parset.feed(s)

if __name__ == '__main__':
    print 'start parse script.'
