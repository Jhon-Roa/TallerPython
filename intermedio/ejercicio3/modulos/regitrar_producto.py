import os

def ListaProducto(lstProductos= dict):
    os.system('cls')
    titulo = """
        ***********************
        * REGISTRO DE EQUIPOS *
        ***********************
    """
    print(titulo)

    codigo = str(input('ingrese el codigo de un producto :'))
    nombre = str(input('ingrese el nombre del producto :'))
    isValueTrue = True
    while isValueTrue:
        try:
            valorC = int(input('ingrese el valor de compra del producto :'))
            valorV = int(input('ingrese el valor de venta del producto :'))
        except ValueError:
            print('debes ingresar un valor entero')
            os.system('pause')
        else:
            if valorV < valorC:
                ('el valor de venta debe ser mayor al de compra')
                os.system('pause')
            else:
                isValueTrue= False
    isValueTrue = True
    while isValueTrue:
        try:
            stockMin = int(input('Ingrese el stock mínimo: '))
            stockMax = int(input('Ingrese el stock máximo: '))
        except ValueError:
            print('El stock debe ser un valor entero.')
            input('Presiona Enter para continuar...')
        else:
            if stockMax < stockMin:
                ('el stock maximo debe ser mayor al stock minimo')
                os.system('pause')
            else:
                isValueTrue= False
                
    nombreP = str(input('ingrese el nombre de el proveedor :'))

    lstProductos.update({codigo: {'codigo': codigo, 'producto': nombre, 'valorCompra': valorC, 'valorVenta': valorV, 'stockMinimo': stockMin, 'stockMaximo': stockMax, 'Proveedor': nombreP}})
    print(lstProductos)


