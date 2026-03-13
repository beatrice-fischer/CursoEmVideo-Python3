# EXERCÍCIO 35 - ler comprimento de 3 retas, dizer se podem ou não formar um triângulo

from time import sleep

r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))

print('-=-'*10)
print('Analisando ...')
sleep(3)

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos PODEM FORMAR um triângulo')
else:
    print('Os segmentos NÃO formam um triângulo')
