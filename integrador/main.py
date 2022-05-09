from manejadorcamas import ManejadorCamas
from manejadormedicamentos import ManejadorMedicamentos
from menu import Menu

if __name__=='__main__':
    unmanejadorcamas=ManejadorCamas()
    unmanejadormedicamentos=ManejadorCamas()
    unmenu=Menu()

    unmanejadorcamas.leerarchivo()
    unmanejadormedicamentos.leerarchivo()
    unmenu.mostrarMenu(unmanejadorcamas, unmanejadormedicamentos)
