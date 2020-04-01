sal=float(input('Digite o seu salario:'))
if sal<=1250:
    print('Seu novo salário será de:{:.2f}'.format((sal/100)*115))
else:
    print('Seu novo salário será de:{:.2f}'.format((sal/100)*110))