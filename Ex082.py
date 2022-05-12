# 082

lst, lst2, lst3 = [], [], []

while True:
    val = int(input('Valor: '))
    lst.append(val)

    conf = str(input('Continuar? [S/N] ')).strip().lower()[0]
    if conf == 'n':
        break

for num in lst:
    if num % 2 == 0:
        lst2.append(num)
    else:
        lst3.append(num)

print(lst)
print(lst2)
print(lst3)

