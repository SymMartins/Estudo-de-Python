# Primeira e última ocorrência de uma string

frase = str(input('Digite uma frase: ')).strip().upper()

print('A primeira letra A aparece na {}ª posição \nE aparece {} vezes na frase.'.format(frase.find('A') + 1, frase.count('A')))
print('Já última letra A aparece na {}ª posição'.format(frase.rfind('A')+1))