"""Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela."""

# 1.º O dicionário:
dados = {}
resultado = 0
# 2.º Lê nome e média do aluno:
dados['nome'] = str(input('Nome do aluno: ')).title().strip()
dados['media'] = float(input(f'Média do {dados["nome"]} : '))
# 3.º Verifica se está aprovado, reprovado ou em recuperação:
if dados['media'] >= 7:
    resultado = 'Aprovado'
elif 7 > dados['media'] >= 5:
    resultado = 'Recuperação'
else:
    resultado = 'Reprovado'
# 4.º Mostra a estrutura na tela:
print('-=' * 30)
print(f'  - Aluno: {dados["nome"]}')
print(f'  - A média do {dados["nome"]} é de: {dados["media"]}')
print(f'  - A sintuação do {dados["nome"]} é de: {resultado}')

# ------------------------------------------Resolução do Guanabara ---------------------------------------------------

# 1.º O dicionário:
dados = {}
# 2.º Lê nome e média do aluno:
dados['nome'] = str(input('Nome do aluno: ')).title().strip()
dados['media'] = float(input(f'Média do {dados["nome"]} : '))
# 3.º Verifica se está aprovado, reprovado ou em recuperação:
if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'
elif 7 > dados['media'] >= 5:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
# 4.º Mostra a estrutura na tela:
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} é igual a {v}')
