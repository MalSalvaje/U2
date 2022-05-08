from manejador import Manejador

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir
                          }
    def opcion(self, op, unmanejador):
        func=self.__switcher.get(op, lambda: print('Opción no válida.'))
        if op=='1' or op=='2' or op=='3': 
            return func(unmanejador)
        else:
            func()
    def salir(self):
        print('Usted salió del programa.')
    def opcion1(self, unmanejador):
        if type(unmanejador)==Manejador:
            return unmanejador.mostrarmin()
    def opcion2(self, unmanejador):
        if type(unmanejador)==Manejador:
            return unmanejador.promedioporhora()
    def opcion3(self, unmanejador):
        if type(unmanejador)==Manejador:
            return unmanejador.mostrardia()
    def __str__(self):
        return '1. Mostrar minimos mensuales de temperatura, humedad y presion.\n2. Mostrar promedio mensual de temperatura para cada hora del dia.\n3. Mostrar todos los registros de un dia indicado.4. Salir del programa\n'

