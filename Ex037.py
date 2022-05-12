# 037

num = int(input('Digite um número inteiro: '))
convType = int(input('Qual será a base de conversão? \n(1) Binário \ (2) Octal \ (3) Hexadecimal: '))

if convType == 1:
    print(f'Resultado: {bin(num)[2:]}')

elif convType == 2:
    print(f'Resultado: {oct(num)[2:]}')
    
else:
    print(f'Resultado: {hex(num)[2:]}')
