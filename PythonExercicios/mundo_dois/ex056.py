'''DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA MOSTRE:
 1: A MÉDIA DE IDADE DO GRUPO
 2: QUAL O NOME DO HOMEM MAIS VELHO
 3: QUANTAS MULHERES TEM MENOS DE 20 ANOS'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for pessoa in range(1,5):
    print(f'-----{pessoa}ª PESSOA -----')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M /F]: ')).strip()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <= 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print((f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}'))
print(f'E temos {totmulher20} mulheres com menos de 20 anos')
