import linecache
import os
import time
import sys
from subprocess import Popen, PIPE

# logname='C:\\Users\\ismma\\Desktop\\Ucheba\\Игросфера\\Git\\log'
log3='log'
as1=os.listdir(log3)
logname='log.log'
pattern = "Error"
base_suffix = ".log"
for log in pattern:
    path = "import_logs.py {log_name}{suffix}".format(
                 log_name=log, suffix=base_suffix)

# print (Popen(stdout = PIPE, shell = True).stdout.read())
# with open(logname, 'rt') as file:
#     for index, line in enumerate(file):
#         if pattern in line:
#             sys.stdout.write('\rПроверено' +' - '+ "%r" % index)
#             sys.stdout.flush()
#             # print(index+1,linecache.getline(logname, index+1))
#             a=open("home.txt",'a')
#             a.write(linecache.getline(logname, index+1))