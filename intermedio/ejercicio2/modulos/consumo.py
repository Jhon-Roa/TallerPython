import os

def consumo(dependencias: dict):
    os.system('cls')
    ignorar='emision'
    for llave, values in dependencias.items():
        for key, item in values.items():
            os.system('cls')
            if key == ignorar:
                continue
            if dependencias[llave][key] == 0.0:
                print(f'{llave}')
                if values[key] == 0.0:
                    isValueTrue= True
                    while isValueTrue:
                        try:
                            w = float(input(f'ingrese la cantidad de vatios de {key} :'))
                            h = float(input(f'ingrese la cantidad de horas de uso de {key} en el mes :'))
                        except ValueError:
                            print('uno de los valores que estas ingresando no es un numero')
                            os.system('pause')
                        else:
                            isValueTrue= False
                    consumo = (w*h)/1000 
                    values.update({key: consumo})
                    suma = sum(values.values())
                    emisionCO2 = float(suma*0.126)
                    emisionCO2 = round(emisionCO2, 3)
                    values.update({'emision': emisionCO2})