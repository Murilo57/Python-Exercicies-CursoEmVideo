#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

#Primeira forma de fazer sem biblioteca math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacence: '))
hi = (co** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

#Segunda forma de fazer com biblitoteca math
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjance: '))
hi = hypot(co, ca)
print('A hipotenusa deve medir: {:.2f}'.format(hi))