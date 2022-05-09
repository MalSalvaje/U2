from clasemedicamento import Medicamento
import csv

class ManejadorMedicamentos:
    __medicamentos= []

    def __init__(self):
        self.__medicamentos= []

    def agregarMedicamento(self, unmedicamento):
        if isinstance(unmedicamento,Medicamento):
            self.__medicamentos.append(unmedicamento)
    
    def leerarchivo(self):
            archivo=open('medicamentos.csv')
            reader=csv.reader(archivo, delimiter=';')
            for fila in reader:
                unmedicamento=Medicamento(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5], float(fila[6]))
                self.agregarMedicamento(unmedicamento)
            archivo.close()

    def getMedicamentosPorIdCama(self, numero):
        suma=0
        c='{}'
        for medicamento in self.__medicamentos:
            if medicamento.getIdCama()==numero:
                cadena+='Medicamento: {} Monodroga: {} Presentacion: {} Cantidad: {} Precio: {}'.format(medicamento.getNombreComercial(),medicamento.getMonodroga(),medicamento.getPresentacion(),medicamento.getCantidadAplicada(),medicamento.getPrecio())
                suma+=medicamento.getPrecio()
        return suma

    

    
