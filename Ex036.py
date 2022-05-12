# 036

valCasa = int(input('Qual o valor da casa? R$'))
salario = int(input('Qual salário do comprador? R$'))
tempo = int(input('Em quantos anos o comprador vai pagar? '))
prestacao = valCasa / (tempo * 12)

print(f'O valor da prestação é: R${prestacao:<.2f}')

if prestacao > salario * 0.30:
    print('O empréstimo foi negado porque a prestação excede 30% do salário do comprador.')
    
else:
    print('O empréstimo foi concedido!')