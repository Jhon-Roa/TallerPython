import os

isNumberInt = True
while isNumberInt:
    os.system('cls')
    try:
        whileNro1= True
        while whileNro1:
            os.system('pause')
            nro1 = int(input('ingrese 3 numeros :'))
            nro2 = int(input(')_'))
            nro3 = int(input(')_'))
            if nro1 >= 0 and nro2 >= 0 and nro3 >= 0:
                whileNro1= False
            else:
                print('todos los numeros deben ser positivos')
                os.system('pause')
    except ValueError:
        print('Ingrese un numero entero')
        os.system('pause')
    else:
        suma = nro1 + nro2 + nro3
        isNumberInt= False
        print(f'la suma de los tres numeros es {suma}')

