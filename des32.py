ano=int(input('Digite o ano:'))
if ano%4==0:
    print('{} é ano bissexto.'.format(ano))
else:
    print('{} não é ano bissexto.'.format(ano))