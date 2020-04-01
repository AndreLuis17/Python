n1=float(input('Digite a nota 1:'))
n2=float(input('Digite a nota 2:'))
m=(n1+n2)/2
if m<5:
    print('Reprovado')
elif m>=7:
    print('Aprovado')
else:
    print('Recuperação')