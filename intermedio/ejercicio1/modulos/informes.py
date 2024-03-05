import os

def informes(ciudades= list, peligro= list):
    for ciudad in ciudades:
        promedio=  sum(ciudad[1]) / len(ciudad[1])
        if promedio <= 2.5:
            peligro[0].append(ciudad[0])
        elif promedio >= 2.6 and promedio < 4.4:
            peligro[1].append(ciudad[0])
        else:
            peligro[2].append(ciudad[0])
    
    if peligro[0]:
        for idx, items in enumerate(peligro[0]):
            print('Amarillo (sin riesgo)')
            print(f'{idx+1}. {items}')

    if peligro[1]:
        for idx, items in enumerate(peligro[1]):
            print('Naranja (riesgo medio)')
            print(f'{idx+1}. {items}')

    if peligro[2]:
        for idx, items in enumerate(peligro[2]):
            print('Rojo (riesgo alto)')
            print(f'{idx+1}. {items}')
    
    os.system('pause')