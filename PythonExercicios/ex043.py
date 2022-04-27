#Calcular o imc:
altura = float(input('Digite sua ALTURA (M): '))
peso = float(input('Digite seu PESO (Kg): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.1f} e você está abaixo do peso!'.format(imc))
elif 18.5 <= imc < 24.9:
    print('Seu IMC é {:.1f} e você está com o peso normal!'.format(imc))
elif 24.9 <= imc < 29.9:
    print('Seu IMC é {:.1f} e você está acima do peso (SOBREPESO)'.format(imc))
elif 29.9 <= imc < 34.9:
    print('Seu IMC é {:.1f} e você está acima do peso (OBESIDADE I)'.format(imc))
elif 34.9 <= imc < 39.9:
    print('Seu IMC é {:.1f} e você está acima do peso (OBESIDADE II)'.format(imc))
else:
    print('Seu IMC é {:.1f} e você está acima do peso (OBESIDADE III)'.format(imc))





"""abaixo de 18.5 = abaixo do peso
    entre 18.5 e 25 =  peso ideal
        de 25 a 30 = sobrepeso
            30 a 40 = obesidade
                acima de 40 = obesidade mórbida"""
