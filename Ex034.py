# 034

salario = float(input('Qual é o salário inicial? R$'))

if salario <= 1250:
    aumento = salario * 0.15
    print(f'O aumento do salário será de R${aumento:<.2f}. Total R${aumento + salario:<.2f} ')
    
else:
    aumento = salario * 0.10
    print(f'O aumento do salário será de R${aumento:<.2f}. Total R${aumento + salario:<.2f} ')