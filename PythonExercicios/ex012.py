valor_produto = float(input('Qual o preço do produto? R$: '))
desconto = float(input('Qual o percentual de desconto? '))
percentual = desconto / 100
valor_desconto = valor_produto - (percentual * valor_produto)
print('O produto que custava R$:{:.2f}, na promoção com desconto de {}% vai custar R$:{:.2f}'.format(valor_produto, desconto, valor_desconto))