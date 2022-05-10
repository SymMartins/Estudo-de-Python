"""Desenvolva um programa que leia quatro valores pelo teclado e quarde-os em uma tupla. no final, mostre:
A = Quantas vezes apareceu o valor 9.
B = Em que posição foi digitado o primeiro valor 3.
C = Quais foram os números pares."""

cont = 0
numero = (int(input('Digite um valor: ')),
          int(input('Digite outro valor: ')),
          int(input('Digite mais um valor: ')),
          int(input('Digite o último valor: ')),)

print(f'Você digitou os valores {numero}')
if 9 in numero:
    print(f'O valor 9 apareceu {numero.count(9)} vezes')
else:
    print('O número 9 não foi digitado nenhuma vez!')
if 3 in numero:
    print(f'O Valor 3 apareceu na {numero.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print('Os valores pares foram: ', end='')
for par in numero:
    if par % 2 == 0:
        print(par, end=' ')
