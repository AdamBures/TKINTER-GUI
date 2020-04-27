import bs4
from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen

url = "https://news.google.com/news/rss"
clien = urlopen(url)
xml_page = clien.read()
clien.close()

soup_page = soup(xml_page, "xml")
news_list = soup_page.findAll("item")
for new in news_list:
	print(new.title.text)
	print(new.link.text)
	print(new.pubDate.text)
	print("-"*60)