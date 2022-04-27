#Jogo da Adivinhação v.1.0
from random import randint
from time import sleep #Sleep serve para criar um retardo na resposta do computador!
print('\033[34m-=--=\033[m'*20)
print('\033[32mVou pensar em um número entre\033[m 0 \033[32me\033[m 5\033[32m.\033[m \033[32mTente Adivinhaa...\033[m')
print('\033[34m-=--=\033[m'*20)

numero = int(input('Em que numero eu pensei? ')) # Número do jogador
numero_pensado = randint(0,10) # Gera um número aleatório entre 0 e 5
print('\033[31mProcessando...\033[m')
sleep(2) #Dentro do () coloca-se o tempo em segundo do aguardo!
if numero_pensado == numero:
    print(f'Você ganhou eu realmente pensei no numero: {numero}')
else:
    print(f'GANHEI!! Eu pensei no número {numero_pensado}, e não no {numero}!')
print('--FIM DE JOGO--')
