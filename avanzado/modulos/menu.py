import os

def Menu():
    os.system('cls')
    titulo= """
        ++++++++++++++++++++++++
        + TORNEO TENIS DE MESA +
        ++++++++++++++++++++++++
    """
    print(titulo)
    opciones = """
    1. Registrar jugador
    2. Torneo Novato
    3. Torneo Intermedio
    4. Torneo Avanzado
    5. Salir
    """
    print(opciones)
    try:
        op = int(input(')_'))
    except ValueError:
        print('el valor que estas ingresando no es entero')
        os.system('pause')
        Menu()
    else:
        if op < 1 and op > 5:
            print('la opcion debe estar en el menu')
            os.system('pause')
        else:
            return op

def MenuNovatos():
    os.system('cls')
    titulo= """
        ++++++++++++++++++
        + Torneo Novatos +
        ++++++++++++++++++
    """
    print(titulo)
    opciones = """
    1. Jugar Torneo
    2. tabla Novatos
    3. Ganador Torneo
    4. Salir
    """
    print(opciones)
    try:
        op = int(input(')_'))
    except ValueError:
        print('el valor que estas ingresando no es entero')
        os.system('pause')
        MenuNovatos()
    else:
        if op < 1 and op > 4:
            print('la opcion debe estar en el menu')
            os.system('pause')
            MenuNovatos()
        else:
            return op 
        
def MenuIntemedio():
    os.system('cls')
    titulo= """
        +++++++++++++++++++++
        + Torneo Intermedio +
        +++++++++++++++++++++
    """
    print(titulo)
    opciones = """
    1. Jugar Torneo
    2. tabla Intermedio
    3. Ganador Torneo
    4. Salir
    """
    print(opciones)
    try:
        op = int(input(')_'))
    except ValueError:
        print('el valor que estas ingresando no es entero')
        os.system('pause')
        MenuIntemedio()
    else:
        if op < 1 and op > 4:
            print('la opcion debe estar en el menu')
            os.system('pause')
            MenuIntemedio()
        else:
            return op 

def MenuAvanzado():
    os.system('cls')
    titulo= """
        +++++++++++++++++++
        + Torneo Avanzado +
        +++++++++++++++++++
    """
    print(titulo)
    opciones = """
    1. Jugar Torneo
    2. tabla Avanzado
    3. Ganador Torneo
    4. Salir
    """
    print(opciones)
    try:
        op = int(input(')_'))
    except ValueError:
        print('el valor que estas ingresando no es entero')
        os.system('pause')
        MenuAvanzado()
    else:
        if op < 1 and op > 4:
            print('la opcion debe estar en el menu')
            os.system('pause')
            MenuAvanzado()
        else:
            return op 