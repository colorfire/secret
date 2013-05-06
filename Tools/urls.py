#!/usr/bin/python

import sys
import codecs
import re
import urllib
import json
from bs4 import BeautifulSoup

#fl = codecs.open('265.html', encoding='gb2312')
#fl = urllib.urlopen('http://www.265.com/Qiche_Qipei/')
#s = fl.read()
#urls = re.findall(r'<a(.+?)href=(?:"|\')?((?:https?://|/)[^\'"]+)(?:"|\')?(.*?)>(.+?)</a>',s.decode('gb2312'))
#for url in urls:
#    print '{"label":"%s", "href":"%s"},' % (url[3], url[1])

def parseWithReg(s):
    urls = re.findall(r'<a(.+?)href=(?:"|\')?((?:https?://|/)[^\'"]+)(?:"|\')?(.*?)>(.+?)</a>',s)
    result = None
    for url in urls:
        result += '{"label":"%s", "href":"%s"},\n' % (url[3], url[1])
    return result

def parseWithLib(s):
    subs = []
    soup = BeautifulSoup(s)
    for content in soup.find_all('div', class_='catalogCategory'):
        sub = {}
        cs = BeautifulSoup(content.prettify())
        title = cs.find('div', class_='titleCS')

        links = []
        ul = cs.find('ul', class_='listUrl')
        us = BeautifulSoup(ul.prettify())
        for link in us.find_all('a'):
            tmp = {'label':_trim(link.string), 'href':link['href']}
            links.append(tmp)

        relates = []
        dl = cs.find('dl', class_='SoKeys')
        ds = BeautifulSoup(dl.prettify())
        for dd in ds.find_all('a'):
            tmp = {'label':_trim(dd.string), 'href':dd['href']}
            relates.append(tmp)
        sub['title'] = {'label':_trim(title.string)}
        sub['links'] = links
        sub['relate'] = relates
        subs.append(sub)
    result = {'id':'s', 'subs':subs}
    return result

def _trim(string):
    return string.replace('\n', '').strip()

if __name__ == '__main__':
    print 'start parse script.'
    #fl = codecs.open('shipin.html', encoding='gb2312')
    #s = fl.read()
    if len(sys.argv) < 1:
        print 'Error Parameter.'
        sys.exit(0)
    fl = urllib.urlopen(sys.argv[1])
    s = fl.read().decode('gb2312')
    print json.dumps(parseWithLib(s))
    print 'end parse script.'
