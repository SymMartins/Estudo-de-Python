''' Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. o programa encerra quando
ele disser que quer mostrar 0 termos'''

print('-=-' * 10)
print('PROGRESSÃO ARITIMÉTICA - V3')
print('-=-' * 10)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('digite a razão da PA: '))
termo = primeiro
cont = 1
total_termos = 0
mais = 10
while mais !=0:
    total_termos = total_termos + mais
    while cont <= total_termos:
        print(f'{termo}', end=' » ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progreção terminada com {total_termos} termos ao todo:')
