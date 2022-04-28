'''melhore o jogo do DESAFIO 028 onde o computador vai "PENSAR" em um numero entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar mostrando no final quantos palpites foram necessários para vencer'''

from random import randint
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
numero_pensado = randint(0, 10)
print(numero_pensado)
numero = int(input('Qual o seu palpite: '))
palpite = 0

if numero_pensado > numero:
    print('Mais...')
elif numero_pensado < numero:
    print('Menos...')

while numero_pensado != numero:
    numero = int(input('Tente mais uma vez: '))

    if numero_pensado > numero:
        print('Mais...' )
    elif numero_pensado < numero:
        print('Menos...')

    if numero_pensado != numero:
        palpite += 1

if numero_pensado == numero:
    palpite += 1
    print(f'Acertou com {palpite} tentativas. Parabéns!!!')