# EXERCÍCIO 26 - ler frase e mostre: quantas vezes "A" aparece, primeira e última vez

frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeiro letra A apareceu na posição {}'.format(frase.find('A')+1)) #+1 porque começa em 0
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
