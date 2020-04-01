t=int(input('Digite o primeiro termo:'))
r=int(input('Digite a razão:'))
c=0
ve=10
mais=1
while mais!=0:
    while c!=ve:
        print(r*c+t, end='')
        print('-'if c<ve-1 else'\n',end='')
        c+=1
    mais=int(input('Quer ver mais quantos termos da PA?'))
    ve=mais+ve
print(ve)