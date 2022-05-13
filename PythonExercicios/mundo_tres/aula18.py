"""Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves individuais."""

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[
:])  # Atenção para não esquecer os conchetes com os dois pontos ([:]) pois se não tiver será criada uma imagem e não uma cópia.
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

# -------------------------------------------------------------------------------------------------------------------
print('-=' * 30)

galera2 = [['joão', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade.')
# -------------------------------------------------------------------------------------------------------------------
print('-=' * 30)

print(galera2[2][1])
print(galera2[1][1])
print(galera2[0][0])

# -------------------------------------------------------------------------------------------------------------------
print('-=' * 30)

galera3 = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])  # lembrando que tem que colocar [:] para criar uma cópia da váriavel dados
    dado.clear()
print(galera3)
totmai = totmen = 0
for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
# -------------------------------------------------------------------------------------------------------------------
print('-=' * 30)
