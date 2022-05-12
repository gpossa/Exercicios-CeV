# 075

nums = (int(input('Digite um número: ')), 
        int(input('Digite mais um número: ')), 
        int(input('Digite mais um número: ')), 
        int(input('Digite mais um número: ')),)
        
print(f'O número 9 apareceu {nums.count(9)} vezes.')

if 3 in nums:
    print(f'O número 3 apareceu na {nums.index(3) + 1}º posição')
else:
    print(f'O número 3 não apareceu nenhuma vez')

print('Os valores pares digitados foram: ', end='')

for index in nums:
    if index % 2 == 0:
        print(index, end='')