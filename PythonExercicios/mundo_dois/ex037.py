numero = int(input('Digite um número inteiro qualquer: '))
print('escolha uma opção [1] para binario, [2] para octal e [3] para hexadecimal: ')
opcao = input('Sua opção é: ')
binario = 1
octal = 2
hexadecimal = 3

if opcao == '1':
    opcao = format(numero, 'b')
    print(f'O numéro {numero} em sua forma binária é {opcao}')
elif opcao == '2':
    opcao = format(numero, 'o')
    print(f'O numero {numero} em sua forma octal é {opcao}')
elif opcao == '3':
    opcao = format(numero, 'X')
    print(f'O numero {numero} em sua forma hexadecimal é {opcao}')
else:
    print('Opção invalida, tente novasmente!')