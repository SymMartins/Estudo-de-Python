"""Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos."""
def lin():
    print('-=' * 15)


def titulo(txt):
    print('-=' * 30)
    print(txt)
    print('-=' * 30)


# programa principal:
titulo('curso em video')
titulo('aprenda python')
titulo('oi')
lin()


# Parte prática da aula:
def soma(a, b):
    s = a + b
    print(s)


# programa principal:
soma(4, 5)
soma(8, 9)
soma(2, 1)
lin()


# ex 2:
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# programa principal:
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a=5, b=4)
lin()


# ex 3:
def contador(*num):  # * é um desempacotador para poder variar a quantidade de parametros na função:
    tam = len(num)
    print(f'Recebi os valores de {num} e são ao todo {tam} números')


# Programa Principla:
contador(1, 3, 4, 5)
contador(1, 2, 5)
contador(9)
contador(9, 4, 3, 4, 8)
lin()


# ex 4:
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)
lin()


# ex 5:
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


soma(5, 2)
soma(2, 9, 4)
