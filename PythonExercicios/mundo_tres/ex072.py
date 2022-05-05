"""Crie um programa que tenha uma TUPLA totalmente prenchida com uma contagem por extenso, do zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso"""

numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

continua = 0
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')

    print(f'Você digitou o número {numeros[num]}')
    continua = str(input('Deseja continuar?[Sim/Não] ')).upper().strip()[0]
    if continua == 'N':
        break

