from bs4 import BeautifulSoup
import requests

url = 'https://showrss.info/?cs=browse'
r = requests.get(url)
data = r.text

soup = BeautifulSoup(data,'lxml')
#all_show = soup.find_all('option')
show_value = soup.find_all('option',{'value' : True})
for value in show_value:
	print value.text
'''
my_file = open("show_detail", "wb")
for info in all_show:
	info.extract()
	
	//print('').join(info.findAll(text=True))
	
	my_file.write(str(info))
	my_file.write ("\n")
'''

