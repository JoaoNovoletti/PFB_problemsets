#!/usr/bin/env python3

myList=[101,2,15,22,95,33,2,27,72,15,52]

somaPares=0
somaImpares=0

for numero in myList:
 if numero % 2 == 0:
  somaPares+=numero
 else:
  somaImpares+=numero

print(f'Sum of even numbers: {somaPares}\nSum of odds: {somaImpares}')
