#Custo da Viagem
# 1ª forma de fazer

distancia = float(input('Qual é a distância de sua viagem? '))
print('Você está preste a começar uma viagem de {}KM'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da passagem será de R$:{:.2f}'.format(preco))


# 2ª forma de fazer

"""distancia = float(input('Qual é a distância de sua viagem? '))
print('Você está preste a começar uma viagem de {}KM'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da passagem será de R$:{:.2f}'.format(preco))"""

# 3ª forma de fazer

"""distancia = float(input('Qual é a disância da sua viagem? '))
tarifa_longa = distancia * 0.45
tarifa_curta = distancia * 0.50
if distancia >= 200:
    print(f'Você está preste a começar uma viagem de {distancia}KM\nE o preço da passagem será de R$:{tarifa_longa}')
else:
    print(f'Você está preste a começar uma viagem de {distancia}KM\nE o preço da passagem será de R$:{tarifa_curta}')"""