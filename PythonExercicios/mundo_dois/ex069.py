"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o preograma deverá perguntar se o usuário quer ou não continuar.
no final mostre:

A = quantas pessoas tem mais de 18 anos.
b = Quantos homens foram cadastrados.
c = quantas mulheres tem menos de 20 anos."""

pessoas = homem = mulher20 = 0

while True:
    print('CADASTRO DE PESSOAS')
    print('-' * 25)
    idade = int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo [M/F]? ')).upper().strip()[0]
    if idade >= 18:
        pessoas += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulher20 += 1

    print('-' * 42)
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja continuar com o cadastro? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break
    print('-' * 42)
print('CADASTRO FINALIZADO.')
print(f'Temos {pessoas} pessoas com mais de 18 anos!')
print(f'Temos {homem} homens cadastrados!')
print(f'temos {mulher20} mulhers com menos de 20 anos!')
