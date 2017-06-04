# -*- coding: utf-8 -*-
"""
Output: dictionary of all concepts, each with a set of subconcepts. 
"""
import pickle
import os
os.chdir('/Users/zhiwei/Google Drive/Knowledge_Base/ConceptGraph')



allc={} # all concepts stored in a dictionary
allc_p={} # all concepts and their parent nodes
# only include relations with occurence > 10 -- look like reasonable relations.
newf='data/short-concept-instance-relations.txt'
nrela=0;
with open(newf, 'w') as file_short, open('data/data-concept-instance-relations.txt', 'r') as file_ori:
    for line in file_ori:
        data=line.split('\t') 
        if int(data[2])<10:
            break
        #file_short.write(line)
        nrela=nrela+1
        supc = data[0] 
        subc = data[1]
        if supc in allc:
           allc[supc].add(subc)
        else:
           allc[supc]={subc}
        if subc in allc_p:
            allc_p[subc].add(supc)
        else:
            allc_p[subc]={supc}


with open('allconcept.pkl', 'wb') as dictfile:
    pickle.dump([allc,allc_p], dictfile)
