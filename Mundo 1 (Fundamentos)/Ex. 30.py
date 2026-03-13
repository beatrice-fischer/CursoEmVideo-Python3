# EXERCÍCIO 30 - ler número inteiro, mostrar se é par ou ímpar

n = int(input('Digite um numero inteiro: '))

if n%2 == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é ímpar'.format(n))

#ou
print('O número é par' if n%2==0 else "O número é ímpar")
