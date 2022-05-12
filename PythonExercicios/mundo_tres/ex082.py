"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas."""

# 1.º Criar 1ª lista:
numero = []
# 2.º Adicionar vários números na lista 1:
while True:
    numero.append(int(input('Digite um número: ')))
    sair = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
# 3.º Criar uma lista para os valores pares e impares:
pares = []
impares = []
for i, valor in enumerate(numero):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)

print('-=' * 30)

# 4.º Mostrar o conteúdo das 3 listas:
print(f'Os números digitados foram: {numero}.')
print(f'Os números pares digitados foram: {pares}.')
print(f'Os números impares digitados foram {impares}.')
