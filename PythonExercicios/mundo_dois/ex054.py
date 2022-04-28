'''CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO
ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES'''
from datetime import date
totmaior = 0
totmenor = 0
for c in range(1,8):
    ano = int(input(f'Digite o ano de nascimento da {c}º pessoa: '))
    idade = date.today().year - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo são {totmaior} maiores de idade')
print(f'E também tivemos {totmenor} menores de idade')


