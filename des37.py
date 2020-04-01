dec=int(input('Qual o número você deseja converter?'))
print(''''[1] Binário
 [2] Octal
 [3] Hexadecimal''')
base=int(input('Para qual base você deseja converter?'))
if base==1:
    print('{} convertido para binário é:{}'.format(dec,bin(dec)[2:]))
elif base==2:
    print('{} convertido para octal é:{}'.format(dec, oct(dec)[2:]))
elif base==3:
    print('{} convertido para hexadecimal é:{}'.format(dec, hex(dec)[2:]))
else:
    print('OPÇÃO INVALIDA!')
    