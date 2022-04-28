# IF e ELSE Condições (Parte 1)

#Exemplo de uma condição:
"""tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('--FIM--')"""

#Exemplo de uma condição:

"""nome = str(input('Qual é o seu nome? '))
if nome == 'Sym':
    print('Que nome lindo!!!')
print(f'Bom dia, {nome}!')"""

#Exemplo de uma condição:

"""nome = str(input('Qual é o seu nome? '))
if nome == 'Sym':
    print('Que nome lindo você tem:')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')"""

#Exemplo de uma condição:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print('A sua média foi: {:.1f}'.format(m))
print('PARABÉNS' if m >=6 else 'ESTUDE MAIS!!!')