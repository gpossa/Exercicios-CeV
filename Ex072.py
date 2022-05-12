# 072

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
             'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 
             'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 
             'Dezenove', 'Vinte')
num = 0

while True:
    try:
        num = int(input('Digite um número entre 0 e 20: '))
    except ValueError:
        continue
    if num < 0 or num > 20:
        continue
    break

print(f'Este número por extenso é: {contagem[num]}')

