from bs4 import BeautifulSoup
import lxml.etree as ET
import requests

url = 'http://new.showrss.info/show/266.rss'
r = requests.get(url)
data = r.text

soup = BeautifulSoup(data)
show_title = soup.find_all('title')
show_magent = soup.find_all('enclosure',{'url' : True})

for t in show_title:
	print('').join(t.find(text=True))
for magnet in show_magent:
	print magnet['url']
	print "\n"	


