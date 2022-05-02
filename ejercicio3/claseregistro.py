class Registro:
    __dia=''
    __hora=''
    __temperatura=''
    __humedad=''
    __presion=''
    def __init__(self, dia:int, hora, temperatura, humedad, presion):
        self.__dia=int(dia)
        self.__hora= hora
        self.__temperatura= temperatura
        self.__humedad=humedad
        self.__presion= presion
    def __str__(self):
        s='Hora: {} Temperatura: {}C° Humedad: {}% Presión: {}HP'.format(self.__hora,self.__temperatura,self.__humedad,self.__presion)
        return s
    def retornadia(self):
        return self.__dia
