class Viajero:
        __numViajero =0
        __dni= ''
        __nombre= ''
        __apellido= ''
        __millasAcumuladas=0
        def __init__(self, numViajero:int, dni, nombre, apellido, millasAcumuladas:int):
            self.__numViajero = int(numViajero)
            self.__dni= dni
            self.__nombre= nombre
            self.__apellido= apellido
            self.__millasAcumuladas= int(millasAcumuladas)
        def idviajero(self):
            return int(self.__numViajero)
        def cantidadTotalMillas(self):
            return int(self.__millasAcumuladas)
        def acumularMillas(self, millas):
            self.__millasAcumuladas += int(millas)
        def canjeaMillas(self, millas):
            if int(millas) <= int(self.__millasAcumuladas):
                self.__millasAcumuladas -= millas
            else:
                print("Error: No hay suficientes millas para efectuar el canje.")
        def __str__(self):
            info='Número de viajero: {}\nDNI: {}\nNombre: {}\nApellido: {}\nMillas Acumuladas: {}' .format(self.__numViajero, self.__dni, self.__nombre, self.__apellido, self.__millasAcumuladas)
            return info
