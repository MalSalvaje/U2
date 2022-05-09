from manejadorcamas import ManejadorCamas
from manejadormedicamentos import ManejadorMedicamentos


class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.salir
                          }
    def opcion(self, unmanejadorcamas, unmanejadormedicamentos, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1':
            func(unmanejadorcamas, unmanejadormedicamentos)
        elif op=='2':
            func(unmanejadorcamas)
        else:
            func(unmanejadorcamas)
    def salir(self, unmanejadorcamas):
        print('Usted salio del programa')


    def opcion1(self, unmanejadorcamas, unmanejadormedicamentos):
        if isinstance(unmanejadorcamas, manejadorcamas) and isinstance(unmanejadormedicamentos, manejadormedicamentos):
            unmanejadorcamas.darAlta(unmanejadormedicamentos)


    def opcion2(self, unmanejadorcamas):
        if isinstance(unmanejadorcamas, manejadorcamas):
            unmanejadorcamas.mostrarPacientesPorDiagnostico()


    def mostrarMenu(self, unmanejadorcamas, unmanejadormedicamentos):
        if isinstance(unmanejadorcamas, manejadorcamas) and isinstance(unmanejadormedicamentos, manejadormedicamentos):
            opcion = '0'
            while opcion != '3':
                print('1. Dar de alta a un paciente.')
                print('2. Mostrar los datos de los pacientes con el diagnostico indicado.')
                print('3. Salir')
                opcion = input('Ingrese opcion preferida:')  
                self.opcion(unmanejadorcamas, unmanejadormedicamentos, opcion)
