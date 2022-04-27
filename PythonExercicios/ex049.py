'''REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR'''


numero = int(input('Digite o número para ver sua tabuada: '))
#Forma feita por mim!
'''multiplicador = 0
print('=' * 11)
for tabuada in range(1, 11):
    resultado = numero * tabuada
    multiplicador += 1
    print(f'{numero} x {multiplicador} = {resultado}')
print('=' * 11)'''
#Forma do Prof. Guanabara
print('=' * 11)
for contador in range(1,11):
    print('{} x {:2} = {}'. format(numero, contador, numero * contador))
print('=' * 11)