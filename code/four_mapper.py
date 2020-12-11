#!/usr/bin/env python3
# coding: utf-8

# In[ ]:


import sys
import itertools

support = 20
basket = {}
for line in sys.stdin:
    temp = line.strip()
    data = temp.split(',')
    # find which basket an item is in, index is item, value is baskets that the item is in
    for item in list(set(data[1:])):  # this is to find the unique values in a basket
        try:
            basket[item].append(data[0])  # data[0] is the user id
        except:
            basket[item] = [data[0]]

frequent2 = set()  # this is the single frequent items in frequent item pairs
# create a frequent item set
with open("output_pairs.txt") as f:
    for line in f.readlines():
        line = line.strip().split(":")
        frequent_itempair = line[0].split(",")
        item1 = frequent_itempair[0]
        item2 = frequent_itempair[1].strip()
        frequent2.add(item1)
        frequent2.add(item2)

# create a dictionary to store item-count pairs
frequent2_dic = {}
for item in frequent2:
    if item in basket.keys():
        frequent2_dic[item] = basket[item]
    
frequent4 = {}  # this is for frequent item-set size 4
# find frequent item-set size 4
for k1, k2, k3, k4 in itertools.combinations(frequent2_dic, 4):
    if len(list(set(frequent2_dic[k1]) & set(frequent2_dic[k2]) & set(frequent2_dic[k3])& set(frequent2_dic[k4]))) >= support:  # check intersection length
        frequent4[k1 + ',' + k2 + ',' + k3 + ',' + k4] = len(list(set(frequent2_dic[k1]) & set(frequent2_dic[k2]) & set(frequent2_dic[k3])& set(frequent2_dic[k4])))

for key, values in frequent4.items():
    print(key + ":" + str(values))

