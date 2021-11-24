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
      codons[gene] = re.findall(r"(.{3})",seqs[gene])
  for gene in codons:
    print(gene+'-frame-1-codons')
    for codon in codons[gene]:
      print(codon, end=' ')
    print()
