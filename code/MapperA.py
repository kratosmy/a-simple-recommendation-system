#!/usr/bin/env python3
# coding: utf-8

# In[ ]:


import sys
from csv import reader

basket = []
lastuser = 'a'
for line in reader(sys.stdin):
    data = list(line)
    lineIndex = data[0]
    rowIndex = data[1]
    userid = data[2]
    productid = data[3]
    if userid == 'newdata.user_id':
        continue
    if userid != lastuser:
        if lastuser != 'a':
            for item in basket:
                print(item, end=",")
            print()
            basket = [userid, productid]
            lastuser = userid
        else:
            basket.append(userid)
            basket.append(productid)
            lastuser = userid
    else:
        basket.append(productid)
