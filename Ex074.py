# 074

from random import randint

nums = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Números gerados: {nums}')
print(f'Menor número: {sorted(nums)[0]}')
print(f'Maior número: {sorted(nums)[-1]}')