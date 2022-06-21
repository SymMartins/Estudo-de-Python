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


def lin(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(lin())
    print(txt.center(42))
    print(lin())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(lin())
    opc = leiaInt('\033[32mSua Opção:\033[m ')
    return opc
