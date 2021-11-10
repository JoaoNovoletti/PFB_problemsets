#!usr/bin/env python3

seq = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

lugar = 1
for nt in seq:
 print(lugar, "\t", len(nt),"\t", nt)
 lugar+=1
 
