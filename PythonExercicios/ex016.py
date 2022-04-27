#Quebrando o número

'''
modo de fazer 1

from math import floor, trunc
valor = float(input('Digite um valor: '))
inteiro = trunc(valor)  #floor(valor)
print('O valor digitado foi: {} e a sua porção inteira é: {}'.format(valor, inteiro))
'''

#modo de fazer 2

num = float(input('Digite um valor '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))