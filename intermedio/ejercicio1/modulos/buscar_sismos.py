import os

def SearchSismos(ciudades= list):
    for idx, items in enumerate(ciudades):
        os.system('cls')
        busqueda= str(input('ingresa el nombre de la ciudad que estas buscando :'))
        if busqueda in ciudades[idx]:
            print(f'si se encuentra la ciudad {busqueda}, y la intensidad de sus sismos son {ciudades[idx][1]}')
            os.system('pause')
            break
        else:
            print('no encontramos la ciudad :,c')
            os.system('pause')