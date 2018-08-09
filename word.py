import os

file = 'test.ini'
F1 = 'TTTTTTTT'


import re
 
with open('test.ini') as f:
    for line in f:
#        line = line.strip()
        if re.match(r"naussac", line):
            print(line)

def replace_word(infile,old_word,new_word):
    if not os.path.isfile(infile):
        print ("Error on replace_word, not a regular file: "+infile)
        sys.exit(1)

    f1=open(infile,'r').read()
    f2=open(infile,'w')
    m=f1.replace(old_word,new_word)
    f2.write(m)

#replace_word('test.ini','toto',F1)

print 'End'