import os
from tabulate import tabulate

def tabla(lstTabla= dict):
    tablaOrdenada = sorted(lstTabla.items(), key= lambda x: x[1].get('TP'))
    table = []
    for key, value in lstTabla.items():
        os.system('cls')
        table.append(value)
        print(tabulate(table, headers='keys', tablefmt='grid'))
    os.system('pause')