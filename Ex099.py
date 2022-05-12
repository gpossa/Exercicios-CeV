# 099

from time import sleep

def maior(*nums):
    print('-=' * 20)
    print('Analisando os valores passados.')

    maiorNum = 0

    for i in nums:
        print(i, end=' ', flush=True)
        sleep(0.5)
        
        if i > maiorNum:
            maiorNum = i

    print(f'Foram informados {len(nums)} valores ao todo.')

    print(f'O maior valor foi {maiorNum}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7 ,0)
maior(1, 2)
maior(6)
maior()