vel=int(input('Qual a velocidade do carro?'))
if vel<=80:
    print('Você não foi multado.')
else:
    print('Você passou {}km/h acima do limite, sua multa é de:R${:.2f}'.format(vel-80, (vel-80)*7))