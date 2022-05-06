import datetime as dt
class Registro:
    __dia=''
    __hora=''
    __temperatura=''
    __humedad=''
    __presion=''
    def __init__(self, dia:int, hh, mm, temperatura, humedad, presion):
        self.__dia=int(dia)
        self.__hora=dt.time(int(mm), int(hh))
        self.__temperatura=int(temperatura)
        self.__humedad=int(humedad)
        self.__presion=int(presion)
    def __str__(self):
        s='Hora: {} Temperatura: {}C° Humedad: {}% Presión: {}HP'.format(self.__hora,self.__temperatura,self.__humedad,self.__presion)
        return s
    def retornadia(self):
        return self.__dia
    def retornahora(self):
        return self.__hora
    def retornatemperatura(self):
        return self.__temperatura
    def retornahumedad(self):
        return self.__humedad
    def retornapresion(self):
        return self.__presion
