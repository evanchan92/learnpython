from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import certifi

# 2019年02月26日13:00:07

pages= set()

def getlinks(pageurl):
    global pages
    html = urlopen("https://en.wikipedia.org" + pageurl)
    bsobj = BeautifulSoup(html)
    for link in bsobj.findAll("a", href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getlinks(newPage)

getlinks("")
