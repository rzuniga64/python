#Read a network usegroup using pythpm using comp.lang.python language newsgroup

#network news tranfser protocol library
from nntplib import *

#use a network that stores network news: web.aioe.org
#google free network news servers
s = NNTP('web.aioe.org')

#connect to the server, provide a list of data vars to be received when going to make a connection to the network
(resp, count, first, last, name) = s.group('comp.lang.python')
(resp, subs) = s.xhdr('subject', {str(first)+'-'+str(last)})
for subject in subs[-10:]:
    print(subject)
number = input('Which article do you want to read? ')
(reply, num, id, list) = s.body(str(number))
for line in list:
   print(line)