# EXERCÍCIO 31 - pergunte a distância de uma viagem em km. Preço da passagem: R$0,50 por km até 200km e R$0,45 por km para viagens mais longas

km = float(input('Qual a quantidade de km para a viagem: '))

if km <= 200:
    print('O valor da passagem para a viagem de {}Km é R${}'.format(km, km*0.5))
else:
    print('O valor da passagem para a viagem de {}Km é R${}'.format(km, km*0.45))

#ou
preco = km*0.5 if km <=200 else km*0.45
print('O valor da passagem para a viagem de {}Km é R${}'.format(km, preco))
