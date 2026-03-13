# EXERCÍCIO 10 - leia quanto dinheiro tenho na carteira e mostra quantos dólares posso comprar (USD1,00 = RS3,27)

din = float(input('Quanto dinheiro tenho em reais?'))
print('Com R${:.2f}, posso comprar US${:.2f} dólares!'.format(din,din/3.27))
