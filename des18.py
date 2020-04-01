import math
a=float(input('Digite o angulo que você deseja:'))
r=math.radians(a)
s=math.sin(r)
c=math.cos(r)
t=math.tan(r)
print('O ângulo de {}° tem o SENO de {:.2f}'.format(a,s))
print('O ângulo de {}° tem o COSENO de {:.2f}'.format(a,c))
print('O ângulo de {}° tem a TANGENTE de {:.2f}'.format(a,t))
