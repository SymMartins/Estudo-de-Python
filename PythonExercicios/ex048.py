'''FACA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS IMPARES QUE SÃO MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM NO
INTERVALO DE 1 ATÉ 500'''

soma = 0
contador = 0
for numeros in range(1, 501, 2):
    if numeros % 3 == 0:
        soma += numeros
        contador += 1
print(f'A soma de todos os {contador} valores solicitados é {soma}')

