import modulos.menu as me
import modulos.regisciudad as rc
import modulos.regissismo as rs
import modulos.buscar_sismos as bs
import modulos.informes as inf

ciudades= []
peligro = [[],[],[]]

if __name__ == "__main__":
    issAppRunning= True
    while issAppRunning:
        op = me.menu()
        if op == 1:
            rc.AddCiudad(ciudades)
            rs.IgualarSismos(ciudades)
        elif op == 2:
            rs.AddSismo(ciudades)
        elif op == 3:
            bs.SearchSismos(ciudades)
        elif op == 4:
            inf.informes(ciudades, peligro)
        elif op == 5:
            issAppRunning = False