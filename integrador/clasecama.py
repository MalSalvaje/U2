class Cama:
    __idCama= None
    __habitacion= None
    __estado= None
    __nombre= None
    __diagnostico= None
    __fechaInternacion= None
    __fechaAlta= None
    
    def __init__(self, idCama, habitacion, estado, nombre, diagnostico, fechaInternacion, fechaAlta= None):
        self.__idCama = idCama
        self.__habitacion= habitacion
        self.__estado = estado
        self.__nombre= str(nombre)
        self.__diagnostico= str(diagnostico)
        self.__fechaInternacion= fechaInternacion
        self.__fechaAlta=fechaAlta

    def getIdCama(self):
        return self.__idCama

    def getHabitacion(self):
        return self.__habitacion

    def getEstado(self):
        return self.__estado
    
    def getNombre(self):
        return self.__nombre

    def getDiagnostico(self):
        return self.__diagnostico
    
    def getFechaInternacion(self):
        return self.__fechaInternacion

    def getFechaAlta(self):
        return self.__fechaAlta

    def alta(self, fechaAlta):
        self.__fechaAlta=fechaAlta
        self.__estado= False

    def __str__(self):
        cadena='Paciente {} Cama: {} Habitacion: {} Diagnostico: {} Fecha de Internacion: {} Fecha de Alta: {}\n'.format(self.getNombre(), self.getIdCama(), self.getHabitacion(), self.getDiagnostico(), self.getFechaInternacion(), self.getFechaAlta())
        return cadena
