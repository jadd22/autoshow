from bs4 import BeautifulSoup
import requests

url = "http://new.showrss.info/browse"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data,'lxml')

recent_show = soup.find_all('div',{'class' : 'col-md-12'})
my_file = open('recent_show_list.txt', 'wb')
for i in recent_show:
	print i.text
	my_file.write(i.text)
