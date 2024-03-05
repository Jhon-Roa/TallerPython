import os

def AddDependencia(dependencias= dict):
    print('ingrese el nombre de la dependencia que desea ingresar')
    nombre= str(input(')_'))
    dependencias.update({nombre: {}})
    issAddDependencia= True
    while issAddDependencia:
        dispositivo = str(input('ingrese un dispositivo :'))
        dependencias[nombre].update({dispositivo: 0.0})
        dependencias[nombre].update({'emision': 0.0})
        issAddDependencia= bool(input('Deseas agregar otro dispositivo en {nombre} SI[S] NO[ENTER]'))

    