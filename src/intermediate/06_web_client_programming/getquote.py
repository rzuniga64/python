import urllib.request
import re
import sys

symbol = sys.argv[1]
# query string
url = 'http://finance.google.com/finance?q='
content = urllib.request.urlopen(url+symbol).read()
#m = re.search('span id="ref.*>(.*)<', content)
m = re.search('"price" content=', content)
if m:
    quote = m.group(1)
else:
    quote = 'no quote for symbol: ' + symbol
print(quote)