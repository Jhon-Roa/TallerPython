from tabulate import tabulate
import os

def tabla(lstProductos= dict):
    table=  []
    for key, item in lstProductos.items():
        os.system('cls')
        table.append(item)
        print(tabulate(table, headers='keys', tablefmt='grid'))
    os.system('pause')