#Radar eletrônico v 2.0
velocidade = float(input('Qual a velocidade do carro: '))
limite = 110
velocidade_minima = limite / 2
multa = 85.13

if velocidade < velocidade_minima:
    print(f'Você está abaixo do limite de velocidade que é {velocidade_minima}KM/h\nE você poderá ser multado!!')
    print(f'De acordo com o artigo 219 do Código de Trânsito Brasileiro que diz:\nTransitar com o veículo em velocidade inferior à metade da velocidade máxima,\n(salvo se estiver na faixa da direita), constitui em infração média, sujeita a multa de R$: {multa}')

elif velocidade > limite:
    print(f'Você foi multado!!! Você excedeu o limite permitido que é de {limite}Km/h')
    multa_velocidade_maxima = (velocidade - limite) * 7
    print(f'Você pagará uma multa de R$:{multa_velocidade_maxima}')

else:
    print(f'Sua velocidade é {velocidade}KM/h, e está dentro do limite de velocidade')