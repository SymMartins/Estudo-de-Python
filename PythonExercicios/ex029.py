#Radar eletrônico
velocidade = float(input('Digite uma velocidade: '))
limite = 80
if velocidade > limite:
    print(f'Você foi multado!!! Você excedeu o limite permitido que é de {limite}Km/h')
    multa = (velocidade-limite) * 7
    print(f'Você deve pagar uma multa de R$:{multa}')
else:
    print('Tenha um bom dia!! Dirija com segurança')

