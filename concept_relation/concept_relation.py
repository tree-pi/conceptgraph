#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 15:19:15 2017

@author: zhiwei
"""
import matplotlib.pyplot as plt
import pickle


with open('allconcept.pkl', 'rb') as dictfile:
    [allc,allc_p]=pickle.load(dictfile)


# idea 1: are two concepts at the same level? if their parents overlap a lot
selectc={}
for key, value in allc_p.items():
    if len(value)>20:
       selectc[key] =value
 
"""      # see the distribution of intersection ratio: 0.2 seems a reasonable threshold
intsratio=[]       
for key1,value1 in selectc.items():
    for key0,value0 in selectc.items():
        a=len(value0.intersection(value1))/len(value0.union(value1))
       # print(a)
        intsratio.append(a)        
plt.hist([x for x in intsratio if x > 0.2])
plt.xlabel("intersection ratio")
plt.ylabel("Frequency")
"""

thres=0.3
pairs = []
listsc=list(selectc.keys())
for k1 in range(len(listsc)):
    for k0 in range(k1+1,len(listsc)):
        value0=selectc[listsc[k0]]
        value1=selectc[listsc[k1]]
        a=len(value0.intersection(value1))/len(value0.union(value1))  
        if a>thres:
            thispr = [listsc[k1],listsc[k0],a]
            pairs.append(thispr)

pairs.sort(key=lambda pairs:pairs[0])

with open('concept_relation/same_level.txt','w') as oupf:
    for thispr in pairs:
        oupf.write(thispr[0]+'\t'+thispr[1]+'\t'+str(thispr[2])+'\n')

# idea 1.1: can you identify what exactly are the common parent concept of them?


# idea 2: is one concept a sub concept of another? 
