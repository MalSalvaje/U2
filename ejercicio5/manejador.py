from claseplanahorro import PlanAhorro
import csv

class Manejador:
    __lista=[]

    def __init__(self):
        self.__lista = []
    def agregarPlan(self, unplan):
        if isinstance(unplan,PlanAhorro):
            self.__lista.append(unplan)
    def leearchivo(self):
        archivo=open('planes.csv')
        reader=csv.reader(archivo, delimiter=';')
        for fila in reader:
            cod=int(fila[0])
            mod=fila[1]
            ver=fila[2]
            val=int(fila[3])
            unplan=PlanAhorro(cod, mod, ver, val)
            self.agregarPlan(unplan)
        archivo.close()
    def actualizarValores(self):
        for plan in self.__lista:
            print(plan.getCodigo())
            print(plan.getModelo())
            num=input('Ingrese nuevo valor del vehículo:')
            plan.setValor(num)
    def mostrarMenores(self):
        val=float(input('Ingrese valor para mostrar planes con una cuota inferior al valor dado:'))
        for plan in self.__lista:
            if plan.getValorCuota()<val:
                print(plan.getCodigo())
                print(plan.getModelo())
                print(plan.getVersion())
    def buscarPorCodigo(self, cod):
        i=0
        while i<len(self.__lista) and cod!=self.__lista[i].getCodigo():
                i+=1
        if i<len(self.__lista):
            return i
        else:
            return -1
    def mostrarPendiente(self):
        cod=int(input('Ingresar codigo del plan para ver importe necesario para licitar el vehiculo:'))
        pos=self.buscarPorCodigo(cod)
        if pos!= -1:
            print('El monto a pagar para licitar el vehiculo es: {}' .format(self.__lista[pos].getMontoLicitacion()))
        else:
            print('No se encontró el vehículo')
    def modificaCuotas(self):
        cod=int(input('Ingresar codigo del plan a modificar:'))
        pos=self.buscarPorCodigo(cod)
        if pos!= -1:
            num=input('Ingrese nueva cantidad de cuotas:')
            self.__lista[pos].setCuotasLicitacion(num)
        else:
            print('No se encontro el plan.')
    def mostrarPlanes(self):
        for plan in self.__lista:
            print(plan)
        


