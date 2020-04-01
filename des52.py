d=0
n=int(input('Digite o número que você quer analisar:'))
for c in range (1,n+1):
    if n%c==0:
        d=d+1
    if d>3:
        print('Número composto')
        break
    else:
        print('Número primo')