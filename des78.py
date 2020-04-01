num=[]
mai=0
men=0
for c in range(0,5):
    val=int(input('Digite um valor:'))
    num.append(val)
    if c==0:
        mai=men=val
    else:
        if val>mai:
            mai=val
        if val<men:
            men=val
print(f'Os numeros digitados foram {num}')
print(f'O maior valor é {mai} na posição ',end='')
for i,v in enumerate(num):
    if v==mai:
        print(f'{i+1}...',end='')
print(f'\nO menor valor foi {men} na posição ',end='')
for i,v in enumerate(num):
    if v==men:
        print(f'{i+1}...',end='')