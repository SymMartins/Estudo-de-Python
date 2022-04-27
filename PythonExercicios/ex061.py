'''refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando as 10 primeiros termos
da progressão usando a estrutura while'''

print('-=-' * 10)
print('PROGRESSÃO ARITIMÉTICA')
print('-=-' * 10)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}', end=' » ')
    termo += razao
    cont += 1
print('ACABOU')
