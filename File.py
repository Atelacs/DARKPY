import time
import datetime
import os


# DST = '/data'
# SRC = '/ECPDS'

N = 15
date_N_days_after = datetime.datetime.now() + datetime.timedelta(days=N)

print datetime.datetime.now().strftime("%m%d")
print date_N_days_after.strftime("%m%d")

D0 = datetime.datetime.now().strftime("%m%d")
D1 = date_N_days_after.strftime("%m%d")
F1 = 'C1Y%s0000%s00001'%(D0,D1)


print F1

if os.path.isfile('./%s')%(F1)