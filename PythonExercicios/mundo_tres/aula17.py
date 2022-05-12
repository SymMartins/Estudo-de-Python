"""Lista parte 1. Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves individuais."""

num = [2, 5, 9, 1]
#Adicionando elementos na lista
num[2] = 3 #modifica o conteúdo da lista
num.append(7) #adiciona um valor na lista
num.sort() #coloca o conteúdo da lista em ordem crescente
#num.sort(reverse=True) #coloca o conteúdo da lista em ordem decresente
num.insert(2, 2) #insere um conteúdo na lista (2 = posição, 0 = valor)

"""#Remoção de elementos na lista num.pop() #remove o ultimo elemento (se adicionar um valor dentro do () vai remover o 
elemento da posição ex num.pop(2) num.remove(2) #Remove o primeiro elemento que ele encontrar na lista ex. 
num.remove(2) ele irá remover o primeiro elento 2"""

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4!')

print(num)
print(f'Essa lista tem {len(num)} elementos') #A função LEN retorna quantos elementos tem em uma lista

# --------------------- Outra forma de fazer lista --------------------------------------------------------------------
print('-'*35)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor ')))

for v in valores:
    print(f'{v}...', end=' ')
print('\n' + '-'*35)

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')

print('-'*35)

# ---------------------------- Peculiaridade do Python nas listas -----------------------------------------------------

a = [2, 3, 4, 7]
b = a[:] # Cria uma cópia da lista A dentro da lista B assim se modificar o numero 8 ele aparecerá no B e na lista A aparecerá o 4
#b = a #ligação entre as listas A e B
b[2] = 8 #Ligação entre as duas listas o numero 8 aparecerá na lista A e na B
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# quanto iguala uma lista com a outra o Python cria uma ligação entre elas