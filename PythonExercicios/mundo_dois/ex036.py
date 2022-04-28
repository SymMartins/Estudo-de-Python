#Aprovando Empréstimo

valor_casa = float(input('Valor da Casa: R$: '))
valor_salario = float(input('Salário do comprador: R$: '))
financiamento = int(input('Quantos anos de financiamento? '))

prestacao = valor_casa / (financiamento * 12)
prestacao_minima = valor_salario * 30 / 100

if prestacao <= prestacao_minima:
    print('Para pagar uma casa de R$:{:.2f} em {} anos a prestação será de R$:{:.2f}'.format(valor_casa, financiamento, prestacao))
    print('Empréstimo APROVADO')
else:
    print('Para pagar uma casa de R$:{:.2f} em {} anos a prestação será de R$:{:.2f}'.format(valor_casa, financiamento, prestacao))
    print('Empréstimo REPROVADO')