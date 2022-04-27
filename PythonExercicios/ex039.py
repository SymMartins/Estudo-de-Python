#alistamento militar

from datetime import date
nascimento = int(input('Digite o ano do seu nascimento: '))
idade_alistamento = 18
ano_alistamento = nascimento + idade_alistamento
ano = date.today().year
anos = nascimento + idade_alistamento - ano

if ano - nascimento > idade_alistamento:
    print(f'Você deveria ter se alistado em {ano_alistamento}!')
    print(f'Já se passaram {abs(anos)} anos, da hora de se alistar!')
elif ano - nascimento == idade_alistamento:
    print('Você tem que se alistar ESTE ANO!!')
else:
    print(f'Você vai se alistar em {ano_alistamento}!')
    print(f'Calma, faltam {abs(anos)} anos para se alistar, sua hora ainda vai chegar!!')





