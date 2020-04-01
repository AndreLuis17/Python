ma=0
me=0
for c in range(0,7):
    i=int(input('Digite a idade:'))
    if i>=18:
        ma=ma+1
    else:
        me=me+1
print('{} deles são maiores de idade e {} são menores.'.format(ma,me))