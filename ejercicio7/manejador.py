from claseviajero import Viajero
import csv

class Manejador:
    __lista= []

    def __init__(self):
        self.__lista= []

    def agregarViajero(self, unviajero):
        if type(unviajero) == Viajero:
            self.__lista.append(unviajero)

    def leerarchivo(self):
        archivo=open('viajeros.csv')
        reader=csv.reader(archivo, delimiter=";")
        for fila in reader:
            numViajero=int(fila[0])
            dni=fila[1]
            nombre=fila[2]
            apellido=fila[3]
            millasAcumuladas=int(fila[4])
            unviajero=Viajero(numViajero, dni, nombre, apellido, millasAcumuladas)
            self.agregarViajero(unviajero)
        archivo.close()

    def mostrarlista(self):
        for viajero in self.__lista:
            print(viajero)

    def buscarmillas(self, num):
        for i in range(len(self.__lista)):
            if (self.__lista[i].idviajero()==int(num)):
                total=self.__lista[i].cantidadTotalMillas()
        return total

    def buscaviajero(self, num):
        for i in range(len(self.__lista)):
            if (self.__lista[i].idviajero()==int(num)):
                break
        return i

    def ingresamillas(self, num):
        i=self.buscaviajero(num)
        millas=int(input('Ingrese cantidad de millas a sumar:'))
        self.__lista[i]=millas+self.__lista[i] #Se invoca la suma subrocargada por derecha
        print('Total millas actualizado {}'.format(self.__lista[i].cantidadTotalMillas()))

    def restamillas(self, num):
        i=self.buscaviajero(num)
        millas=int(input('Ingrese cantidad de millas a canjear:'))
        self.__lista[i]=millas-self.__lista[i]
        print('Total millas actualizado {}'.format(self.__lista[i].cantidadTotalMillas()))

    def comparar(self):
        if self.__lista[2]>100:
            print('El viajero 3 tiene mas millas que el viajero 4')
        else:
            print('El viajero 3 no tiene mas millas que el viajero 4')
    
    def verificar(self):
        pos=int(input('Ingrese numero de viajero para determinar si tiene 200 millas'))-1
        if 200==self.__lista[pos]: #Se comprueba que no es necesario sobrecargar el operador por derecha
            print('El viajero tiene exactamente 200 millas')
        else:
            print('El viajero no tiene 200 millas')

    def encontrarMaximo(self):
        max=int(self.__lista[0].cantidadTotalMillas())
        pos=0
        for i in range(len(self.__lista)):
            if self.__lista[i]>max:
                max=self.__lista[i].cantidadTotalMillas()
                pos=i
        print('El viajero con mas millas es el numero {}'.format(pos+1))


