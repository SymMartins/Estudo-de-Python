# Sorteando uma ordem na lista
import random

aluno_um = str(input('Primeiro aluno: '))
aluno_dois = str(input('Segundo aluno: '))
aluno_tres = str(input('Terceiro aluno: '))
aluno_quatro = str(input('Quarto aluno: '))

lista = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]
random.shuffle(lista)
print('A ordem de apresentação sera: \n {}'.format(lista))