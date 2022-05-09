import csv
import numpy as np
from datetime import date as dt
from clasecama import Cama
from manejadormicamentos import ManejadorMeciamentos

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

    
