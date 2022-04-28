'''FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFICIO, INDO DE 10 ATÉ 0,
COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES'''

from time import sleep
import emoji

fogos = emoji.emojize(':collision:')
for contagem in range(10, -1, -1):
    print(contagem)
    sleep(1)
print(fogos * 10)
