from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsobj = BeautifulSoup(html)

namelist = bsobj.findAll("span",{"class":"green"})
for name in namelist:
    print(name.get_text())
    print(name)

alltext = bsobj.findAll(id = "text")
for s in alltext:
    print(s.get_text())

comment = bsobj.findAll(id = "comment")
