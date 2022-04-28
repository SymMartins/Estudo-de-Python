sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Sexo invalido! Digite seu sexo [M/F]: '))
print(f'Sexo {sexo} registrado com sucesso!')

