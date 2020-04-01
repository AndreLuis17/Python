import random
pc=random.randint(0,10)
v=0
while True:
    num = int(input('Digite o número:'))
    parimpar = str(input('Par ou Impar:[P/I]')).upper().strip()[0]
    if (num+pc)%2==0 and parimpar=='P':
        print(f'Você jogou {num} e o computador {pc}. Total= {pc+num} Deu PAR')
        print('Você Ganhou!')
        v+=1
    if (num+pc)%2==0 and parimpar=='I':
        print(f'Você jogou {num} e o computador {pc}. Total= {pc+num} Deu PAR')
        print('Você Perdeu!')
        break
    if (num+pc)%2!=0 and parimpar=='P':
        print(f'Você jogou {num} e o computador {pc}. Total= {pc+num} Deu IMPAR')
        print('Você Perdeu!')
        break
    if (num+pc)%2!=0 and parimpar=='I':
        print(f'Você jogou {num} e o computador {pc}. Total= {pc+num} Deu IMPAR')
        print('Você Ganhou!')
        v+=1
print(f'Você ganhou {v} vezes!')