# EXERCÍCIO 29 - velocidade de um carro. Se ultrapassar 80km/h, mostre mensagem de multa de 7 reais por km acima do limite

vel = float(input('Qual a velocidade do carro? '))

if vel > 80:
    print('Multa por excesso de velocidade. {}Km/h. R${}'.format(vel,(vel - 80) * 7))
else:
    print('Dentro do limite de velocidade!')
