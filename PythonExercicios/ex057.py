'''faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". caso esteja errrado, peça
a digitação novamente até ter um valor correto'''

sexo = str(input('Informe seu sexo [M / F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos! Por favor, informe seu sexo [M/F]')).strip().upper()[0]

print(f'Sexo {sexo} registrado com sucesso')
