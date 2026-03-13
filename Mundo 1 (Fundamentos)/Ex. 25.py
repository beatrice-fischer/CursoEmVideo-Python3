# EXERCÍCIO 25 - ler nome completo e diga se tem "Silva" no nome

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome tem SILVA? {}'.format('SILVA' in nome.upper()))
