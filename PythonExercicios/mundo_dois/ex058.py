'''melhore o jogo do DESAFIO 028 onde o computador vai "PENSAR" em um numero entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar mostrando no final quantos palpites foram necessários para vencer'''

from random import randint
numero_pensado = randint(0, 10)
print('Olá! Meu nome é Jarvis... E acabei de pensar em um número de 0 a 10.')
print('Será que você consegue adivinhar qual foi este número?')

acertou = False
palpites = 0
while not acertou:
    numero = int(input('Qual o seu palpite? '))
    palpites += 1
    if numero == numero_pensado:
        acertou = True
    else:
        if numero < numero_pensado:
            print('Mais... Tente mais uma vez.')
        elif numero > numero_pensado:
            print('Menos... Tente mais uma vez.')

print(f'Acertou com {palpites} tentativas. Parabéns!')