import modulos.regitrar_producto as rp
import modulos.menu as me
import modulos.tabla_productos as tp
import modulos.añadir_stock as ast

lstProductos=  {}

if __name__ == "__main__":
    isAppRunning= True
    while isAppRunning:
        op= me.Menu()
        if op == 1:
            rp.ListaProducto(lstProductos)
        elif op == 2:
            tp.tabla(lstProductos)
        elif op == 3:
            ast.AddStock(lstProductos)
        elif op == 4:
            ast.ProductosCriticos(lstProductos)
        elif op == 5:
            ast.Ganancia(lstProductos)
        elif op == 6:
            isAppRunnings = False

