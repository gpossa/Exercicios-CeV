# 064

index, count, resultado = 0, 0, 0

while index != 999:
    index = int(input('Digite um número [999 para parar]: '))
    
    if index != 999:
        count += 1
        resultado += index

print(f'Foram digitados {count} números, e a soma de todos eles é {resultado}')




    