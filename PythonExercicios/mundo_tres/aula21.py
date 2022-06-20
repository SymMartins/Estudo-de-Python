"""Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python,
escopo de variáveis e retorno de resultados."""


def lin():
    print('-=' * 30)

def contador(i, f, p):
    """
    ===>> Faz uma contagem e mostra na tela
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('fim')

contador(2, 10, 2)
help(contador)

lin()
print(' ===> PARÂMETROS OPCIONAIS <=== ')
lin()

def somar(a=0, b=0, c=0):  # 0 é um parâmetro opcional, assim se informar sómente 1 ou 2 parâmetros não vai dar erro
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)
somar(b=4, c=2)
somar(c=2, a=4)

lin()
print(' ===> ESCOPO DE VARIÁVEIS <=== ')
lin()

def teste():
    x = 8  # A variável X só vai funcionar dentro da função TESTE e ela é chamada de escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa principal
n = 2  # A variável N vai funcionar tanto na função TESTE quanto fora, e ela é chamada de escopo global

print(f'No Programa principal, n vale {n}')
teste()
# print(f'No programa principla, x vale {x}') RETORNA ERRO POIS A VARIÁVEL X PERTENCE A FUNÇÃO TESTE

lin()
def teste2(b):
    # global a, transforma o A local em A global
    a = 8  # A = Scopo local
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')  # Scopo local
    print(f'C dentro vale {c}')  # Scopo local

# programa principal
a = 5  # com o comando global o numero 5 se transforma em 8
teste2(a)  # Scopo Global
print(f'A fora vale {a}')

lin()
print('===> RETORNO DE VALORES <===')
lin()

def somar(a= 0, b=0, c=0):
    s = a + b + c
    #  print(f'A soma vale {s}')
    return s

# somar(3, 2, 5)
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')

lin()
print(' ===> AULA PRATICA <=== ')
lin()

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

"""n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')"""

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')

lin()

def parOuImpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if parOuImpar(num):
    print('É par!')
else:
    print('Não é par!')
lin()