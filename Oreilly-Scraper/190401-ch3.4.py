from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# Get all internal links
def getInternalLinks(bsObj, includeUrl):
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

# Get all External Links
def getExternalLinks(bsObj,excludeUrl):
    externalLinks = []
    # find all links started with http or www and exclude current url.
    for link in bsObj.findAll("a", href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        print("No external link, looking around the site for one")
        domain = urlparse(startingPage).scheme + "://" + urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj,domain)
        return getNextExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])

    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is:" + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://www.yangzhiping.com")
