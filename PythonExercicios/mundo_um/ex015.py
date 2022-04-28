dias_alugado = int(input('Quantos dias o carro ficou alugado? '))
km_rodados = float(input('Quantos Km foram rodados? '))
valor_aluguel = dias_alugado * 60
valor_km = km_rodados * 0.15
valor_total = valor_aluguel + valor_km
print('O total a pagar pelo aluguel do carro é de R$:{:.2f}'.format(valor_total))