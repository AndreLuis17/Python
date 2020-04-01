num=int(input('Digite um numero:'))
m=num//1000
c=(num%1000)//100
d=(num%1000)%100//10
u=((num%1000)%100)%10//1
print('Unidade:{} \nDezena:{} \nCentena:{} \nMilhar:{}'.format(u, d, c, m))