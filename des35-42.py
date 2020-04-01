r1=float(input('Valor da reta 1:'))
r2=float(input('Valor da reta 2:'))
r3=float(input('Valor da reta 3:'))
if r1>(r2-r3) and r1<(r2+r3):
    print('Pode formar um triangulo.')
    if r1==r2 and r1==r3:
        print('Triangulo Equilátero.')
    elif (r1==r2 and r1!=r3)or(r1==r3 and r1!=r2)or(r2==r3 and r2!=r1):
        print('Triangulo Isosceles.')
    elif (r1!=r2)and(r2!=r3)and(r1!=r2):
        print('Triangulo escaleno.')
else:
    print('Não pode formar um triangulo.')