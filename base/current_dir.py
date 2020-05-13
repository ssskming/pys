#!/usr/bin/env python
# _*_ conding:UTF-8 _*_

import os
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 

curdir = 'D:\\temp\\'
if not os.path.exists(curdir):
    os.mkdir(curdir)

os.chdir(curdir)

file = open('dir.txt','w')

for root,dirs,files in os.walk('D:\\'):
    for name in files:
        FileName = os.path.join(root,name)
        #print(os.path.join(root,name))
        #print(FileName)
        try:
            file.write(FileName+"\n")
        except IOError:
            print("fdsafdsafdsa\n")
os.walk()
os.listdir(path)
file.close()