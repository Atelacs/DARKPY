import sys
import fileinput

F1 = 'CDR111000983748505'

file = open("testfile.txt","w") 
 
file.write('[uwsgi]\n') 
file.write('env = LD_LIBRARY_PATH=/opt/ecmwf/eccodes/lib\n') 
file.write('env = ECMWF_WMS_SERVER_DATA_PATH=/data/'+F1+'\n')
file.write('pidfile = /var/log/uwsgi/wms-server.pid\n')
file.close()