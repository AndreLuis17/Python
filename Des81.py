lista=[]
while True:
    lista.append(input('Digite um número:'))
    resp=str(input('Você quer continuar?[S/N]')).upper().strip()[0]
    if resp=='N':
        break
print('Foram digitados {} números.'.format(len(lista)))
print('A lista de forma decrescente é {}'.format(lista.reverse()))
if 5 in lista:
    print('A lista contém o número 5.')
else:
    print('A lista não contém o número 5.')