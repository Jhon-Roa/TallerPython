import os

def AddPlayer(lstJugadores= dict):
    os.system('cls')
    print('Ingrese los datos del jugador que desea añadir')
    isValueTrue= True
    while isValueTrue:
        id = (str(input('ID :')))
        if id in lstJugadores['Novato'] or id in lstJugadores['Intermedio'] or id in lstJugadores['Avanzado']:
            print('el jugador ya se encuentra registrado')
            os.system('pause')
        else:
            isValueTrue= False
    nombre = str(input('Nombre :'))
    isValueTrue = True
    while isValueTrue:
        try:
            edad = int(input('Edad :'))
        except ValueError:
            print('el valor que ingresaste no es un entero')
        else:
            isValueTrue = False
    if edad < 15:
        print('No tiene la edad validad para ingredar al torneo')
        os.system('pause')
    elif edad >= 15 and edad <= 16:
        lstJugadores['Novato'].update({id: {'id': id, 'nombre': nombre, 'edad': edad, 'PJ': 0, 'PG': 0, 'PP': 0, 'PA': 0, 'TP': 0}})
    elif edad >= 17 and edad <= 20:
        lstJugadores['Intermedio'].update({id: {'id': id, 'nombre': nombre, 'edad': edad, 'PJ': 0, 'PG': 0, 'PP': 0, 'PA': 0, 'TP': 0}})
    elif edad > 20:
        lstJugadores['Avanzado'].update({id: {'id': id, 'nombre': nombre, 'edad': edad, 'PJ': 0, 'PG': 0, 'PP': 0, 'PA': 0, 'TP': 0}})
