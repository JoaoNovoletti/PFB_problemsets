import sys
anotest = int(sys.argv[1])
print ("Ano sendo testado: "+ sys.argv[1])

if anotest%4 == 0:
    if not anotest%100 == 0:
        print("O ano é bissexto (leap year)")
    elif anotest %400 == 0:
        print("O ano é bissexto (leap year)")
else:
    print ("O ano não é bissexto (leap year)")

