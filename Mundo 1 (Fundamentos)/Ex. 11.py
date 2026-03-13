# EXERCÍCIO 11 - leia a altura e largura de uma parede em metros, calcule a área e a quantidade de tinta necessária, sabendo que cada litro pinta 2m²

alt = float(input('Altura da parede: '))
larg = float(input('Largura da parede: '))
print('Área da parede = {}'.format(alt*larg))
print('Quantidade de tinta necessária = {}L'.format((alt*larg)/2))
