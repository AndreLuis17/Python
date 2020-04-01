n=int(input('Digite o numero de elementos que você deseja ver na sequencia de Fibonacci:'))
v=2
t1=0
t2=1
t3=0
print('{}-{}'.format(t1,t2),end='')
while n!=v:
    t3=t1+t2
    print('-{}'.format(t3)if v<=n else'' ,end='')
    t1=t2
    t2=t3
    v+=1