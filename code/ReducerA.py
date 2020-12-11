#!/usr/bin/env python3
# coding: utf-8

# In[ ]:


import sys

for line in sys.stdin:
    temp = line.strip(',')
    data = temp.split(',')
    for item in data[:-2]:
        print(item,end=',')
    print(data[-2])

