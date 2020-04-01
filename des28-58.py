import random
n=int(random.randint(0,10))
c=int(input('Digite um número de 0 a 10:'))
e=0
while c!=n:
    e+=1
    c=int(input('Você errou digite outro:'))
print('Você precisou de {} tentativas'.format(e))
