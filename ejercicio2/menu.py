from manejador import manejador

class Menu:
    __switcher= None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir
                          }
    def opcion(self,op,unmanejador,num):
        func=self.__switcher.get(op, lambda: print('Opción no válida.'))
        if op=='1' or op=='2' or op=='3':
            return func(unmanejador, num)
        else:
            func()
    def salir(self):
        print('Usted salió del programa.')
    def opcion1(self, unmanejador, num):
        if type(unmanejador)==manejador:
            return unmanejador.buscarmillas(num)
    def opcion2(self, unmanejador, num):
        if type(unmanejador)==manejador:
            unmanejador.ingresamillas(num)
    def opcion3(self, unmanejador, num):
        if type(unmanejador)==manejador:
            unmanejador.restamillas(num)
    def __str__(self):
        return '1. Ver cantidad de millas del viajero.\n2.Sumar millas al viajero\n3.Canjear millas del viajero.\n4.Salir del programa.'
