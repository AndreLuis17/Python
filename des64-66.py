n=0
nd=0
while True:
    nd=int(input('Digite um número:'))
    if nd==999:
        break
    n=n+nd
print('A soma entre os numeros digitados é: {}'.format(n))