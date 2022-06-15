"""Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""

# Funções:
def area(larg, comp):
    s = l * c
    print(f'Com as medidas de: {larg}m comprimento e: {comp}m largura, seu terreno tem: {s}m²')


def cabeçalho():
    print('-=' * 23)
    print(' << Calculadora de M² para terrenos >> ')
    print('-=' * 23)


# programa principal:
cabeçalho()
l = float(input('Digite o comprimento do terreno me metros: '))
c = float(input('Digite a largura do terreno me metros: '))
area(l, c)
