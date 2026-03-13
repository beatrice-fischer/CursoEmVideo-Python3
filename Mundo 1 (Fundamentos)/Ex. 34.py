# EXERCÍCIO 34 - perguntar salário, calcular o aumento. Salário superior a R$1250,00 +10%. Salários inferior +15%.

salario = float(input('Qual é o seu salário? '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario*1.10
print('Seu salário com aumento será de R${:.2f}'.format(novo))
