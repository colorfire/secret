import codecs
import re

fl = codecs.open('265.html', encoding='gb2312')
s = fl.read()
urls = re.findall(r'<a(.+?)href=(?:"|\')?((?:https?://|/)[^\'"]+)(?:"|\')?(.*?)>(.+?)</a>',s)
for url in urls:
    print '{"label":"%s", "href":"%s"},' % (url[3], url[1])
