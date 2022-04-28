# Formar um triângulo

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
lado_a = float(input('Primeiro Segmemto: '))
lado_b = float(input('Segundo Segmento: '))
lado_c = float(input('Terceiro segmento: '))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print('Os Segmentos acima PODEM FORMAR um triângulo,', end= '')
    if lado_a == lado_b == lado_c:
        print(' no qual é um triângulo EQUILATERO')
    elif lado_a != lado_b != lado_c != lado_a:
        print(' no qual é um triângulo ESCALENO')
    else:
        print(' no qual é um triângulo ISÓCELES')
else:
    print('O segmentos acima NÃO PODEM FORMAR um triângulo')
