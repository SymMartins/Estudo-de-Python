''' Crie um programa que leia VARIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor
999 que é a CONDIÇÃO DE PARADA. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag) '''

numero = cont = soma = 0
numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    cont += 1
    soma += numero
    numero = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} e a soma entre eles foi {soma}')
