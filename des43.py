import time
val=int(input('Digite o valor do produto:'))
print('''[1]A vista(-10%)
[2]A vista no cartão(-5%)
[3]Até 2 vezes no cartão
[4]3 vezes ou mais no cartão''''')
time.sleep(2)
opc=int(input('Qual opção de pagamento você deseja?'))
if opc==1:
    print('O valor a ser pago será R${:.2f}'.format(val/100*90))
elif opc==2:
    print('O valor a ser pago será R${:.2f}'.format(val/100*95))
elif opc==3:
    print('O valor a ser pago será R${:.2f}'.format(val))
elif opc==4:
    print('O valor a ser pago será R${:.2f}'.format(val/100*120))
else:
    print('OPÇÃO INVALIDA')