"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

valores = list()

# 1.º cadastra valores númericos em uma lista:
while True:
    numero = (int(input('Digite um valor: ')))
    # 2.º Se tiver números repetidos não poderar ser adicionado:
    if numero not in valores:
        valores.append(numero)
    else:
        print('Valor duplicado! Não vou adiciona-lo...')

    # 3.º Exibir todos os valores únicos cadastrados em ordem crescente:
    valores.sort()

    # 5.º Sai do programa e mostra o resultado
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if sair == 'N':
        break

print('-=' * 30)
print(f'Você digitou os valores: {valores}.')
# fim do programa!
