#Associação de natação

from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano_nascimento
print(f'Você tem {idade} anos e sua categoria de competição será:')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')

"""if idade <= 9:
    print('MIRIM')
elif 14 >= idade > 9:
    print('INFANTIL')
elif 19 >= idade > 14:
    print('JUNIOR')
elif 25 >= idade > 19:
    print('SÊNIOR')
else:
    print('MASTER')
"""
