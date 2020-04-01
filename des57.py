sex=str(input('Digite o sexo (F/M):')).upper().strip()[0]
while not(sex=='F' or sex=='M'):
    sex=str(input('Valor invalido, digite seu sexo:')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(sex))