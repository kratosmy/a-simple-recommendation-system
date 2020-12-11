#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
setcount = {}
#read in the basket file
for line in sys.stdin:
    data = line.split(',')   #data[0] is userid, else are product ids
    data[-1] = data[-1].strip('\n')
    #this is the candidate file
    with open('outputphase2_final.txt','r') as fh:
        all_lines = fh.readlines()
        for line2 in all_lines:
            k1 = line2.split(',')
            k1[-1] = k1[-1].strip('\n')
            if k1[0] in data[1:]:
                if k1[1] in data[1:]:
                    try:
                        setcount[k1[0]+','+k1[1]] += 1
                    except:
                        setcount[k1[0]+','+k1[1]] = 1
            else:
                continue
for key, value in setcount.items():
    print(key+':'+str(value))

