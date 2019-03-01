from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://search.jd.com/Search?keyword=%E8%BF%9B%E5%8F%A3%E9%9B%B6%E9%A3%9F&enc=utf-8&wq=%E8%BF%9B%E5%8F%A3%E9%9B%B6%E9%A3%9F&pvid=ryxp9pui.nhltvu")
bsobj = BeautifulSoup(html)

prices = bsobj.findAll("",{"class":"p-price"})
for price in prices:
    print(price.get_text())
goods_names = bsobj.findAll("",{"class":"p-name p-name-type-2"})
for goods_name in goods_names:
    print(goods_name.get_text().strip())
