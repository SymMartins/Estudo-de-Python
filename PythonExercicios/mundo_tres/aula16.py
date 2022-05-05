"""Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python.
As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves individuais."""

# tuplas são IMUTÁVEIS (não pode ser modificadas)
# lanche[1] = 'refrigerante' (comando ERRADO)

lanche = ('amburgue', 'suco', 'pizza', 'pudim', 'Batata Frita')
print('='*55)
print('Primeiro (FOR)')
for cont in range(0, len(lanche)):
    print(cont)
print('=' * 130)
# Segundo FOR e o terceiro terão o mesmo resultado (escolha a critério do programador) porém às vezes só sairá o resultado com o TERCEIRO FOR
print('Segundo (FOR)')
for comida in lanche:
    print(f'eu vou comer {comida},') #o modo mais simplis sem colocar a posição!
print('=' * 130)
print('Terceiro (FOR)')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('=' * 130)
print('Quarto (FOR)')
for pos, comida in enumerate(lanche): #Dá a posição de cada item na tupla!
    print(f'Eu vou comer {comida} na posição {pos}')

print('=' * 130)
print('comi pra caramba!')
print('='* 130)
print('='*55)
print(sorted(lanche)) #sorted é para colocar em ordem! (não altera a Tupla apenas coloca em ordem)
print('='*55)
print(lanche)
print('='*55)
print(lanche[0])
print('='*55)
print(lanche[1])
print('='*55)
print(lanche[-2])
print('='*55)
print(lanche[1:3])
print('='*55)
print(lanche[2:])
print('='*55)
print(lanche[:2])
print('='*55)
print(lanche[-3:])
print('='*55)
