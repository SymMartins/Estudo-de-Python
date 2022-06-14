"""Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""


jogador = dict()
partidas = list()

# Dados do jogador
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()

# Quantas partidas o jogador fez
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

# Quantos gols foram feitos por partida
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
jogador['gols'] = partidas[:]

# Soma quantos gols foram feitos no total
jogador['total'] = sum(partidas)

# Exibe o resultado 1
print('-=' * 30)
print(jogador)
print('-=' * 30)

# Exibe o resultado 2
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

# Exibe o resultado 2
print(f'O Jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i + 1}, fez {v} gols')
print(f'O jogador {jogador["nome"]} tem um total de {jogador["total"]} gols')
