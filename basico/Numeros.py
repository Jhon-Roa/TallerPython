import os

print('algoritmo que ingresa numeros enteros positivos e imprime un reporte, si este es negativo :')
dictNumeros= {
    'totalNumeros': [],
    'totalPares': [],
    'totalImpar': [],
    'promedioPares': 0.0,
    'promedioImpar': 0.0,
    'menor10': [],
    '20-50': [],
    'mayor100': []
}

numeroValid = True
while numeroValid:
    try:
        n= int(input('ingrese la cantidad de numeros que desea ingresar :'))
    except ValueError:
        print('debe ingresar un numero valido')
        os.system('pause')
    else:
        numeroValid= False
        
        for i in range(0, n):
            os.system('cls')
            numeroValid= True
            while numeroValid:
                try:
                    numero = int(input('ingrese un numero :'))
                except ValueError:
                    print('ingrese un numero entero')
                    os.system('pause')
                else:
                    numeroValid=False
                dictNumeros['totalNumeros'].append(numero)
                
                if numero % 2 == 0:
                    dictNumeros['totalPares'].append(numero)
                else:
                    dictNumeros['totalImpar'].append(numero)

                if dictNumeros['totalPares']:
                    promedioP = sum(dictNumeros['totalPares']) / len(dictNumeros['totalPares'])
                    dictNumeros['promedioPares']= promedioP
                
                if dictNumeros['totalImpar']:
                    promedioI = sum(dictNumeros['totalImpar']) / len(dictNumeros['totalImpar'])
                    dictNumeros['promedioImpar']= promedioI
                
                if numero < 10:
                    dictNumeros['menor10'].append(numero)
                elif numero >= 20 and numero <= 50:
                    dictNumeros['20-50'].append(numero)
                elif numero > 100:
                    dictNumeros['mayor100'].append(numero)
                    
                if numero < 0:
                    lenNumeros = len(dictNumeros['totalNumeros'])
                    print(f'1. el total de numeros ingresados es {lenNumeros}')
                    lenNumeros = len(dictNumeros['totalPares'])
                    print(f'2. el total de numeros pares es {lenNumeros}')
                    print(f'3. el promedio de los numeros pares es {round(dictNumeros["promedioPares"], 2)}')
                    print(f'4. el promedio de los numeros impares es {round(dictNumeros["promedioImpar"], 2)}')
                    a= len(dictNumeros["menor10"])
                    print(f'5. la cantidad de numeros menores a 10 es {a}')
                    b= len(dictNumeros["20-50"])
                    print(f'6. la cantidad de numeros entre 20 y 50 es {b}')
                    c= len(dictNumeros["mayor100"])
                    print(f'7. la cantidad de numeros mayores a 100 es {c}')
                    os.system('pause')
                    
lenNumeros = len(dictNumeros['totalNumeros'])
print(f'1. el total de numeros ingresados es {lenNumeros}')
lenNumeros = len(dictNumeros['totalPares'])
print(f'2. el total de numeros pares es {lenNumeros}')
print(f'3. el promedio de los numeros pares es {round(dictNumeros["promedioPares"], 2)}')
print(f'4. el promedio de los numeros impares es {round(dictNumeros["promedioImpar"], 2)}')
a= len(dictNumeros["menor10"])
print(f'5. la cantidad de numeros menores a 10 es {a}')
b= len(dictNumeros["20-50"])
print(f'6. la cantidad de numeros entre 20 y 50 es {b}')
c= len(dictNumeros["mayor100"])
print(f'7. la cantidad de numeros mayores a 100 es {c}')
            