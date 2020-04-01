casa=int(input('Digite o preço da casa:'))
sal=int(input('Digite o seu salario:'))
ano=int(input('Digite em quantos anos irá pagar:'))
prest= casa/(ano*12)
porc= (sal/100)*30
if prest>porc:
    print("Desculpe, você não podera fazer o emprestimo :(")
else:
    print('Você podera fazer o emprestimo')