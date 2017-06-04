#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 10:58:33 2017

@author: zhiwei
what concepts contains most parent concepts? no intuition what does that mean....
"""
import matplotlib.pyplot as plt
import pickle


with open('allconcept.pkl', 'rb') as dictfile:
    [allc,allc_p]=pickle.load(dictfile)

n_supc = []
for key, value in allc_p.items():
    n_supc.append(len(value))

thres=20
large_nsupc=[x for x in n_supc if x>thres]
plt.hist(large_nsupc)
plt.title("concepts with more than %d parents: %d"%(thres,len(large_nsupc)))
plt.xlabel("N supconcepts")
plt.ylabel("Frequency")


thres=100
d_rootC={}
for key, value in allc_p.items():
    if len(value)>thres:
        d_rootC[key]=len(value)

