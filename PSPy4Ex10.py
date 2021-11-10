#!usr/bin/env python3

import sys

inicio = int(sys.argv[1])
fim = int(sys.argv[2]) + 1

numeros = [number for number in range (inicio,fim)if number % 2 != 0]
print(numeros)
