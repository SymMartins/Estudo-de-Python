"""Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""

# Exercício nº. 93

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()  # Limpa o dicionário jogador
    # Dados do jogador
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    # Quantas partidas o jogador fez
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    # Quantos gols foram feitos por partida
    partidas.clear()  # apaga os dados da lista partida
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    # Soma quantos gols foram feitos no total
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())  # Adiciona o jogador na lista time
    # Pergunta se quer continuar cadastrando novos jogadors
    while True:
        continuar = str(input('Deseja continuar cadastrando? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')  # Exibe erro se o usuário não digitar S ou N
    if continuar == 'N':
        break

# Exibe o cabeçalho
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
# Exibe o resultado
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
# Mostra dados de um jogador específico
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe o jogador com o código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
        print('-' * 40)
print('<< VOLTE SEMPRE >>')
