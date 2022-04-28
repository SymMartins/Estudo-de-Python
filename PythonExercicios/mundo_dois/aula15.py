"""Nessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código.
É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.
Além disso, vamos aprender como trabalhar com as novas fstrings do Python."""
#Ex de um while com loop infinito e parado pelo break
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

"""nome = 'pedro'
idade = 25
peso = 59.6

print(f'O {nome:-^20} tem {idade} e pesa {peso:.2f}')
EX: de formatação com f.
obs: números deve ser transformados em (int) ou (float)
"""

