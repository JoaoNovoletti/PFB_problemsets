#!usr/bin/env python3

import re

seqs={}
codons={}
arquivo = input('Arquivo fasta: ')
print(arquivo, '\n')

with open(arquivo, "r") as R_arquivo:
  for line in R_arquivo:
    line = line.rstrip()
  
    if line[0] == '>':
   
     achandogene = re.search(r">(\w+)\s", line)
     gene = (achandogene.group(1))

     if gene not in seqs.keys():
       seqs[gene]=''

    else:
      seqs[gene] += line

for gene in seqs.keys():
  if gene not in codons.keys():
    codons[gene]={}
for gene in codons:
  codons[gene]["frame-1"] = re.findall(r"(.{3})",seqs[gene])
  codons[gene]["frame-2"] = re.findall(r"(.{3})",seqs[gene][1:])
  codons[gene]["frame-3"] = re.findall(r"(.{3})",seqs[gene][2:])
  codons[gene]["frame-4"] = re.findall(r"(.{3})",seqs[gene][::-1])
  codons[gene]["frame-5"] = re.findall(r"(.{3})",seqs[gene][-2::-1])
  codons[gene]["frame-6"] = re.findall(r"(.{3})",seqs[gene][-3::-1])
  
with open ("Python_08.codons-6frames.nt", "w") as codonsframe3:
  for gene in codons:
    for frame in codons[gene]:
      frameseq = ""
      for codon in codons[gene][frame]:
        frameseq += codon
        frameseq += ' '
      print(gene+'-'+frame+'-codons'+'\n'+frameseq)
      codonsframe3.write(gene+'-'+frame+'-codons'+'\n'+frameseq+'\n')
