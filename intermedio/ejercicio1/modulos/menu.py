import os

def menu():
    lstOpciones= [1, 2, 3, 4, 5]
    menuOP= """
    1- Registrar ciudad 
    2- Registrar sismo
    3- Buscar sismos por ciudad
    4- informe de riesgo 
    5- salir
    """
    os.system('cls')
    print(menuOP)
    print('ingrese la opcion a elegir')
    try:
        op= int(input(')_'))
    except ValueError:
        print('ingrese un valor valido')
        os.system('pause')
        menu()
    else:
        if op in lstOpciones:
            return op
        else:
            print('el numero debe estar en el menu de opciones')
            os.system('cls')
            menu()