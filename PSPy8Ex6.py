#!usr/bin/env python3

import re

seqs={}
codons={}
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
      
      codonsframe3.write(gene+'-'+frame+'-codons'+'\n'+frameseq+'\n')



seqscodons={}

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

with open("Python_08.codons-6frames.nt", "r") as R_arquivo:
  for line in R_arquivo:
    line = line.rstrip()
    codonfound = re.search(r"[ATCG][ATCG][ATCG]", line)
    achandogeneframe = re.search(r"(c\d\w+-\w+-\d)", line)
    if achandogeneframe:
      geneframe = (achandogeneframe.group(1))
      if geneframe not in seqscodons.keys():
       seqscodons[geneframe]=''
    elif codonfound:
       seqscodons[geneframe] += line

with open ("Python_08.translated.aa", "w") as traducao:
  for geneframe in seqscodons:
    line = seqscodons[geneframe]
    line = line.rstrip()
    codonslist = line.split(' ')
    translatedcodons = []
    for codon in codonslist:
      codonfound = re.search(r"[ATCG][ATCG][ATCG]", codon)
      if codonfound:
        translatedcodons.append(translation_table[codon])
    translatedlist = ''
    for codons in translatedcodons:
      translatedlist += codons
    
    traducao.write(geneframe + "-aa" + '\n' + translatedlist + '\n')


seqsAA = {}
seqsmaiorAA = {}

with open("Python_08.translated.aa", "r") as R_arquivo:
  for line in R_arquivo:
    line = line.rstrip()
    achandogeneAA = re.search(r"(c\d\w+)", line)
    if achandogeneAA:
      geneAA = (achandogeneAA.group(1))
      if geneAA not in seqsAA.keys():
       seqsAA[geneAA]=[]
    else:
       seqsAA[geneAA].append(line)

with open ("Python_08.translated-longest.aa", "w") as Tlongest:
  for genaa in seqsAA:
    maior = 0
    pepmaior = "pepitide not found in any frame"
    tamanho = 0
    for AAs in seqsAA[genaa]:
      for pep in re.finditer(r"(M\w*\*)", AAs):
        tamanho = len(pep.group(0))
        if tamanho > maior:
          maior = tamanho
          pepmaior = pep.group(0)
    
    Tlongest.write(genaa + "-longest_peptide" + '\n' + pepmaior + '\n')
