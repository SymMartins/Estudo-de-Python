"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo"""

while True:
    print('-'*32)
    numero = int(input('Qual taboada você quer saber? '))
    print('-' * 32)
    if numero <= 0:
        break
    for contador in range(1, 11):
        print(f'{numero} x {contador} = {numero * contador}')
print('Programa Tabuada encerrado. Volte sempre!')
