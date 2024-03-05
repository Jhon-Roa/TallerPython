import os

def AddStock(lstProductos= dict):
    validate = str(input('ingrese el codigo del producto al que quieres ingresar un stock :'))
    if validate in lstProductos:
        isValueTrue= True
        while isValueTrue:
            try:
                stock= int(input('ingrese el stock del producto :'))
            except ValueError:
                print('el stock debe ser un numero entero')
                os.system('pause')
            else:
                if stock > 0 and stock < lstProductos[validate]['stockMaximo']:
                    isValueTrue= False
                    lstProductos[validate].update({'stock': stock})
                else:
                    print('el stock debe ser positivo y estar debajo del stock maximo')
                
def ProductosCriticos(lstProductos= dict):
    print('estos productos estan por debajo del stock minimo')
    for idx, (key, item) in enumerate(lstProductos.items()):
        if item['stockMinimo'] > item['stock']:
            noHay= 1
            product = item['producto']
            print(f'{idx+1}. {product}')
    if not noHay == 1:
        print('no hay productos en estado critico')
    os.system('pause')
            
def Ganancia(lstProductos = dict):
    print('ganancia potencial de los productos:')
    for idx, (key, item) in enumerate(lstProductos.items()):
        resta = item['valorVenta'] - item['valorCompra']
        ganancia = resta * item['stock']
        product= item['producto']
        print(f'{idx+1}. {product}: {ganancia} ')
    os.system('pause')