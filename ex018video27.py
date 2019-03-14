import math
an=float(input('Digite o ângulo que você deseja: '))
se=math.sin(math.radians(an))
co=math.cos(math.radians(an))
ta=math.tan(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}\nO ângulo de {} tem o COSSENO de {:.2f}\nO ângulo de {} tem a TANGENTE de {:.2f}'.format(an,se,an,co,an,ta))

