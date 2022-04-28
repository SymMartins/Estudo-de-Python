""" Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

resp = 'S'
soma = cont = media = maior = menor = 0
while resp in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip() [0]
media = soma / cont
print(f'Você digitou {cont} número e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
