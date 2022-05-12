"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

# 1.º Criar uma lista:
valor = []

# 2.º cadastrar os números já na posição correta de inserção:
for cont in range(0, 5):
    numero = int(input('Digite um valor: '))
    if cont == 0 or numero > valor[-1]:
        valor.append(numero)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(valor):
            if numero <= valor[pos]:
                valor.insert(pos, numero)
                print(f'Adicionado da posição {pos} da lista...')
                break
            pos +=1
# 3.º Mostrar a lista em forma ordenada:

print('-=' * 30)
print(f'Os valores digitados foram: {valor}')

