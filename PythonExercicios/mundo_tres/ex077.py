"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

# 1º Tupla com várias palavras sem usar acentos.
palavras = ('casa', 'carro', 'apartamento', 'estacionamento', 'amizade',
            'pessoas', 'amor', 'motocicleta', 'viagem', 'python',
            'estudar', 'foco', 'ajudar', 'gratis')
# 2º Mostra quais são as vogais de cada palavra.
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()}, temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')