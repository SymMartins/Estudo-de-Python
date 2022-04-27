salario_atual = float(input('Qual é o valor do salário atual? R$: '))
aumento = float(input('Qual o percentual de almento '))
percentual = aumento / 100
novo_salario = salario_atual + (percentual * salario_atual)
print('O funcionário recebia R$:{:.2f}, com um aumento de: {}%, passou a receber R$: {:.2f}'.format(salario_atual, (percentual * 100), novo_salario))