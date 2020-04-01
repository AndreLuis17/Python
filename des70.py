total=0
mais100=0
nome=''
produto= str(input('Produto:'))
preço =float(input('Digite o preço:'))
menorp=preço
while True:
    resp = str(input('Quer adicionar mais produtos?')).upper().strip()[0]
    if resp=='N':
        break
    produto= str(input('Produto:'))
    preço =float(input('Digite o preço:'))
    total+=preço
    if preço>100:
        mais100+=1
    if preço<=menorp:
        menorp=preço
        nome=produto

print(f'O preço total é {total}')
print(f'{mais100} produtos custaram mais de 100 reais')
print(f'O produto mais barato é "{nome}" e ele custa: {menorp} reais.')