#!usr/bin/env python3

import re

seqs={}
seqs_qtd_nt={}
arquivo = input('Arquivo fasta: ')

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
      print(seqs[gene])

  for gene in seqs.keys():
    if gene not in seqs_qtd_nt.keys():
      seqs_qtd_nt[gene] = {}
    for nt in set(seqs[gene]):
      seqs_qtd_nt[gene][nt] = seqs[gene].count(nt)
   
    print(gene,'\t',seqs_qtd_nt[gene]['A'],'\t',seqs_qtd_nt[gene]['T'],'\t',seqs_qtd_nt[gene]['G'],'\t',seqs_qtd_nt[gene]['C'])
