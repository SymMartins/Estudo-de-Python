"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta."""

# 1.º Importa as bibliotecas das random e time as funções randint e sleep:
from random import randint
from time import sleep

# 2.º Cria o cabeçalho do progrma:
print('-=' * 16)
print('      JOGA NA MEGA-SENA      ')
print('-=' * 16)

# 3.º Pergunta ao usuário quantos jogos ele quer fazer:
jogo = int(input('Quantos jogos você que que eu sorteie? '))

# 4.º Criando as variaveis:
lista = list()
jogos = list()
total = 1

# 5.º Gera os números aleatórios adiciona na lista sem números repitidos:
while total <= jogo:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        # 6.º Restringe em seis número
        if cont >= 6:
            break
    # 7.º Adiciona na lista Jogos a quantidade de jogos pedidos pelo usuário e apaga a lista inicial:
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-=' * 3, f'SORTEANDO {jogo} JOGOS', '=-' * 3)

# 8.º Mostra a lista de números sorteados em ordem crescente:

for indice, lista in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lista}')
    sleep(1)

print('-=' * 5, '< BOA SORTE! >', '=-' * 5)
