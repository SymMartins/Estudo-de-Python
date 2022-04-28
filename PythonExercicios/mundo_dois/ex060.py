'''faça um programa que leia um número qualquer e mostre o seu FATORIAL
Ex: 5! = 5x4x3x2x1 = 120'''
from math import factorial

'''f = factorial(numero)
print(f'O fatorial de {numero} é {f}' )''' # utilizando o modulo Fatorial
numero = int(input(''' Digite um número para
 calcular seu fatorial: '''))
c = numero
f = 1
print(f'Calculando {numero}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')