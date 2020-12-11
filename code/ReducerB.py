#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input1 = []
for line in sys.stdin:
    temp = line.strip()
    input1.append(temp)
temp2 = set(input1)
output1 = sorted(temp2)
for item in output1:
    print(item)

