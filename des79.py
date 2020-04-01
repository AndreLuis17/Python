v=[]
val=0
resp=''
while True:
    val=float(input('Qual número deseja adicionar?'))
    if (val in v):
        print('O número ja foi adicionado antes.')
    else:
        v.append(val)
        print('O número foi adicionado com sucesso.')
    resp=str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    if (resp=='N'):
        break
v.sort
print(f'A lista de números sorteados é {v}')