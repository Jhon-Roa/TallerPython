import modulos.menu as me
import modulos.regis_dependencia as rd
import modulos.consumo as co
import modulos.co2producido as cp

dependencias= {}

if __name__ == "__main__":
    isAppRunning= True
    while isAppRunning:
        op= me.Menu()
        if op == 1:
            rd.AddDependencia(dependencias)
        elif op == 2:
            co.consumo(dependencias)
        elif op == 3:
            cp.CO2Producido(dependencias)
        elif op == 4:
            cp.MaxCO2(dependencias)
        elif op == 5:
            isAppRunnings = False