n1=float(input('Digite o primeiro valor:'))
n2=float(input('Digite o segundo valor:'))
fun=0
while not fun==5:
    fun=int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa'))
    if fun==1:
        som=n1+n2
        print('A soma entre {} e {} é igual a {}'.format(n1,n2,som))
    if fun==2:
        mult=n1*n2
        print('A multiplicação entre {} e {} é igual a {}'.format(n1,n2,mult))
    if fun==3:
        if n1>n2:
            print('O maior número entre {} e {} é {}'.format(n1,n2,n1))
        elif n1<n2:
            print('O maior número entre {} e {} é {}'.format(n1,n2,n2))
        else:
            print('Os dois números são iguais')
    if fun==4:
        n1=float(input('Digite um números:'))
        n2=float(input('Digite outro números:'))