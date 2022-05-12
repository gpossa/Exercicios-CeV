# 023

numero = input('Digite um número entre 0 e 9999: ')
numeroFinal = '000' + numero

print(f'Unidade: {numeroFinal[-1]} \nDezena: {numeroFinal[-2]} \nCentena: {numeroFinal[-3]} \nMilhar: {numeroFinal[-4]} ')