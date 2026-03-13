# EXERCÍCIO 20 - sortear ordem de apresentação de 4 alunos, ler os nomes e escreva a ordem de apresentação

import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

lista = [a1, a2, a3, a4]
random.shuffle(lista)

print('A ordem de apresentação será: {}')
print(lista)
