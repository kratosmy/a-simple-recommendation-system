#!/usr/bin/env python3
# coding: utf-8

# In[ ]:


import sys
totalcount = {}
threshold = 60
for line in sys.stdin:
    data = line.split(':')
    data[-1] = data[-1].strip('\n')
    product = data[0]
    count = data[1]
    product = data[0].split(',')
    try:
        totalcount[product[0]+','+product[1]] += int(count)
        continue     #only execute when succeed
    except:
        pass
    try:
        totalcount[product[1]+','+product[0]] += int(count)
    except:
        totalcount[product[0]+','+product[1]] = int(count)
        
finaloutput={}
for key, value in totalcount.items():
    if totalcount[key] >= threshold:
        finaloutput[key] = value    
for key, value in finaloutput.items():    
    print(key+':'+str(value))

