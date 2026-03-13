# EXERCÍCIO 15 - Aluguél de carros: dias alugado, Km rodados, valor a pagar (60 reais por dia e 0,15 reais por km)

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias*60) + (km*0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
