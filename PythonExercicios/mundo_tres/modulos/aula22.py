"""Nessa aula, vamos continuar os nossos estudos de funções em Python, aprendendo como criar módulos em Python
e reutilizar os nossos códigos em outros projetos. Vamos aprender também como agrupar vários módulos em um pacote,
ampliando ainda mais a modularização em grandes projetos em Python."""
from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O Fatorial de {num} é {fat}.')
print(f'O Dobro de {num} é {numeros.dobro(num)}')
print(f'O Triplo de {num} é {numeros.triplo(num)}')

numeros.lin()
print('===> PACOTES <===')
numeros.lin()
