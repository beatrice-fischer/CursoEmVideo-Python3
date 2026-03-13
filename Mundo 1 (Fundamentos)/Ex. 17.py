# EXERCÍCIO 17 - ler comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o cumprimento da hipotenusa

import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = math.hypot(co, ca)
#hip = ((co*co) + (ca*ca))**(1/2)

print(hip)
