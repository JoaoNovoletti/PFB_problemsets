#!usr/bin/env python3

import re

#Abrindo os dicionários e pegando o arquivo da entrada do usuário.
seqs={}
seqs_qtd_nt={}
arquivo = input('Arquivo fasta: ')

#Abrindo arquivo, armazenando-o nos dicionário abertos  e imprimindo-o
with open(arquivo, "r") as R_arquivo:
  for line in R_arquivo:
    line = line.rstrip()
  
    if line[0] == '>':
   
     #Reconhecendo o gene e armazenando seu nome
     achandogene = re.search(r">(\w+)\s", line)
     gene = (achandogene.group(1))

     if gene not in seqs.keys():
       seqs[gene]=''

    else:
      seqs[gene] += line
  
  #Montando um dicionário com a contagem dos nt
  for gene in seqs.keys():
    if gene not in seqs_qtd_nt.keys():
      seqs_qtd_nt[gene] = {}
    for nt in set(seqs[gene]):
      seqs_qtd_nt[gene][nt] = seqs[gene].count(nt)
   
    #Linha abaixo imprime o arquivo da sequinte forma: seqName\tA_count\tT_count\tG_count\C_count
    print(gene,'\t',seqs_qtd_nt[gene]['A'],'\t',seqs_qtd_nt[gene]['T'],'\t',seqs_qtd_nt[gene]['G'],'\t',seqs_qtd_nt[gene]['C'])
