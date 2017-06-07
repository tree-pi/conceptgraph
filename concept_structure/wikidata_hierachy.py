#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test hypo0: is number of instances clustered? (If there's hierachy, may cluster)
[alternative: some thick tail distribution]
test hypo1: level of hierachy is corelated with number of instances.
[alternative: different disciplines matters; also, data source matters -- if you count the instance of wikidata/schema.org itself!]
test hypo2: there's an optimal amount of instances for a concept to be "easy to grasp"
[first, need behavioral tests to show some concepts are "easy to grasp" (eg: learn a new concept, what's the adequate level of explanation)? Then, check the number of instances of those levels]

Created on Tue Jun  6 08:13:51 2017

@author: zhiwei
"""

import matplotlib.pyplot as plt
import pickle
import numpy as np

projdir='/Users/zhiwei/Google Drive/Knowledge_Base/conceptgraph/'
with open(projdir+'data_preprocess/allconcept.pkl', 'rb') as dictfile:
    [allc,allc_p]=pickle.load(dictfile)


n_subc = []
for key, value in allc.items():
    n_subc.append(len(value))

# test hypo0, see the distribution of number of child
"""
plt.hist(np.log10(n_subc),1500)
plt.xlabel("N subconcepts")
plt.ylabel("Frequency")
"""
# --conclusion: no cluster can be seen. may ask more strictly: how to model this distribution?

# test hypo1, select two hierachical levels from schema.org, compare their # of instances

level0 = ['product','event','place','organization','person'] # immediately under "item"
level1 = ['vehicle','festival','tourist attraction','company','patient'] # "more specific Types available in extensions" under level 0 Types

nsub_0 = []
nsup_0=[]
for c0 in level0:
    nsub_0.append(len(allc[c0]))
    nsup_0.append(len(allc_p[c0]))

nsub_1 = []
nsup_1=[]
for c1 in level1:
    nsub_1.append(len(allc[c1]))
    nsup_1.append(len(allc_p[c1]))
# hypothesis is kinda true, "company" as an exception -- very salient in our data set.
# => can test whether this is a natural phenomenon (not bc scrapping bias) by asking human subject to list instances under each category?
