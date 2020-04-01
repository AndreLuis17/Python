from random import choice
from tkinter import*
from functools import*
resp=''
valtot=0
val=0
pc=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
nai=['Copas','Paus','Ouros','Espadas']
janela=Tk()
def bt_press(Button):
    lb["text"]=val
    resp.write('S')

janela.geometry('200x200+100+100')

bt1= Button(janela, width=6, height=6, text='HIT')
bt1.grid(row=0, column=0)
bt1["command"]=partial(bt_press,bt1)

lb= Label(janela)
lb.grid(row=2,column=3)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
for c in range(1,2):
    while True:
        resp=str(input('Quer puxar umar carta?[S/N]')).upper().strip()[0]
        if resp=='S':
            num=choice(pc)
            naipe=choice(nai)
            for i,v in enumerate(pc):
                if v==num:
                    val=i+1
            if val>10:
                val=10
            valtot=valtot+val
            print(f'Você recebeu a carta {num} de {naipe} seu total é:{valtot}')
            if valtot==21:
                print('Você é topper')
                break
            if valtot>21:
                print('Você perdeu bocó')
                break
            else:
                if valtot>21:
                    valtot=21-(valtot-21)
                elif valtot<21:
                    valtot=valtot

                print(f'A pontuação do jogador {c} foi:{valtot}')
                break