from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# Get all internal links
def getInternalLinks(includeUrl):
    includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
    # scheme = 协议,是 http 还是 https 还是 ftp
    # netloc = 域名,例如 www.wikipedia.org
    # 这段代码的意思就是,输入一个网址,只截取本站内容

    ## 找出所有以"/"开头的链接
    internalLinks = []
    for link in bsObj.findAll("a",href = re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
            else:
                internalLinks.append(link.attrs['href'])
    return internalLinks


getInternalLinks("www.yangzhiping.com")
