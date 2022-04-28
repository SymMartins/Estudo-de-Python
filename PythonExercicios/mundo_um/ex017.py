# Catetos e Hipotenusa
# modo de fazer 1

'''
cateto_oposto = float(input('Comprimento do catete oposto: '))
catete_adjacente = float(input('Comprimento do catete adjacente: '))
hipotenusa = (cateto_oposto ** 2 + catete_adjacente ** 2) ** (1/2)
print('A hipotenusa do triangulo vai medir: {:.2f}'.format(hipotenusa))
'''

# modo de fazer 2
# importando a biblioteca math

import math
cateto_oposto = float(input('Comprimento do catete oposto: '))
catete_adjacente = float(input('Comprimento do catete adjacente: '))
hipotenusa = math.hypot(cateto_oposto, catete_adjacente)
print('A hipotenusa do triangulo vai medir: {:.2f}'.format(hipotenusa))