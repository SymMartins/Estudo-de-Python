# Sorteando um item na lista
import random
aluno_um = str(input('Primeiro Aluno: '))
aluno_dois = str(input('Segundo Aluno: '))
aluno_tres = str(input('Terceiro Aluno: '))
aluno_quatro = str(input('Quarto Aluno: '))
lista = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]
sorteio = random.choice(lista)
print('O aluno escolido foi {}:'.format(sorteio))



