from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# Get all internal links of the pageself.
def getInternalLinks(bsobj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netlock
    internalLinks = []

    # Find all pages started with "/"
    for link in bsobj.findAll("a",href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
            else:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# Get all external links
def getExternalLinks(bsobj, excludeUrl):
    externalLinks = []
    # find all pages started with "http" or "www" and not included in internalLinks
    for link in bsobj.findAll("a", href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsobj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsobj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        print("No external links, looking around the site for one")
        domain = urlparse(startingPage).scheme + "://" + urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsobj,domain)
        internalLinks = getInternalLinks(startingPage)
        return getNextExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExtenalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("random external link is:" + externalLink)
    followExtenalOnly(externalLink)

followExtenalOnly("http://oreilly.com")
