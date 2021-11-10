#!usr/bin/env python3

sequences=[]
seq = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for nt in seq:
 LenandSeq = (len(nt), nt)
 sequences.append(LenandSeq)

print(sequences)

 
