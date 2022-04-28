salario = int(input('Qual o salário do funcionário? '))
#modo um:

aumento_um = salario + (salario * 15/100)
aumento_dois = salario + (salario * 10/100)
if salario <= 1250:
    print(f'O salário passará de R$:{salario} para R$:{aumento_um}')
else:
    print(f'O salário passará de R$:{salario} para R$:{aumento_dois}')

#modo dois:

"""if salario <= 1250:
    novo_salario = salario + (salario * 15 / 100)
else:
    novo_salario = salario + (salario * 10 / 100)
print(f'Quem ganhava R$:{salario} passará a ganhar R$:{novo_salario} agora')"""