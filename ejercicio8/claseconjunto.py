class Conjunto:
    __elementos=[]
    
    def __init__(self):
        self.__elementos=[]

    def agregarElemento(self, elem):
        if type(elem)==int:
            if elem not in self.__elementos:
                self.__elementos.append(elem)
                self.__elementos.sort()
            else:
                print('Numero repetido')
        else:
            print('Solo pueden agregarse enteros.')
    
    def getElemento(self, indice):
            return self.__elementos[indice]

    def getLength(self):
        return len(self.__elementos)

    def __add__(self,otro):
        if isinstance(otro, Conjunto):
            suma=Conjunto()
        i=0
        j=0
        for i in range(len(self.__elementos)):
                while j<otro.getLength() and otro.getElemento(j)<=self.__elementos[i]: 
                    suma.agregarElemento(otro.getElemento(j))
                    j=j+1
                if j==otro.getLength():
                    suma.agregarElemento(self.__elementos[i])
                elif self.__elementos[i]< otro.getElemento(j):
                    suma.agregarElemento(self.__elementos[i])
        while j<otro.getLength():
            suma.agregarElemento(otro.getElemento(j))
            j=j+1
        return suma

    def __sub__(self,otro):
        resta=Conjunto()
        
        for elemento in self.__elementos:
            i=0
            while i<otro.getLength() and elemento!=otro.getElemento(i):
                i+=1
            if i>=otro.getLength():
                resta.agregarElemento(elemento)
        return resta

    def mostrar(self):
        for elemento in self.__elementos:
            print(elemento)

    def __str__(self):
        cadena=''
        if self.getLength()!=0:
            for elemento in self.__elementos:
                cadena+='{} '.format(elemento)
        return cadena
    
    def __eq__(self, otro):
        if self.getLength()!=otro.getLength():
            return False
        else:
            band=True
            for i in range(len(self.__elementos)):
                if self.__elementos[i]!=otro.getElemento(i):
                    band=False
            return band




