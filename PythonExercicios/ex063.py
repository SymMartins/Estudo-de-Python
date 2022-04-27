'''escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma sequencia Fibonacci:
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8'''
from time import sleep
print('-=-' * 8)
print('Sequencia de Fibonacci')
print('-=-' * 8)
sleep(1)
print('~~' * 18)
n = int(input('Quantos termos você quer mostrar? '))
print('~~' * 18)
t1 = 0
t2 = 1
print(f'{t1} - {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' - {t3}', end='')
    cont += 1
    t1 = t2
    t2 = t3
print(' - FIM')
print('~~' * 18)
