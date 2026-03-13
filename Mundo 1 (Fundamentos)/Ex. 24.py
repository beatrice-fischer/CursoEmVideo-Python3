# EXERCÍCIO 24 - ler nome de cidade, dizer se começa ou não com a palavra "Santo"

cid = str(input('Nome da cidade:')).strip()

print(cid[:5].upper() == 'SANTO')
