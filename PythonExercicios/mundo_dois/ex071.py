"""Crie um programa que simule o funcionamento de um caixa eletrônica.
No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$: 50,00 - R$ 20,00 - R$ 10,00 e R$ 1,00."""

print('=' * 35)
print('{:-^35}'.format(' Banco do Sym Salamim '))
print('=' * 35)
valor = int(input('Qual o valor a ser sacado? '))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cedulas de R$:{ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 35)
print('Volte sempre ao banco Sym Salamim')
print('=' * 35)
