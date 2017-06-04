# -*- coding: utf-8 -*-
"""
Basic functions for reading concept structure
"""
import os
os.chdir('/Users/zhiwei/Google Drive/Knowledge_Base/ConceptGraph')

d = []
newf='data/short-concept-instance-relations.txt'
nrela=0;
with open(newf, 'w') as file_short, open('data/data-concept-instance-relations.txt', 'r') as file_ori:
    for line in file_ori:
        if int(line.split('\t')[2])<10:
            break
        file_short.write(line)
        nrela=nrela+1;

"""
with open(,'rb') as f:
    for line in f:
        rela = line.split()
        if rela[2]<4: # don't include 
            break
        
        d.append(fields)
"""
