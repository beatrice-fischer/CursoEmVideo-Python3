# EXERCÍCIO 19 - sortear um dos 4 alunos, ler os nomes e escrever o nome escolhido

import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]
sorteio = random.choice(lista) #escolhe um valor

print('Aluno sorteado: {}'.format(sorteio))
