from manejador import Manejador

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.salir
                            }
    def opcion(self, op, unmanejador):
        func=self.__switcher.get(op, lambda: print('Opción no válida.'))
        if op=='5':
            func()
        else:
            return func(unmanejador)
    def salir(self):
        print('Usted salio del programa.')
    def opcion1(self, unmanejador):
        if isinstance(unmanejador, Manejador):
            return unmanejador.actualizarValores()
        else:
            print('Error. Se esperaba un objeto de clase Manejador')
    def opcion2(self, unmanejador):
        if isinstance(unmanejador, Manejador):
            return unmanejador.mostrarMenores()
        else:
            print('Error. Se esperaba un objeto de clase Manejador')
    def opcion3(self, unmanejador):
        if isinstance(unmanejador, Manejador):
            return unmanejador.mostrarPendiente()
        else:
            print('Error. Se esperaba un objeto de clase Manejador')
    def opcion4(self, unmanejador):
        if isinstance(unmanejador, Manejador):
            return unmanejador.modificaCuotas()
        else:
            print('Error. Se esperaba un objeto de clase Manejador')
    def __str__(self):
        s='1. Actualizar el valor del vehiculo de cada plan.\n2. Buscar planes con cuotas inferiores a un valor.\n3.Ver monto a pagar para licitar un vehiculo.\n4.Modificar cuotas necesarias para licitacion.\n5.Salir del programa.\n'
        return s


