from manejador import Manejador
from menu import Menu

if __name__=='__main__':
    unmanejador=Manejador()
    unmenu=Menu()
    unmanejador.leearchivo()
    unmanejador.mostrarPlanes()
    print(unmenu)
    opcion=input('Ingrese número de opción preferida:')
    unmenu.opcion(opcion, unmanejador)
    unmanejador.mostrarPlanes()

