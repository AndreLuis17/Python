i=0
mulh=0
maidh=0
maisvelho=''
for p in range(1,5):
    print('--- {}ª PESSOA---'.format(p))
    nome=str(input('Nome:'))
    idade=int(input('Idade:'))
    sexo=str(input('Sexo[M/F]:')).upper()
    i+=idade
    if p==1 and sexo=='M':
        maidh= idade
        maisvelho= nome
    if sexo=='M' and idade>maidh:
        maidh=idade
        maisvelho=nome
    if sexo=='F' and idade<20:
        mulh+=1
print('A média das idades é:{}'.format(i/4))
print('O homem mais velho é {} e tem {} anos.'.format(maisvelho,maidh))
print('{} mulheres tem menos de 20 anos.'.format(mulh))