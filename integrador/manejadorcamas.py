import csv
import numpy as np
from datetime import date as dt
from clasecama import Cama
from manejadormedicamentos import ManejadorMedicamentos

class ManejadorCamas:
    __cantidad = 0
    __dimension = 30
    __incremento = 5
    __camas = None

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 30
        self.__incremento = 5
        self.__camas = np.empty(30, dtype=Cama)

    def agregarCama(self, unacama):
        if isinstance(unacama, Cama):
            if self.__cantidad == self.__dimension:
                self.__dimension += self.__incremento
                self.__camas.resize(self.__dimension)
            self.__camas[self.__cantidad] = unacama
            self.__cantidad += 1

    def leerarchivo(self):
        archivo=open('camas.csv')
        reader=csv.reader(archivo, delimiter=';')
        for fila in reader:
            unacama=Cama(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            self.agregarCama(unacama)
        archivo.close()

    def buscarPaciente(self, nombre):
        i=0
        while i<self.__cantidad and self.__camas[i].getNombre().lower()!=nombre.lower():
            i+=1
        if i==self.__cantidad:
            return  -1
        else:
            return i

    def darAlta(self, unmanejadormedicamentos):
        if isinstance(unmanejadormedicamentos, ManejadorMedicamentos):
            nombre=str(input('Ingrese nombre del paciente a dar de alta:'))
            pos=self.buscarPaciente(nombre)

            if pos!=-1:
                if self.__camas[pos].getEstado():
                    hoy= dt.today()
                    hoy= hoy.strftime('%d/%m/%Y')
                    self.__camas[pos].alta(hoy)
                    print(self.__camas[pos])
                    print(unmanejadormedicamentos.getMedicamentoPorIdCama(self.__camas[pos].getIdCama()))
                else:
                    print('El paciente ya se encuentra de alta')
            else:
                    print('No se encientra el paciente')
    
    def mostrarPacientesPorDiagnostico(self):
        diagnostico=str(input('Ingrese diagnostico para mostrar pacientes con diagnostico coincidente:'))
        for cama in self.__camas:
            if isinstance(cama,Cama):
                if cama.getEstado() and cama.getDiagnostico().lower()==diagnostico.lower():
                    print('Nombre: {} Cama: {} Habitacion: {} Diagnostico: {} Fecha de Internacion: {}'.format(cama.getNombre(),cama.getIdCama(),cama.getHabitacion(),cama.getDiagnostico(),cama.getFechaInternacion()))
