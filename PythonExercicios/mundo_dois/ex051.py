''' DESENVOLVA UM PROGRAMA QUE LEIA PRIMEIRO TERMO E A RAZÃO DE UMA (PA) PROGRESSÃO ARITIMETICA. NO FINAL
MOSTRA OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO'''

print('=' * 23)
print('PROGRESSÃO ARITIMÉTICA - V1')
print('=' * 23)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('digite a razão: '))
decimo = termo + (10 - 1) * razao
for progressao in range(termo, decimo + razao, razao):
    print(f'{progressao}', end=' » ')
print('ACABOU')
