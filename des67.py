tab=int(input('Quer ver a tabuada de qual número?'))
while True:
    if tab<0:
        break
    for c in range(1,11):
        print(f'{tab}x{c}={tab*c}')
    tab=int(input('Quer ver a tabuada de qual outro número?'))
print('Tabela finalizada')