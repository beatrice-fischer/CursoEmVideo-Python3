# EXERCÍCIO 28 - número aleatório de 0 a 5, o usuário tenta descobrir qual foi o número. Usuário venceu ou perdeu?

from time import sleep
import random

num = random.randint(0, 5)

print('-=-'*18)
print('Vou pensar num número entre 0 e 5. Tente adivinhar...')
print('-=-'*18)

usuario = input('Escolha um número entre 0 e 5: ')
print('Processando ...')
sleep(3)

if num == usuario:
    print('PARABÉNS, você acertou!')
else:
    print('Tente novamente. Eu pensei no número {}'.format(num))
