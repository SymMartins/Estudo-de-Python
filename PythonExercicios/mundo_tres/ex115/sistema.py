from libi.interface import *
from time import sleep
while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do programa... Até Logo!')
        break
    else:
        print('\033[31mERRO!! Digite uma opção válida!\033[m')
    sleep(2)

