# Analisador de Textos

nome = input('Digite seu nome completo: ').strip()
dividido = nome.split()
primeiro_nome = dividido[0]

print('Analisando seu nome...')
print(f'Seu nome com letras maiúsculas é: {nome.upper()}')
print(f'Seu nome com letras minúsculas é: {nome.lower()}')
print('Seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é: {} e ele tem: {} letras'.format(primeiro_nome, len(dividido[0])))
