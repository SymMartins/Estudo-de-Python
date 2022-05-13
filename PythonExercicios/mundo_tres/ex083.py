"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

# 1.º Entrada da expressão:
exprecao = str(input('Digite sua expressão: '))

# 2.º Analise da expressão:
pilha = []
for simb in exprecao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

# 3.º Resultado da expressão:
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
