#Par ou Ímpar?
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2

if resultado == 0:
    print(f'O número {numero} é PAR!!')
else:
    print(f'o número {numero} é IMPAR')