'''melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. o programa encerra quando
ele disser que quer mostrar 0 termos'''


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