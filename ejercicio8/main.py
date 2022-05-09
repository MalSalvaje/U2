from claseconjunto import Conjunto

if __name__=='__main__':
    a=Conjunto()
    b=Conjunto()
    num=int(input('Ingrese numero natural para agregarlo al conjunto A:'))
    while num!= 0:
        a.agregarElemento(num)
        num=int(input('Ingrese numero natural para agregarlo al conjunto A:'))
    num=int(input('Ingrese numero natural para agregarlo al conjunto B:'))
    while num!= 0:
        b.agregarElemento(num)
        num=int(input('Ingrese numero natural para agregarlo al conjunto B:'))
    print('El conjunto A tiene {} elementos:\n'.format(a.getLength()))
    if(a==b):
        print('Ambos conjuntos son iguales')
    else:
        print('Los conjuntos no son iguales')
    #a.mostrar()
    pos=int(input('Ingrese indice para mostrar elemento en esa posicion de A:'))
    print(a.getElemento(pos))
    nuevo=a-b
    print('La resta de A y B es:\n')
    #print(nuevo)
    nuevo.mostrar()



