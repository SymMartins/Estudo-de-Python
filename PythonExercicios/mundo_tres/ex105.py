"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas
    – A maior nota
        – A menor nota
            – A média da turma
                – A situação (opcional)"""


def notas(*n, sit=False):
    """
    -> Função para analizar as notas e sutuações de vairos alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: (opcional) indica se deve ou não adicionar a situação
    :return: dicionáario com várias informações sobre a situação do aluno
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['média'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    return r


# Programa Principal:
resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
# help(notas)
