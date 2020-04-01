from math import hypot
ca=float(input('Qual o valor do Cateto A?'))
cb=float(input('Qual o valor do Cateto B?'))
h=hypot(ca,cb)
print('O valor da hipotenusa é:{:.2f}'.format(h))