# 078

lst, menorPos, maiorPos = [], [], []

for i in range(0, 5):
    val = int(input(f'Digite o valor {i}: '))
    lst.append(val)

for idx, num in enumerate(lst):
    if num == max(lst):
        maiorPos.append(idx)
    elif num == min(lst):
        menorPos.append(idx)

print('-=' * 15)
print(f'Você digitou os nº: {lst}')
print(f'O maior nº foi: [{max(lst)}] | Posição {maiorPos}')
print(f'O menor nº foi: [{min(lst)}] | Posição {menorPos}')