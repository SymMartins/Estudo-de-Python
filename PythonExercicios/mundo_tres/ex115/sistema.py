from PythonExercicios.mundo_tres.ex115.libi.interface import *
from PythonExercicios.mundo_tres.ex115.libi.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar um conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do programa... Até Logo!')
        break
    else:
        print('\033[31mERRO!! Digite uma opção válida!\033[m')
    sleep(2)

