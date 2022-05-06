import csv
from claseregistro import Registro

class Manejador:
    __lista=[[],[],[],[]]
    def agregarregistro(self, unregistro):
        self.__lista[unregistro.retornadia()-1].append(unregistro)
    def leearchivo(self):
       archivo=open('registros.csv')
       reader=csv.reader(archivo,delimiter=',')
       for fila in reader:
           d=fila[0]
           h=fila[1]
           m=fila[2]
           temp=fila[3]
           hum=fila[4]
           pres=fila[5]
           unregistro=Registro(d,h,m,temp,hum,pres)
           self.agregarregistro(unregistro)   
    def mostrardia(self):
        dia=int(input('Ingrese numero de dia a mostrar:'))
        for registro in self.__lista[dia-1]:
            print(registro)
    def mostrarmin(self):
        mint=9999
        minh=9999
        minp=9999
        for dia in self.__lista:
            for hora in dia:
                if hora.retornatemperatura()<mint:
                    mint=hora.retornatemperatura()
                    post=hora.retornadia()
                    ht=hora.retornahora()
                if hora.retornahumedad()<minh:
                    minh=hora.retornahumedad()
                    posh=hora.retornadia()
                    hh=hora.retornahora()
                if hora.retornapresion()<minp:
                    minp=hora.retornapresion()
                    posp=hora.retornadia()
                    hp=hora.retornahora()
        print('La menor temperatura fue de {} C. Se alcanzo el dia {} a las {} horas.\n'.format(mint, post, ht.strftime("%M:%S")))
        print('La menor humedad fue de {} %. Se alcanzo el dia {} a las {} horas.\n'.format(minh, posh, hh.strftime('%M:%S')))
        print('La menor presion fue de {} HPa. Se alcanzo el dia {} a las {} horas.\n'.format(minp, posp, hp.strftime('%M:%S')))
    def promedioporhora(self):
        for i in range(4):
            acum=0
            for dia in self.__lista:
                acum+=dia[i].retornatemperatura()
            prom=acum/len(self.__lista)
            hora=dia[i].retornahora()
            print('El promedio de temperatura para la hora {} fue de {}C durante este mes.'.format(hora.strftime('%M:%S'), prom))

