nome=str(input('Qual seu nome completo?'))
print('Seu nome com todas em maiusculas fica:{}'.format(nome.upper()))
print('Seu nome com todas em minusculas fica:{}'.format(nome.lower()))
nospace=''.join(nome.split())
print('Seu nome tem {} letras.'.format(len(nospace)))
stnome=nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(stnome[0])))
