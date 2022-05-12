# 052

num = int(input('Digite um número: '))
mult = 0

for index in range(2, num):
    if num % index == 0:
        print(f'Multiplo de {index}')
        mult += 1

if mult == 0:
    print("É primo")