# condição de pagamento
print('{:=^40}'.format(' LOJINHA DO SYM '))
valor_compra = float(input('Valor da compra R$: '))
forma_pagamento = int(input('''Formas de pagamento:
 (1) À Vista (cheque ou dinheiro)
 (2) À Vista Cartão
 (3) Até 2x no Cartão
 (4) 3x ou MAIS no Cartão
Escolha uma forma de pagamento: '''))

if forma_pagamento == 1:
    valor_compra_desconto = valor_compra - (valor_compra * 10 / 100)
    print('O valor da sua compra será de R$:{:.2f}'.format(valor_compra_desconto))
elif forma_pagamento == 2:
    valor_compra_desconto = valor_compra - (valor_compra * 5 / 100)
    print('O valor da sua compra será de R$:{:.2f}'.format(valor_compra_desconto))
elif forma_pagamento == 3:
    parcelas = valor_compra / 2
    print('Sua compra será parcelada em 2x de R$:{:.2f} com total de R$: {:.2f}'.format(parcelas, valor_compra))
elif forma_pagamento == 4:
    valor_compra_juros = valor_compra + (valor_compra * 20 / 100)
    total_parcelas = int(input('Quantas Parcelas? Máximo 10x: '))
    parcelas = valor_compra_juros / total_parcelas
    print('Sua compra será parcelada em {}x de R$:{:.2f} com JUROS dando o valor total de R$:{:.2f}'.format(total_parcelas, parcelas, valor_compra_juros))
else:
    print('ERRO! Forma de pagamento não indentificado!\nTENTE NOVAMENTE!')
