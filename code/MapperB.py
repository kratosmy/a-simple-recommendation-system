#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import itertools
support = 20
basket = {}
for line in sys.stdin:
    temp = line.strip()
    data = temp.split(',')
    #find which basket an item is in, index is item, value is baskets that the item is in
    for item in list(set(data[1:])):   #this is to find the unique values in a basket
        try:
            basket[item].append(data[0])   #data[0] is the user id
        except:
            basket[item] = [data[0]]
            
frequent1 = {}         #this is the frequent itemset size 1
#find frequent itemset size 1
for key, value in basket.items():
    if len(basket[key]) >= support:
        frequent1[key] = value
    else:
        continue
            
frequent2 = {}     #this is for frequent itemset size 2
#find frequent itemset size 2
for k1, k2 in itertools.combinations(frequent1, 2):
    if len(list(set(frequent1[k1]) & set(frequent1[k2]))) >= support:    #check intersection length
        frequent2[k1+','+k2] = len(list(set(frequent1[k1]) & set(frequent1[k2])))

for key, values in frequent2.items():
    print(key + ":" + str(values))

