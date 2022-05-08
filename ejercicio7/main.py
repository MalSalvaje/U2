from manejador import Manejador

if __name__=='__main__':
    unmanejador=Manejador()
    unmanejador.leerarchivo()
    unmanejador.comparar()
    unmanejador.encontrarMaximo()
    cod=int(input('Ingrese numero de viajero para acumular millas:'))
    unmanejador.ingresamillas(cod) 
    cod=int(input('Ingrese numero de viajero para restar millas:'))
    unmanejador.restamillas(cod) 
    unmanejador.verificar() 
