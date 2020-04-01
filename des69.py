i18=0
man=0
wom18=0
while True:
    i=int(input('Qual a Idade?'))
    s=str(input('Qual o Sexo?[M/F]')).upper().strip()[0]
    resp=(input('Quer continuar?[S/N]')).upper().strip()[0]
    if i>=18:
        i18+=1
    if s=='M':
        man+=1
    if s=='F' and i<20:
        wom18+=1
    if resp!='S':
        break
print(f'{i18} pessoas tem mais de 18 anos')
print(f'{man} pessoas são homens')
print(f'{wom18} pessoas são mulheres com menos de 20 anos')