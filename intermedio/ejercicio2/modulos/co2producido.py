import os

def CO2Producido(dependencias: dict):
    for idx, (key, item) in enumerate(dependencias.items()):
        try:
            emisionCO2 = item['emision']
        except KeyError:
            print('aun no has registrado ningun consumo')
            break
        else:
            print (f'{idx+1}. La produccion de CO2 de {key} es {emisionCO2}')
    os.system('pause')

def MaxCO2(dependencias= dict):
    if dependencias:
        maxCO2 = max(dependencias.items(), key=lambda x: x[1].get('emision', 0))
        emision = maxCO2[1]['emision']
        nombreMax = max(dependencias.items(), key=lambda x: x[1].get('emision', 0))[0]
        print(f'la dependencia  que mas CO2 consumio fue {nombreMax} con {emision}')
        os.system('pause')
    else: 
        print('no has añadiddo ninguna dependencia')
        os.system('pause')