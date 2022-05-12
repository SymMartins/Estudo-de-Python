"""Crie um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre o maior e o menor valor digitado e as suas respectivas posições na lista"""

# 1.º Ler cinco valores e guardar em uma lista:
maior = menor = 0
valor = []
valor_max = int(input('Digite o valor máximo: '))
for cont in range(0, valor_max):
    valor.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'Você digitou os valores: {valor}')

# 2.º Mostrar o valor maior e menor digitado:
maior = max(valor)
menor = min(valor)

print(f'O maior valor digitado foi: {maior} nas posições. ', end='')
# 3.º Mostrar as suas posições na lista:
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i}...', end=' ')
print()

print(f'O menor valor digitado foi: {menor} nas posições. ', end='')
# 3.º Mostrar as suas posições na lista:
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i}...', end=' ')
print()
print('Fim')
