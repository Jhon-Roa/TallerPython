import os

def AddSismo(ciudades= list):
    for idx, ciudad in enumerate(ciudades):
        isValueTrue = True
        while isValueTrue:
            os.system('cls')
            try:
                intensidad= float(input(f'ingrese la intensidad del sismo en la ciudad {ciudad} :'))
            except ValueError: 
                print('ingrese un numero entero o real')
                os.system('pause')
            else:
                ciudades[idx][1].append(intensidad)
                isValueTrue = False
                

def IgualarSismos(ciudades= list):
    sismos = max(ciudades, key=lambda x: len(x[1]))
    sismos= len(sismos[1])
    
    for idx, ciudad in enumerate(ciudades):
        if len(ciudades[idx][1]) == sismos:
            pass
        else:
            for i in range (0,sismos):
                isValueTrue = True
                while isValueTrue:
                    try:
                        Faltante= float(input(f'ingrese la intensidad del sismo {i+1}'))
                    except ValueError:
                        print('tienes que ingresar un numero')
                    else:
                        isValueTrue= False
                ciudades[idx][1].append(Faltante)
    os.system('pause')
