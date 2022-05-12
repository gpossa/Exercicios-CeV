# 044

preco = float(input('Digite o preço do produto: '))
pagamento = int(input('Selecione a opção de pagamento: \n(1) À vista no dinheiro ou cheque; \n(2) A vista no cartão; \n(3) Até 2x no cartão; \n(4) 3x ou mais no cartão:.\n'))

if pagamento == 1:
    precoFinal = preco - (preco * 0.10)
    print(f'Opção escolhida: À vista no dinheiro ou cheque. \nO preço final será R${precoFinal:<.2f}')
    
elif pagamento == 2:
    precoFinal = preco - (preco * 0.05)
    print(f'Opção escolhida: A vista no cartão. \nO preço final será R${precoFinal:<.2f}')

elif pagamento == 3:
    print(f'Opção escolhida: Até 2x no cartão. \nO preço final será R${preco}')

else: 
    precoFinal = preco + (preco * 0.2)
    print(f'Opção escolhida: 3x ou mais no cartão. \nO preço final será R${precoFinal:<.2f}')