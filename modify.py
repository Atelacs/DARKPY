import sys


import string
s = open("test.ini","r+")
for line in s.readlines():
   print line
   string.replace(line, 'mickey','minnie')
   print line
s.close()


#s = open('test.ini').read()
#s = s.replace('C1Y%', 'test')
#print(message)
#s.close()

#f = open('test.ini', 'w')
#f.write(s)
#f.close()