# EXERCÍCIO 27 - ler nome completo, mostrar primeiro e último nome separados

nome = str(input('Digite seu nome completo: ')).strip().split()

print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))
