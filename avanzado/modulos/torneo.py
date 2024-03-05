import os

def Torneo(categoria= dict, nroTorneo= int):
    if len(categoria) >= 5:
        nroTorneo += 1
        partidos = []
        for key, values in categoria.items():
            for llave, valores in categoria.items():
                if key == llave:
                    continue
                else:
                    os.system('cls')
                    team1 = values['nombre']
                    team2 = valores['nombre']
                    print(f'partido {key}. {team1} vs {llave}. {team2} ')
                    partidos.append([llave, key])
                    if [key, llave] in partidos:
                        continue
                    else:
                        isValuetrue= True
                        while isValuetrue: 
                            ganador= str(input('quien fue el ganador (ingrese el ID) :'))
                            if ganador == llave:
                                isValuetrue1 = True
                                while isValuetrue1:
                                    try:
                                        perdedor = int(input(f'ingrese cuantos puntos hizo {team1} :'))
                                    except ValueError:
                                        print('el numero a ingresar debe ser un entero')
                                        os.system('pause')
                                    else:
                                        if perdedor < 0 and perdedor > 10:
                                            print('los puntos deben ser positivos y deben ser menores a los del ganador (11)')
                                            os.system('pause')
                                        else:
                                            valores['PJ'] += 1
                                            valores['PG'] += 1
                                            PA= 11 - perdedor
                                            valores['PA'] += 1
                                            valores['TP'] += 2
                                            values['PJ'] += 1
                                            values['PP'] += 1
                                            isValuetrue1= False
                                            isValuetrue = False
                            elif ganador == key:
                                isValuetrue1 = True
                                while isValuetrue1:
                                    try:
                                        perdedor = int(input(f'ingrese cuantos puntos hizo {team2} :'))
                                    except ValueError:
                                        print('el numero a ingresar debe ser un entero')
                                        os.system('pause')
                                    else:
                                        if perdedor < 0 and perdedor > 10:
                                            print('los puntos deben ser positivos y deben ser menores a los del ganador (11)')
                                            os.system('pause')
                                        else:
                                            values['PJ'] += 1
                                            values['PG'] += 1
                                            Pa= 11 - perdedor
                                            values['PA'] += Pa
                                            values['TP'] += 2
                                            valores['PJ'] += 1
                                            valores['PP'] += 1
                                            isValuetrue1= False
                                            isValuetrue= False
                            else:
                                print('La id ingresada es invalida, debes ingresar el numero que esta al lado del nombre')
                                os.system('pause')
    else:
        print('ingresa primero al menos 5 jugadores')
        os.system('pause')