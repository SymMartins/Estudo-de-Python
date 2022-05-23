"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
    B) A soma dos valores da terceira coluna.
        C) O maior valor da segunda linha."""

# Exercício anterior:
# 1.º Cria a matriz:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = maior = soma_coluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor para: L: [{linha + 1}], C: [{coluna + 1}]: '))

# 2.º Mostra a matriz organizada:
print('-=' * 21)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')

        # 3.º Soma todos os valores pares da matriz
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
    print()  # Quebra a linha para organizar as colunas
print('-=' * 21)

# 4.º Soma a terceira coluna:
for linha in range(0, 3):
    soma_coluna += matriz[linha][2]

# 5.º Descobre qual é o maior número da segunda linha:
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]

# 6.º Mostra as respostas A B e C:
print(f'A soma dos valores pares é {soma_par}')    # Resposta da letra A
print(f'O resultado da soma da 3.º coluna é {soma_coluna}')    # resposta da letra B
print(f'O maior valor da 2.º linha é {maior}')    # resposta da letra C
