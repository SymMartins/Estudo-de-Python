largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2

print('Sua parede tem a dimensão de L: {} x A: {} e a sua área é de {} m²'.format(largura, altura, area))
print('Para pintar sua parede, você presisará de {}L de tinta.'.format(tinta))