# jogo de Jokenpô
from random import randint
from time import sleep
import emoji

pedra = emoji.emojize('✊')
papel = emoji.emojize('🖐')
tesoura = emoji.emojize('✌')

nome_jogador = str(input('Olá meu nome é Jarvis!\nQual o seu nome? ')).upper().strip()
print(f'Olá {nome_jogador}! É um prazer te conhecer!')

jogar = str(input('Eu adoro jogar JOKENPO! Você gostaria de jogar comigo? ')).lower().strip()
sleep(1)

if jogar == 'sim':
    print('{:=^40}'.format(f' ÓTIMO {nome_jogador}, que bom!! '))
    sleep(1)
    print('{:=^40}'.format(' ENTÃO VAMOS JOGAR JOKENPO! '))
    itens = ('Pedra', 'Papel', 'Tesoura')
    jarvis = randint(0, 2)
    print('Escolha entre: [ 0 ] PEDRA ' + pedra, '[ 1 ] PAPEL ' + papel, '[ 2 ] TESOURA ' + tesoura)
    jogador = int(input('O que você vai jogar? '))
    print('{:=^40}'.format(' PREPARADO? '))
    sleep(1)
    print('{:=^40}'.format(' ENTÃO VAMOS LÁ...'))
    sleep(1)
    print('JO...', pedra)
    sleep(1)
    print('KEN...', pedra)
    sleep(1)
    print('POOO', pedra)
    print('=--=' * 10)
    print('Jarvis jogou: {}'.format(itens[jarvis]))
    print('{} jogou: {}'.format(nome_jogador, itens[jogador]))
    print('=--=' * 10)
    if jarvis == 0:   # computador jogou PEDRA
        if jogador == 0:
            print(f'Nossa {nome_jogador}! Nós pensamos igual!! EMPATAMOS!!')
        elif jogador == 1:
            print(f'VOCÊ me VENCEU {nome_jogador}!! PARABÉNS!')
        elif jogador == 2:
            print('AH-RÁ! EU te VENCI!!')
        else:
            print('jogada INVÁLIDA!')
    elif jarvis == 1:  # computador jogou PAPEL
        if jogador == 0:
            print('AH-RÁ! EU te VENCI!!')
        elif jogador == 1:
            print(f'Nossa {nome_jogador}! Nós pensamos igual!! EMPATAMOS!!')
        elif jogador == 2:
            print(f'VOCÊ me VENCEU {nome_jogador}!! PARABÉNS!')
        else:
            print('jogada INVÁLIDA!')
    elif jarvis == 2:  # computador jogou TESOURA
        if jogador == 0:
            print(f'VOCÊ me VENCEU {nome_jogador}!! PARABÉNS!')
        elif jogador == 1:
            print('AH-RÁ! EU te VENCI!!')
        elif jogador == 2:
            print(f'Nossa {nome_jogador}! Nós pensamos igual!! EMPATAMOS!!')
        else:
            print('jogada INVÁLIDA!')
else:
    print(f'Que pena! Eu gostaria muito de jogar JOKENPO com você {nome_jogador}!')
