numteste = 50

if numteste > 0:
    print('positive')
    if numteste < 50:
        if numteste%2 == 0:
            print("it is an even number that is smaller than 50")
    elif numteste >50:
       if numteste%3 == 0:
           print("it is larger than 50 and divisible by 3")
elif numteste == 0:
    print('é igual a zero')
else:
    print ('negative')

