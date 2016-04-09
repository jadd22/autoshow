from bs4 import BeautifulSoup
import urllib2
import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
url = "http://new.showrss.info/browse"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'pl-PL,pl;q=0.8',
       'Connection': 'keep-alive'}
       
req = urllib2.Request(url,headers=hdr)
page = urllib2.urlopen(req,context=context)
content = page.read()
soup = BeautifulSoup(content)
value = soup.find_all('option',{'value' : True})
print value.text
