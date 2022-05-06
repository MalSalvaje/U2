from claseregistro import Registro
from manejador import Manejador
from menu import Menu

if __name__=='__main__':
    unmenu=Menu()
    unmanejador=Manejador()
    
    unmanejador.leearchivo()
    print(unmenu)
    opcion=input('Ingrese opcion preferida:')
    unmenu.opcion(opcion,unmanejador)
