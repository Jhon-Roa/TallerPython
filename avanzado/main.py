import modulos.añadirjugador as aj
import modulos.menu as me
import modulos.torneo as to
import modulos.tabla as ta
import modulos.Ganador as ga

categorias = dict({'Novato': {}, 'Intermedio': {}, 'Avanzado': {}})
torneos= [[],[],[]]

if __name__ == "__main__":
    isAppRunning = True
    while isAppRunning:
        op = me.Menu()
        if op == 1:
            isValueTrue= True
            while isValueTrue:
                aj.AddPlayer(categorias)
                print('desea agregar otro jugador S[Si] ENTER[No]')
                isValueTrue= str(input(')_'))
        elif op == 2:
            nroN= 0
            isValueTrue= True
            while isValueTrue:
                opm = me.MenuNovatos()
                if opm == 1:
                    if nroN == 0:
                        to.Torneo(categorias['Novato'], nroN)
                    else:
                        print('el torneo ya fue realizado :C')
                        to.os.system('pause')
                elif opm == 2:
                    ta.tabla(categorias['Novato'])
                elif opm == 3:
                    ga.Ganador(categorias['Novato'])
                elif opm == 4:
                    isValueTrue = False
        elif op == 3:
            nroI = 0
            isValueTrue = True
            while isValueTrue:
                opm = me.MenuIntemedio()
                if opm == 1:
                    if nroI == 0:
                        to.Torneo(categorias['Intermedio'], nroI)
                    else:
                        print('el torneo ya fue realizado :C')
                        to.os.system('pause')
                elif opm == 2:
                    ta.tabla(categorias['Intermedio'])
                elif opm == 3:
                    ga.Ganador(categorias['Intermedio'])
                elif opm == 4:
                    isValueTrue = False
        elif op == 4:
            nroA = 0
            isValueTrue = True
            while isValueTrue:
                opm = me.MenuAvanzado()
                if opm == 1:
                    if nroA == 0:
                        to.Torneo(categorias['Avanzado'], nroA)
                    else:
                        print('el torneo ya fue realizado :C')
                        to.os.system('pause')
                elif opm == 2:
                    ta.tabla(categorias['Avanzado'])
                elif opm == 3:
                    ga.Ganador(categorias['Avanzado'])
                elif opm == 4:
                    isValueTrue = False
        elif op == 5:
            isAppRunning= False
