# EXERCÍCIO 22 - leia nome completo, mostrar ele maiúsculo, minúsculo, total de letras sem espaços, quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome ...')
print('Maiúscula: {}'.format(nome.upper()))
print('Minúscula: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(nome) - nome.count(' ')))
print('Quantidade de letras do primeiro nome: {}'.format(nome.find(' ')))
# ou separa = nome.split()
# print('Seu primeiro nome é {} e ele tem {} letras').format(separa[0], len(separa[0])))
