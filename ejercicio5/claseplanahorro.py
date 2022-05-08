class PlanAhorro:
    #VariablesDeInstancia
    __codigo=''
    __modelo=''
    __version=''
    __valor=''
    #VariablesDeClase
    __cantidadCuotas=60
    __cuotasLicitacion=10
    def __init__(self, codigo, modelo, version, valor):
        self.__codigo= int(codigo)
        self.__modelo= modelo
        self.__version= version
        self.__valor=int(valor)
    def getCodigo(self):
        return self.__codigo
    def getModelo(self):
        return self.__modelo
    def getVersion(self):
        return self.__version
    def getValor(self):
        return self.__valor
    def getValorCuota(self):
        return self.__valorCuota
    def setValor(self, num):
        self.__valor=num
    def setCuotasLicitacion(self, num):
        self.__cuotasLicitacion=num
    @classmethod
    def getCantidadCuotas(cls):
        return cls.__cantidadCuotas
    @classmethod
    def getCuotasLicitacion(cls):
        return cls.__cuotasLicitacion
    def getMontoLicitacion(self):
        return self.getCuotasLicitacion()*self.getValorCuota()
    def getValorCuota(self):
        return self.getValor()/self.getCantidadCuotas() + self.getValor() * 0.10
    def __str__(self):
        return 'Modelo: {} Versión: {} Valor de Vehículo: {} Valor de la cuota: {}'.format(self.__modelo, self.__version, self.__valor, self.getValorCuota())
        return s
