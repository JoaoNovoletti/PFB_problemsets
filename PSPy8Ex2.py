#!usr/bin/env python3

#Importando modulo re
import re

#Abrindo os dicionários e pegando o arquivo da entrada do usuário.
seqs={}
codons={}
arquivo = input('Arquivo fasta: ')
print(arquivo, '\n')

#Abrindo arquivo, lendo e armazenando nos dicionário abertos
with open(arquivo, "r") as R_arquivo:
  for line in R_arquivo:
    line = line.rstrip()
  
    #identificando padrão de início para leitura do nome do gene
    if line[0] == '>':
     
     #Reconhecendo o gene e armazenando seu nome
     achandogene = re.search(r">(\w+)\s", line)
     gene = (achandogene.group(1))

     if gene not in seqs.keys():
       seqs[gene]=''

    else:
      seqs[gene] += line

  #Para cada sequencia, o código abaixo divide os nt em códons
  for gene in seqs.keys():
    if gene not in codons.keys():
      codons[gene] = re.findall(r"(.{3})",seqs[gene])
  for gene in codons:
    print(gene+'-frame-1-codons')
    for codon in codons[gene]:
      print(codon, end=' ')
    print()

#Nesse caso, o exercício pede para armazenar o output em um arquivo 'Python_08.codons-frame-1.nt'. Isso foi feito, porém exteriormente ao python com o Redirect command ">".
#Nos próximos exercícios foi utilizada outra estratégia.
