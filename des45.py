from random import choice
jog=int(input('[1]Pedra\n[2]Papel\n[3]Tesoura\nQual sua jogada?'))
comp=['Pedra', 'Papel', 'Tesoura']
jogcomp=choice(comp)
print('O computador jogou {}'.format(jogcomp))
if   jogcomp=='Pedra'and jog==2:
    print('Você ganhou')
elif jogcomp=='Pedra'and jog==3:
    print('Você perdeu')
elif jogcomp=='Papel'and jog==1:
    print('Você perdeu')
elif jogcomp=='Papel'and jog==3:
    print('Você ganhou')
elif jogcomp=='Tesoura'and jog==1:
    print('Você perdeu')
elif jogcomp=='Tesoura'and jog==2:
    print('Você ganhou')
elif jogcomp==('Pedra'and jog==1)or(jogcomp=='Papel'and jog==2)or(jogcomp=='Tesoura'and jog==3):
    print('Empate')
else:
    print('Opção invalida!')