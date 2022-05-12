"""Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, mostre:
        A) Quantos números foram digitados.
           B) A lista de valores, ordenada de forma decrescente.
              C) Se o valor 5 foi digitado e está ou não na lista."""
# 1.º Criar uma lista:
numeros = list()
# 2.º Pedir ao usuário para inserir vários números:
while True:
    valor = int(input('Digite um valor: '))
    # 3.º Inserindo o valor na lista:
    numeros.append(valor)

    # 7.º Sai do programa e mostra o resultado:
    sair = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if sair == 'N':
        break

print('-=' * 30)

# 4.º Somar quantos números foram digitados:
print(f'Foram adicionados na lista {len(numeros)} valores.')

# 5.º Ordenar a lista em forma decrescente:
numeros.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente {numeros}')

# 6.º Verificar se o número 5 esta ou não na lista:
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
