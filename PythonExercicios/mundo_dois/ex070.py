"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A = Qual o total gasto na compra
B = quantos produtos custam mais de R$: 1000,00.
C = Qual o nome do produto mais barato. """
print('-' * 30)
print('{:-^30}'.format(' Lojinha do Sym '))
print('-' * 30)

total_compras = total_mil = menor_preco = cont = 0
barato = ''
while True:

    cont += 1
    produto = str(input('Digite um produto: ')).strip().title()
    preco = float(input('Valor do produto R$: '))

    total_compras += preco
    if preco > 1000:
        total_mil += 1
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        barato = produto

    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja continuar cadastrando novos produtos [S/N]? ')).upper().strip()[0]
    if sair == 'N':
        break

print(f'O total da sua compra foi de R$: {total_compras:.2f}.')
print(f'Temos {total_mil} produtos custando mais de R$: 1000.00')
print(f'O produto mais barato foi {barato} e ele custa R$: {menor_preco}')

print('Cadastro de produtos finalizado.')
