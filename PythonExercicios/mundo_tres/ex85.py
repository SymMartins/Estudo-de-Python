"""Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma (lista única) que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente."""

# 1.º Criar uma lista:
numeros = list()  # 1.º modo de criar uma lista
par = []  # 2.º modo de criar uma lista
impar = []

# 2.º Números adiconados pelo usuário, total de 7 números:
for cont in range(0, 7):
    numeros.append(int(input(f'Digite o {cont + 1}.º número: ')))

# 3.º Separando os números pares e impares:
for num in numeros:
    if num % 2 == 0:
        par.append(num)
        par.sort()
    else:
        impar.append(num)
        impar.sort()
# 4.º Mostra os valores pares e impares em ordem crescente:
print('-=' * 30)
print(f'Os números pares são: {par}')
print(f'Os números impares são: {impar}')
print()

# ------------------------------------ RESOLUÇÃO DO EX. 85 DA FORMA CORRETA --------------------------------------------

numeros = [[], []]
valor = 0
for num in range(1, 8):
    valor = int(input(f'Digite o {num}.º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print('-='*30)
print(f'Os números pares são: {numeros[0]}')
print(f'Os números impares são: {numeros[1]}')
