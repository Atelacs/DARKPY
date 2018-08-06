import sys
import time
import datetime
import os
import shutil

# Test de fichier

DST = '/Users/darkmutch/DARKPY'
SRC = '/Users/darkmutch/'

N = 15
date_N_days_after = datetime.datetime.now() + datetime.timedelta(days=N)

print datetime.datetime.now().strftime("%m%d")
print date_N_days_after.strftime("%m%d")

D0 = datetime.datetime.now().strftime("%m%d")
D1 = date_N_days_after.strftime("%m%d")
F1 = 'C1Y%s0000%s00001'%(D0,D1)

print F1

if os.path.isfile(os.path.join(DST,F1)):
	print 'Destination Up 2 date'
	print 'Exit'
	sys.exit(0)
	
if os.path.isfile(os.path.join(SRC,F1)):
	print 'Source file received'
else:
	print 'Source File not received'
	print 'Exit'
	sys.exit(0)

print 'Copying File'
shutil.copy2(os.path.join(SRC,F1),DST)