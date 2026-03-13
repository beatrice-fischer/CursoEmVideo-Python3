# EXERCÍCIO 33 - ler 3 números, mostrar o maior e o maior

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#verificar o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#verificar o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
