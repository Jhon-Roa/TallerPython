import os

def Menu():
    os.system('cls')
    titulo= """"
    **************************
    * GESTION DE INVENTARIOS * 
    ************************** 
    """
    print(titulo)

    menuOp= """
    1. Agregar producto
    2. lista de productos
    3. Actualizar stock
    4. informe de productos criticos
    5. calculo de ganancia potencial
    6. salir
    """
    print(menuOp)
    try:
        op= int(input(')_'))
    except ValueError:
        print('debes ingresar un numero entero')
        os.system('pause')
        Menu()
    else:
        if op < 1 and op >6:
            print('el numero debe estar entre 1 y 6')
            os.system('pause')
        else:
            return op
