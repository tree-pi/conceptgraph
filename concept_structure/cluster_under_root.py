#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 10:37:41 2017

@author: zhiwei
hypothesis: find "subcategories" of a concept by clustering its subconcepts' other supconcepts
"""
import matplotlib.pyplot as plt
import pickle
from collections import Counter

projdir='/Users/zhiwei/Google Drive/Knowledge_Base/conceptgraph/'
with open(projdir+'data_preprocess/allconcept.pkl', 'rb') as dictfile:
    [allc,allc_p]=pickle.load(dictfile)
    
arrrootc =['person','event','plant','animal','food']

with open('sub_categ.txt','w') as oupf:    
    for rootc in arrrootc:
        subcls = allc[rootc]
        allsupc = []
        for subc in subcls:
            allsupc=allsupc+list(allc_p[subc])
   
        # remove supconcepts of the "rootc" 
        temp = allsupc
        for supc in allsupc:
            if supc in allc_p[rootc] or supc == rootc:
                temp.remove(supc)
        allsupc=temp
        countsup=Counter(allsupc)
        
        oupf.write('\nroot concept: '+rootc+'\n')
        oupf.write(str(countsup.most_common(20))+'\n')
        
        """
        problem: just counting can generate parallel concepts (eg. event - activity) of root concept
        You are not "clustering", which means be able to distinguish subconcepts into smaller sets.
        
        If wanna "cluster", need to find a group of concepts whose subconcepts cover most concepts yet don't overlap with each other
        There might be different groups, representing different dimensions to organize subconcepts
        
        Interesting observation: unlike naturalists, here the "subcategories" are much 
        more practical -- like "cash crop" and "topping" are top hits for "plant"!
        """
        
        #specificity index: highest if all the subconcepts are in this group. 
        # purpose: rule out too general concepts -- but not true. like, s-index of "artist" / "writer" is very low...
            # but "worker" is pretty high, intuitively bc it's more abstract than "artist"...
            #purpose 2: to diagnosis how abstract is a concept!
            #purpose 3: indicates gap in knowledge? should be able to infer that a specific artist is a person...
"""
        for supc in allsupc:
            spcf_idx = countsup.get(supc)/len(allc[supc]) 

"""
            # this part, no conclusion yet
