"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado."""

# 1.º Importar bibliotecas:
from random import randint
from time import sleep
from operator import itemgetter  # coloca o Dicionário em ordem!

# 2.º Criar o dicionario:
jogo = {'Jogador-1': randint(1, 6),
        'Jogador-2': randint(1, 6),
        'Jogador-3': randint(1, 6),
        'Jogador-4': randint(1, 6)}

# 3.º Criar lista RANKING
ranking = list()

# 4.º Coloca o dicionario em ordem crescente:
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # Esta linha coloca o ranking em ordem

# 5.º Mostra o resultado na tela:
print('Valores Sorteados:')
print('-=' * 15)
for k, v, in jogo.items():
    print(f'  {k} tirou {v} no dado.')
    sleep(1)
print('-=' * 15)
print('  ==RANKING DOS JOGADORES ==')
for i, v, in enumerate(ranking):
    print(f'  {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
