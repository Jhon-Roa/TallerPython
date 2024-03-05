import os

def AddCiudad(ciudades= list):
    os.system('cls')
    ciudad = str(input('ingrese el nombre de la ciudad :'))
    ciudades.append([ciudad])
    for idx, item in enumerate(ciudades):
        if len(ciudades[idx]) < 2:
            ciudades[idx].append([])