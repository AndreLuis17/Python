ma=0
me=0
peso=[]
for c in range(0,5):
    p=int(input('Digite o peso:'))
    peso.insert(0,p)
print('Menor peso:{}\nMaior peso:{}'.format(min(peso),max(peso)))