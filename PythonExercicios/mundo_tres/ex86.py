"""Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
 No final, mostre a matriz na tela, com a formatação correta."""

# 1.º Cria a matriz:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor para: L: [{linha + 1}], C: [{coluna + 1}]: '))
# 2.º Mostra a matriz organizada:
print('-=' * 21)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()  # Quebra a linha para organizar as colunas
