import os

def Menu():
    os.system('cls')
    titulo= """"
    ************************
    * CONSUMO DE CO2 * 
    ************************ 
    """
    print(titulo)

    menuOp= """
    1. Agregar dependencia
    2. Registrar consumo de dependencia
    3. Ver CO2 producido
    4. Dependencia que produce mayor CO2
    5. salir
    """
    print(menuOp)
    try:
        op= int(input(')_'))
    except ValueError:
        print('debes ingresar un numero entero')
        os.system('pause')
        Menu()
    else:
        if op < 1 and op >5:
            print('el numero debe estar entre 1 y 5')
            os.system('pause')
        else:
            return op