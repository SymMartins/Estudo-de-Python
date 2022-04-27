#Maior e menor valores
valor_um = int(input('Primeiro valor: '))
valor_dois = int(input('Segundo valor: '))
valor_tres = int(input('Terceiro valor: '))

#Verificando quem é menor:
menor = valor_um
if valor_dois < valor_um and valor_dois < valor_tres:
    menor = valor_dois
if valor_tres < valor_um and valor_tres < valor_dois:
    menor = valor_tres

#Verificando quem é maior:
maior = valor_um
if valor_dois > valor_um and valor_dois > valor_tres:
    maior = valor_dois
if valor_tres > valor_um and valor_tres > valor_dois:
    maior = valor_tres
print(f'O menor valor digitado foi {menor}')
print(f'O menor valor digitado foi {maior}')