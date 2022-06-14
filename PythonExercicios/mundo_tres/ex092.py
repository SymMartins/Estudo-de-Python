"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
 Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
 Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""
from datetime import datetime

# Dados da pessoa
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho nº. (0 não tem): '))

# Dados da carteira de trabalho e idade para se aposentar
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Qual o salário? '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

# Exibe dados:
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
