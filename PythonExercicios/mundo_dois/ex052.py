'''FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO'''
numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {numero} foi divisível {total} vezes:')
if total == 2:
    print('Por isso ele É PRIMO')
else:
    print('Por isso ele NÃO é PRIMO')

