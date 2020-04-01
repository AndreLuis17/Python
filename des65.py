n=0
nd=0
vez=0
lista=[]
resp='S'
while resp=='S':
    nd=float(input('Digite um número:'))
    n=n+nd
    resp=str(input('Quer continuar?[S/N]')).upper().strip()[0]
    lista.insert(0,nd)
    vez+=1
maior=max(lista)
menor=min(lista)
print(f'A média entre os numeros é: {n/vez}, o maior é {maior} e o menor é {menor}')