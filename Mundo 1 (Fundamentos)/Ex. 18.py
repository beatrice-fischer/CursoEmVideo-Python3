# EXERCÍCIO 18 - ler ângulo, mostrar seno, cosseno e tangente

import math

a = float(input("Digite um ângulo: ")) #ângulo centígrado, transformar para radianos
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print('O ângulo {} tem seno {}; cosseno {} e tangente {}'.format(a,sen,cos,tan))
