# EXERCÍCIO 04
t = input("Digite algo: ")
print('O tipo primitivo desse valor é ',type(t)) #métodos de teste de tipo
print('Só tem espaços? ',t.isspace())
print('É um número? ', t.isnumeric())
print('É alfabético? ', t.isalpha())
print('É alfanumérico', t.isalnum())
print('Está em maiúsculas? ', t.isupper())
print('Está em minúsculas? ', t.islower())
print('Está capitalizada? ', t.istitle())