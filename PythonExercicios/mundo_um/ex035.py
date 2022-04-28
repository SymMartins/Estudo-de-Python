#Analisando Triângulo v1.0

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
lado_a = float(input('Primeiro Segmemto: '))
lado_b = float(input('Segundo Segmento: '))
lado_c = float(input('Terceiro segmento: '))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print('Os Segmentos acima PODEM FORMAR um triângulo')
else:
    print('O segmentos acima NÃO PODEM FORMAR um triângulo' )