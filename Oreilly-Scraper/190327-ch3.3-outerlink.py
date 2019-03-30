from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# get all internal links
def getInternalLinks(bsObj,includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []
    # find all links started with "/"
    for link in bsObj.findAll("a",href = re.compile("^(/|.*"includeUrl+")")):
        if link.attrs['href'] is not None:
            if links.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
            else:
                internalLinks.append(link.attrs['href'])
    return internalLinks


def getExternalLinks
