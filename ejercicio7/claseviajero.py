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

        def __gt__(self, otro):
            if isinstance(otro, Viajero):
                if self.cantidadTotalMillas()>otro.cantidadTotalMillas():
                    return True
                else:
                    return False
            elif type(otro)==int:
                    if self.cantidadTotalMillas()>otro:
                        return True
                    else:
                        return False
            else:
                print('No puede realizarse la comparación entre tipo viajero y tipo {}'.format(type(otro)))

        def __lt__(self, otro):
                    if isinstance(otro, Viajero):
                        if self.cantidadTotalMillas()<otro.cantidadTotalMillas():
                            return True
                        else:
                            return False
                    elif type(otro)==int:
                            if self.cantidadTotalMillas()<otro:
                                return True
                            else:
                                return False
                    else:
                        print('No puede realizarse la comparación entre tipo viajero y tipo {}'.format(type(otro)))


        def __add__(self,otro):
                if type(otro)==int:
                    result=self.cantidadTotalMillas()+otro
                    suma=Viajero(self.__numViajero,self.__dni,self.__nombre,self.__apellido,result)
                    return suma
                else:
                    print('No puede sumarse viajero y tipo de dato {}'.format(type(otro)))          

        def __radd__(self,otro):
                if type(otro)==int:
                    result=self.cantidadTotalMillas()+otro
                    suma=Viajero(self.__numViajero,self.__dni,self.__nombre,self.__apellido,result)
                    return suma
                else:
                    print('No puede sumarse viajero y tipo de dato {}'.format(type(otro)))          

        def __sub__(self,otro):
                if type(otro)==int:
                    result=self.cantidadTotalMillas()-otro
                    resta=Viajero(self.__numViajero,self.__dni,self.__nombre,self.__apellido,result)
                    return resta
                else:
                    print('No puede restarse viajero y tipo de dato {}'.format(type(otro)))          
        
        def __rsub__(self,otro):
                if type(otro)==int:
                    result=self.cantidadTotalMillas()-otro
                    resta=Viajero(self.__numViajero,self.__dni,self.__nombre,self.__apellido,result)
                    return resta
                else:
                    print('No puede restarse viajero y tipo de dato {}'.format(type(otro)))          

        def __eq__(self,otro):
            if isinstance(otro,Viajero):
                if self.cantidadTotalMillas()==otro.cantidadTotalMillas():
                    return True
                else:
                    return False
            elif type(otro)==int:
                if self.cantidadTotalMillas()==otro:
                    return True
                else:
                    return False
            else:
                    print('ERROR. No se puede comparar viajero con tipo de dato {}'.format(type(otro)))
