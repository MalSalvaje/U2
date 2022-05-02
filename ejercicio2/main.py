from claseviajero import Viajero
from manejador import manejador
from menu import Menu

if __name__=='__main__':
    unmanejador = manejador() 
    unmanejador.leerarchivo()
    unmanejador.mostrarlista() #invoca al str del objeto unmanejador
    unmenu=Menu()
    num=input('\nIngrese numero de viajero:')
    print(unmenu)
    op=input('\nIngrese numero de opcion:')
    unmenu.opcion(op,unmanejador,num)
