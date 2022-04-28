valor_produto = float(input('Valor do produto a vista R$: '))
forma_pagamento = (input('Forma de pagamento Dinheiro ou Prazo? '.lower()))
percentual = 15 / 100
pagamento_dinheiro = valor_produto - (percentual * valor_produto)
pagamento_prazo = valor_produto + (percentual * valor_produto)
dinheiro = pagamento_dinheiro
prazo = pagamento_prazo

if forma_pagamento == 'dinheiro':
    print(f'O Valor a ser cobrado será de R$:{pagamento_dinheiro}')
else:
    print(f'O Valor a ser cobrado será de R$:{pagamento_prazo}')

