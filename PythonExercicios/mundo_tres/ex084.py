"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas:
    B) Uma listagem com as pessoas mais pesadas:
        C) Uma Listagem com as pessoas mais leves"""

# 1.º Criar uma lista:
pessoas = list()
dados = list()
maispesadas = maisleves = 0

# 2.º Adicionar na lista nome e peso de várias pessoas:
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    # 4.º Gera a informação com as pessoas mais pesadas e mais leves:
    if len(pessoas) == 0:
        maispesadas = maisleves = dados[1]  # dados na posição [0] é igual a nome e dados na posição [1] é igual a peso!
    else:
        if dados[1] > maispesadas:
            maispesadas = dados[1]
        if dados[1] < maisleves:
            maisleves = dados[1]
    pessoas.append(dados[:])
    dados.clear()

# 5.º Sai do arco e exibe o resultado:
    sair = str(input('Deseja continuar cadastrando? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break

# 3.º Calcula quantas pessoas foram cadastradas e exibe a resposta:
print('-=' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas')

# 6.º Resultado das pessoas mais pesadas
print(f'O maior peso foi de {maispesadas} Kg. Peso de ', end='')
for pes in pessoas:  # pes (pessoas) para fazer como contador
    if pes[1] == maispesadas:
        print(f'[{pes[0]}]', end=' ')
print()
# 7.º Resultado das pessoas mais leves
print(f'O menor peso foi de {maisleves} Kg. Peso de ', end='')
for pes in pessoas:
    if pes[1] == maisleves:   # pes (pessoas) para fazer como contador
        print(f'[{pes[0]}]', end=' ')
print()
