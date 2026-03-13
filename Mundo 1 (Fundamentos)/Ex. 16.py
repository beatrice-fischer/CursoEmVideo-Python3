# EXERCÍCIO 16 - ler número real, mostrar porção inteira

from math import trunc

n = float(input('Digite um número real: '))

print('A porção real é {} e a porção inteira é {}'.format(n,trunc(n)))
print('A porção real é {} e a porção inteira é {}'.format(n,int(n)))
