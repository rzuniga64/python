import urllib.request
import html.parser
import formatter
import re
import sys
from bs4 import BeautifulSoup

website = urllib.request.urlopen("http://ibm.com")
data = website.read()
website.close()
soup = BeautifulSoup(data)
for link in soup.find_all('a'):
    print(link.get('href'))




