"""Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[31mERRO!! Por favor, digite um número inteiro válido\33[m')
            continue
        except (KeyboardInterrupt):
            print('\n\33[31mO usuário preferiu não digitar este número.!\33[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\33[31mERRO!! Por favor, digite um número real válido\33[m')
            continue
        except (KeyboardInterrupt):
            print('\n\33[31mO usuário preferiu não digitar este número.!\33[m')
            return 0
        else:
            return n


# programa principal:

n1 = leiaInt('Digite um nº Inteiro: ')
n2 = leiaFloat('Digite um nº Real: ')

print(f'Você acabou de digitar o número {n1} e o real foi {n2}')
