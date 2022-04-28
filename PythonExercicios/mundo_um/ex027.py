# Primeiro e último nome de uma pessoa

n = str(input('Digite seu nome completo: ')).strip().lower()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome[0].capitalize()))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1].capitalize()))
