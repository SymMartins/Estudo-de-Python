#média da nota

nota_um = float(input('Digite a primeira nota: '))
nota_dois = float(input('Digite a segunda nota: '))
media = float((nota_um + nota_dois) / 2)
print(f'Tirando {nota_um} e {nota_dois}, a média do aluno é {media}')

if media < 5:
    print('Você foi REPROVADO!')
elif 6.9 > media >= 5:  #media >= 5 and media < 7:
    print('Você está de RECUPERAÇÃO')
else:
    print('Você foi APROVADO!')
