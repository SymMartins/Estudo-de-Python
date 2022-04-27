# Procurando uma string dentro de outra

# Forma 1
nome = input('Qual é o seu nome completo? ').strip().upper()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

# Forma 2
s_nome = 'SILVA' in nome
print(f'Seu nome tem Silva? {s_nome}')
