valor=int(input('DIGITE O VALOR A SER SACADO:'))
nota50=valor//50
nota20=(valor%50)//20
nota10=((valor%50)%20)//10
nota1 =((valor%50)%20)%10
print(f'{nota50} notas de 50 reais')
print(f'{nota20} notas de 20 reais')
print(f'{nota10} notas de 10 reais')
print(f'{nota1} notas de 1 reais')