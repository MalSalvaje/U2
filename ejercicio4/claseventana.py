class Ventana:
    __titulo= ''
    __xSuperiorIzq = 0
    __ySuperiorIzq = 0
    __xInferiorDer = 0
    __yInferiorDer = 0
    def __init__(self, titulo = '', ax = 0, ay = 0, dx = 500, dy =-500):
        if dy<=500 and dy<ay and ax<dx<=500:
            self.__titulo= titulo
            self.__xSuperiorIzq= ax
            self.__ySuperiorIzq= ay
            self.__xInferiorDer= dx
            self.__yInferiorDer= dy
    def mostrar(self):
        print('Titulo: {} Esquina Superior Izquierda ({},{}) Esquina Inferior derecha: ({},{})' .format(self.__titulo, self.__xSuperiorIzq, self.__ySuperiorIzq, self.__xInferiorDer, self.__yInferiorDer)) 
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return int(self.__ySuperiorIzq) - int(self.__yInferiorDer)
    def ancho(self):
        return int(self.__xInferiorDer) - int(self.__xSuperiorIzq)
    def moverDerecha(self, u=1):
        self.__xSuperiorIzq+=u
        self.__xInferiorDer+=u
    def moverIzquierda(self, u=1):
        self.__xSuperiorIzq-=u
        self.__xInferiorDer-=u
    def subir(self, u=1):
        self.__ySuperiorIzq+=u
        self.__yInferiorDer+=u
    def bajar(self, u=1):
        self.__ySuperiorIzq-=u
        self.__yInferiorDer-=u
    
