'''DESENVOLVA UM PROGRAMA QUE LEIA 6 NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES.
SE O VALOR FOR IMPAR DESCONSIDERE-O'''
soma = 0
cont = 0
for contador in range(1, 7):
    numero = int(input(f'Digite o {contador} valor: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {soma}')