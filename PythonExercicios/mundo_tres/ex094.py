"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
 e todos os dicionários em uma lista.
No final, mostre:
    A) Quantas pessoas foram cadastradas
        B) A média de idade
            C) Uma lista com as mulheres
                D) Uma lista de pessoas com idade acima da média"""
# Lista, dicionário e variáveis
galera = list()
pessoa = dict()
soma = media = 0

# Entrada dos dados
while True:
    pessoa.clear()  # Apaga os dados do dicionário pessoas
    pessoa['nome'] = str(input('Nome: ')).strip().title()

    # Dar entrada no sexo da pessoa e verifica se o usuário digitou apenas M ou F
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')  # Exibe um erro se o usuário não digitou corretamente o sexo
    pessoa['idade'] = int(input('Idade: '))  # Pede a idade da pessoa cadastrada
    soma += pessoa['idade']  # Soma a idade das pessoas cadastradas
    galera.append(pessoa.copy())

    # Pergunta se o usuário deseja continuar cadastrando
    while True:
        continuar = str(input('Deseja continuar cadastrando? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')  # Exibe erro se o usuário não digitar S ou N
    if continuar == 'N':
        break

# Exibe na tela as respostas A B C D:
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')  # Exibe quantas pessoas foram cadastradas
media = soma / len(galera)  # Calcula a média de todas as pessoas cadastradas
print(f'A média de idade é de {media:5.2f} anos')

# Mostra quais foram as mulheres cadastradas
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()

# Mostra quais pessoas estão acima da média de idade
print('Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v, in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
