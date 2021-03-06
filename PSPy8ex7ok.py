#!usr/bin/env python3

#Importando os módulos necessários 
import re

seqs={}
codons={}
arquivo = input('Arquivo fasta: ')

#Abrind o arquivo e correspondendo o gene e a sequencia em um dicionário
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

#Montando um dicionário com os genes e seus 6 frames
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

#Escrevendo o arquivo Python_08.codons-6frames.nt a partir do dicionário códons
with open ("Python_08.codons-6frames.nt", "w") as codonsframe3:
  for gene in codons:
    for frame in codons[gene]:
      frameseq = ""
      for codon in codons[gene][frame]:
        frameseq += codon
        frameseq += ' '

      codonsframe3.write(gene+'-'+frame+'-codons'+'\n'+frameseq+'\n')

#Montando um dicionário com as traduções dos códons

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

#Abrindo o arquivo Python_08.codons-6frames.nt" novamente, dessa vez lendo e montando um dicionário (fiz esse passo pensando que pode ser destacado do código e modificado para usar em outro que não tenha os passos anteriores).
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

#Abrindo o arquivo Python_08.translated.aa e escrevendo nele a tradução dos códons
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


#Abrindo o arquivo Python_08.translated.aa e montando um duicionário com ele (fiz esse passo pensando que pode ser destacado do código e modificado para usar em outro que não tenha os passos anteriores).

seqsAA = {}

with open("Python_08.translated.aa", "r") as R_arquivo:
  for line in R_arquivo:
    line = line.rstrip()
    achandogeneAA = re.search(r"(c\d\w+)-(\w+-\d)", line)
    if achandogeneAA:
      geneAA = (achandogeneAA.group(1))
      geneframeAA = (achandogeneAA.group(0))
      if geneAA not in seqsAA.keys():
        seqsAA[geneAA]={}
      if geneframeAA not in seqsAA[geneAA].keys():
        seqsAA[geneAA][geneframeAA] = ""
    else:
       seqsAA[geneAA][geneframeAA] += line

dadospepmaior = {}

#Abrindo o arquivo Python_08.translated-longest.aa para a identificação do maior pepitideo em relação a todos os frames e escrevendo.
#Nesse caso ele armazena também os dados do maior peptídeo, nome, começo e fim em um dicionário’
with open ("Python_08.translated-longest.aa", "w") as Tlongest:
  for genaa in seqsAA:
    maior = 0
    pepmaior = "pepitide not found in any frame"
    tamanho = 0
    sequencia = ""
    for AAs in seqsAA[genaa]:
      for pep in re.finditer(r"(M\w*\*)", seqsAA[genaa][AAs]):
        tamanho = len(pep.group(0))
        if tamanho > maior:
          maior = tamanho
          pepmaior = pep.group(0)
          sequencia = AAs
          inicio = pep.start(0)
          fim = pep.end(0)

    Tlongest.write(genaa + "-longest_peptide" + '\n' + pepmaior + '\n')
    if sequencia != "":
      dadospepmaior[sequencia] = []
      dadospepmaior[sequencia].append(inicio)
      dadospepmaior[sequencia].append(fim)

#Abrindo novamente o Python_08.codons-6frames.nt e armazenando os dados, para não haver erros nas variáveis    
seqscodons = {}
with open ("Python_08.codons-6frames.nt", "r") as SeqCodonsframe:
  for line in SeqCodonsframe:
    line = line.rstrip()
    codonfound = re.search(r"[ATCG][ATCG][ATCG]", line)
    achandogeneframe = re.search(r"(c\d\w+-\w+-\d)", line)
    if achandogeneframe:
      geneframe = (achandogeneframe.group(1))
      if geneframe not in seqscodons.keys():
       seqscodons[geneframe]=''
    elif codonfound:
       seqscodons[geneframe] += line

#Abrindo o arquivo Python_08.orf-longest.nt e escrevendo nele o orf baseado na localização dele na sequencia de AAs do qual o maior pepitideo deriva.
with open("Python_08.orf-longest.nt", "w") as LpepCodons:
  for seqspep in dadospepmaior:
    for frame in seqscodons:
      for pepframe in re.finditer(rf"{seqspep}", frame):
        correctsequence = seqscodons[frame]
        seqinicio = dadospepmaior[seqspep][0]*4
        seqfim = dadospepmaior[seqspep][1]*4
        subsequence = correctsequence[seqinicio:seqfim]

    fnomedogene = re.search(r"(c\d\w+)", seqspep)
    nomedogene = fnomedogene.group(0)
    LpepCodons.write(nomedogene + "-orf-longest_peptide" + '\n' + subsequence + '\n')

