import os

os.system('cls')
print('Calculadora de Indice De Masa Corporal (IMC)')
nombre = str(input('por favor ingrese su nombre :'))
isValueTrue = True
while isValueTrue:
    try:
        edad = int(input('por favor ingrese su edad :'))
    except ValueError:
        print('ingrese una edad valida')
    else:
        isValueTrue = False
isValueTrue= True
while isValueTrue:
    try:
        peso = float(input('por favor ingrese su peso :'))
    except ValueError:
        print('ingrese una edad valida')
    else:
        isValueTrue = False
isValueTrue= True
while isValueTrue:
    try:
        altura = float(input('por favor ingrese su altura :'))
    except ValueError:
        print('ingrese una edad valida')
    else:
        isValueTrue = False

imc = peso/altura**2
imc = round(imc, 2)

if imc < 18.5:
    bajoPeso =(f'el estudiante con nombre: {nombre}, edad: {edad} y IMC: {imc}:')
    print(bajoPeso)
    print(f'tiene un bajo peso')
elif imc >= 18.5 and imc <= 24.9:
    pesoIdeal = (f'el estudiante con nombre: {nombre}, edad: {edad} y IMC: {imc}:')
    print(pesoIdeal)
    print(f'tiene un peso normal')
elif imc >= 25 and imc <= 29.9:
    print(f'el estudiante con nombre: {nombre}, edad: {edad} y IMC: {imc}:')
    print(f'tiene obesidad tipo I')
elif imc >= 30 and imc <= 34.9:
    print(f'el estudiante con nombre: {nombre}, edad: {edad} y IMC: {imc}:')
    print(f'tiene obesidad tipo II')
elif imc >= 40:
    print(f'el estudiante con nombre: {nombre}, edad: {edad} y IMC: {imc}:')
    print(f'tiene obesidad tipo III')