# 083

equac = input('Digite a equação: ').replace(' ', '')
 
abertoCount, abertoIdx, fechadoCount = 0, 0, 0
charsLst = list(equac)
print(charsLst)

for idx, char in enumerate(charsLst):
    if char == '(':
        abertoCount += 1
        abertoIdx = idx
    elif char == ')' and idx > abertoIdx:
        fechadoCount += 1
    
if abertoCount != fechadoCount:
    print('A expressão não é válida.')
else:
    print('A expressão é válida.')