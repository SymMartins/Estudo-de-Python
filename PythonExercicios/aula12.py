#Condições Aninhadas

#para entender a formação da condição aninhada
"""if carro_esquerda():
    pass
elif carro_direita():
    pass
else:
    pass"""

#aula:

nome = str(input('Qual o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é normal:')
print('tenha um bom dia, {}'.format(nome))