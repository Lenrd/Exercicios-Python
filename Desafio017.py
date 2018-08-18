# comprimento da hipotenusa
from math import hypot

a = float(input('Cateto oposto: '))
b = float(input('Cateto adjacente: '))
c = hypot(a, b)
print('A soma dos quadrados dos catetos é: {}'.format(c))
