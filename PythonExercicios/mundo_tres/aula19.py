"""Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves literais."""

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 95.5
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print(pessoas.items())
print(pessoas.values())
print(pessoas.keys())
for k, v, in pessoas.items():
    print(f'{k} = {v}')
print()
# ----------------------------------------------------------------------------------------------------------------------

brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print('Dicionário 1')
print(estado1)
print('Dicionário 2')
print(estado2)
print('Lista Brasil com os dicionários 1 e 2')
print(brasil)
print('-=' * 40)
print(brasil[0]['UF'])
print(brasil[0]['Sigla'])
print(brasil[1]['UF'])
print(brasil[1]['Sigla'])

# ----------------------------------------------------------------------------------------------------------------------
print('-=' * 40)
est = dict()
br = list()
for c in range(0, 3):
    est['Uf'] = str(input('Unidade Federativa: ')).title()
    est['Sigla'] = str(input('Sigla: ')).upper()
    br.append(est.copy())   # Para criar uma cópia em dicionário deve utilizar o metodo .copy
print('-=' * 50)
print(br)
print('-=' * 50)
for e in br:
    for k, v, in e.items():
        print(f'O campo {k} tem valor {v}.')
print('-=' * 30)
for e in br:
    for v in e.values():
        print(v, end=' ',)
    print()
print('-=' * 30)
