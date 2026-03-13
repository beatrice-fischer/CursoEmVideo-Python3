# EXERCÍCIO 12 - leia o preço do produto e mostre o novo preço com 5% de desconto

preco = float(input('Qual é o preço do produto? R$'))
print('O preço atualizado do produto é: R${:.2f}'.format(preco*0.95)) #ou preco*5/100
