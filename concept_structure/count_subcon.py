#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 10:58:33 2017

@author: zhiwei
"""
import matplotlib.pyplot as plt
import pickle
import collections

with open('data_preprocess/allconcept.pkl', 'rb') as dictfile:
    [allc,allc_p]=pickle.load(dictfile)
"""
n_subc = []
for key, value in allc.items():
    n_subc.append(len(value))

thres=1000
large_nsubc=[x for x in n_subc if x>thres]
plt.hist(large_nsubc,100)
plt.title("concepts with more than %d children: %d"%(thres,len(large_nsubc)))
plt.xlabel("N subconcepts")
plt.ylabel("Frequency")
"""

thres=1000
d_rootC={}
for key, value in allc.items():
    if len(value)>thres:
        d_rootC[key]=len(value)


with open('rootConcepts.txt','w') as oupf:
    for w in sorted(d_rootC, key=d_rootC.get, reverse=True):
        oupf.write(w+'\t'+str(d_rootC[w])+'\n')