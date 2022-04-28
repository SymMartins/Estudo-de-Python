valor = float(input('Quanto dinheiro você tem na carteira? R$: '))
dolar = 4.76
euro = 5.23
cambio_d = valor / dolar
cambio_e = valor / euro
print('Com R$: {:.2f} você consegue comprar US$: {:.2f}'.format(valor, cambio_d))
print('E com R$: {:.2f} você consegue comprar €: {:.2f}'.format(valor, cambio_e))