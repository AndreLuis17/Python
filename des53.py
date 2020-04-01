frase=str(input('Digite a frase:'))
nospace=frase.split()
junto=''.join(nospace)
if junto==junto[::-1]:
    print('Palindromo')
else:
    print('Não palindromo')