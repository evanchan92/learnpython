"""
Get all links within 1 website
Be careful about the redundant links.
目标:把老阳博客里面所有打 psy 标签的博文找出来
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("https://www.yangzhiping.com"+pageUrl)
    bsObj = BeautifulSoup(html)
    try:
        print(bsObj.findAll("a",href = re.compile("^(/psy)")))

    except AttributeError:
        print("No worries")

    for link in bsObj.findAll("a",href=re.compile("(/psy/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")
