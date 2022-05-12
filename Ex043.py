# 043

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / altura**2

if imc < 18.5:
    print(f'IMC {imc:<.1f}: Você está abaixo do seu peso ideal.')

elif imc > 18.5 and imc < 25:
    print(f'IMC {imc:<.1f}: Você está no seu peso ideal.')

elif imc > 25 and imc < 35:
    print(f'IMC {imc:<.1f}: Você está acima do seu peso ideal (sobrepeso).')

elif imc > 30 and imc < 40:
    print(f'IMC {imc:<.1f}: Você está acima do seu peso ideal (obeso).')
    
else:
    print(f'IMC {imc:<.1f}: Você está acima do seu peso ideal (obesidade mórbida).')