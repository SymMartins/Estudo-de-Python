import random
from time import sleep

nome_jogador = str(input('Olá meu nome é Jarvis qual o seu nome? '))
print(f'Olá {nome_jogador}')

jogar = str(input('Eu adoro jogar JOKENPO! Você gostaria de jogar comigo? ')).lower()
sleep(1)
if jogar == 'sim':
    print('{:=^40}'.format(f' ÓTIMO {nome_jogador}, que bom!! '))
    sleep(1)
    print('{:=^40}'.format(' ENTÃO VAMOS JOGAR JOKENPO! '))
    print('[1] Pedra\n[2] Papel\n[3] Tesoura')
    jogada_jogador = int(input ('Escolha sua jogada: '))
    print('{:=^40}'.format(' PREPARADO? ' ))
    sleep(2)

    jogadas =[1, 2, 3]
    jogada_pc = random.choice(jogadas)

    print('JO...')
    sleep(1)
    print('QUEN...')
    sleep(1)
    print('PÔ!!')
    sleep(1)

    if jogada_jogador == 1 and jogada_pc == 2:
        print(' Eu ganhei PAPEL embrulha PEDRA!')
    elif jogada_jogador == 2 and jogada_pc == 1:
        print('Parabéns! PAPEL embrulha PEDRA, você GANHOU!')
    elif jogada_jogador == 2 and jogada_pc == 3:
        print('Eu ganhei TESOURA corta PAPEL!')
    elif jogada_jogador == 3 and jogada_pc == 2:
        print('Parabéns! TESOURA corta PAPEL, você GANHOU!')
    elif jogada_jogador == 3 and jogada_pc == 1:
        print('Eu ganhei PEDRA quebra TESOURA!')
    elif jogada_jogador == 1 and jogada_pc == 3:
        print('Parabéns! PEDRA quebra TESOURA, você GANHOU!')
    else:
        print(f'EMPATE eu coloquei {jogada_pc} e você colocou {jogada_jogador}')
else:
    print(f'Que pena eu gostaria muito de jogar JOKENPO com você {nome_jogador}')
        
