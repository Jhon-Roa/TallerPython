import os

def Ganador(lstGanador= dict):
    os.system('cls')
    maxValor = max(lstGanador.items(), key= lambda x: x[1].get('TP'))
    Comprobacion = maxValor[1]['TP']
    claves= []
    claves_max= []
    for values in lstGanador.values():
        TPL = values['TP']
        claves.append(TPL)
    for item in claves:
        if item == Comprobacion:
            claves_max.append(item)
    HacetTA= len(claves_max)
    if HacetTA == 1:
        nombreGanador = maxValor[1]['nombre']
        puntuacionGanador = maxValor[1]['TP']
        print(f'el ganador fue {nombreGanador} con un total de {puntuacionGanador} puntos')
        os.system('pause')
    else:
        maxValor = max(lstGanador.items(), key= lambda x: x[1].get('PA'))
        nombreGanador = maxValor[1]['nombre']
        puntuacionGanador = maxValor[1]['PA']
        print('debido a un empate')
        print(f'el ganador fue {nombreGanador} con un total de {puntuacionGanador} puntos a favor')
        os.system('pause')