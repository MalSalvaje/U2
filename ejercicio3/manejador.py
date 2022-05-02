import csv
from claseregistro import Registro

class Manejador:
    __lista=[[],[]]
    def agregarregistro(self, unregistro):
        self.__lista[unregistro.retornadia()-1].append(unregistro)
    def leearchivo(self):
       archivo=open('registros.csv')
       reader=csv.reader(archivo,delimiter=',')
       for fila in reader:
           d=fila[0]
           h=fila[1]
           temp=fila[2]
           hum=fila[3]
           pres=fila[4]
           unregistro=Registro(d,h,temp,hum,pres)
           self.agregarregistro(unregistro)   
    def mostrardia(self,dia:int):
        for registro in self.__lista[dia-1]:
            print(registro)
    def mostrarmin(self):
        for dia in self.__lista:
            for registro in dia:
                print(registro)
