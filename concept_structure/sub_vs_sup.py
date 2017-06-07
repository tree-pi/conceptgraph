#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 08:49:51 2017

@author: zhiwei

hypothesis: more concrete concepts will have less subconcepts, yet more superconcepts? (i.e. more ways to describe them? -- graph not tree)
"""

import matplotlib.pyplot as plt
import pickle
import numpy as np

projdir='/Users/zhiwei/Google Drive/Knowledge_Base/conceptgraph/'
with open(projdir+'data_preprocess/allconcept.pkl', 'rb') as dictfile:
    [allc,allc_p]=pickle.load(dictfile)


n_subc = []
n_supc = []
for key,subvalue in allc.items():
    if key in allc_p:
        n_subc.append(len(subvalue))
        n_supc.append(len(allc_p[key]))

plt.plot(np.log10(n_subc), np.log10(n_supc),'r.')

# conclusion: seems actually positively correlated...but it's also because of the weird definition of "sup concepts".