dis=int(input('Qual a distancia da sua viagem?'))
if dis<=200:
    print('O preço de sua passagem será de:R${:.2f}'.format(dis*0.50))
else:
    print('O preço de sua passagem será de:R${:.2f}'.format(dis * 0.45))