'''crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA

seu programa deverá realizar a operação solicitada em cada caso. '''
from time import sleep
valor_um = int(input('Digite o valor um: '))
valor_dois = int(input('Digite o valor dois: '))
opcao_5 = False
while not opcao_5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        resultado = valor_um + valor_dois
        print(f'A soma entre {valor_um} e {valor_dois} é {resultado}')

    elif opcao == 2:
        resultado = valor_um * valor_dois
        print(f'O resultado entre {valor_um} x {valor_dois} é {resultado} ')

    elif opcao == 3:
        if valor_um > valor_dois:
            print(f'Entre o {valor_um} e o {valor_dois} o maior é {valor_um}')
        else:
            print(f'Entre o {valor_um} e o {valor_dois} o maior é {valor_dois}')

    elif opcao == 4:
        valor_um = int(input('Digite o valor um: '))
        valor_dois = int(input('Digite o valor dois: '))

    elif opcao == 5:
        opcao_5 = True
    else:
        print('Opção inválida. Tente novamente! ')
    print('=-=' * 10)
    sleep(2)
print('Programa finalizado')
