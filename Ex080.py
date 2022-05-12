# 080

lst = []
result = []

for i in range(0, 5):
    val = int(input('Valor: ')) 

    if i == 0 or val > lst[-1]:
        lst.append(val)
    else:
        pos = 0
        while pos < len(lst):
            if val <= lst[pos]:
                lst.insert(pos, val)
                break
            pos += 1

print ('-=' * 15)
print(f'Os valores digitados foram: {lst}')

