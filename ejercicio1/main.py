from claseemail import Email
import csv

def main():
            archivo=open('datos.csv')
            reader=csv.reader(archivo, delimiter=';')
            for fila in reader:
                    for columna in fila:
                        nombre=columna
                        nombre= Email('','','','')
                        nombre.creardir(columna)
                        nombre.retornamail()

            mailprueba = Email('marco','gmail','com','regadera')
            mailprueba.retornamail()
            mailprueba.getDominio()
            cuenta1 = Email('','','','')
            cuenta1.crearCuenta()
            cuenta1.modificaPassword()
            cuenta2= Email('','','','')
            completo=input('\tIngrese direccion para crear nueva cuenta:')
            cuenta2.creardir(completo)
            cuenta2.retornamail()
            cuenta2.getDominio()
            


if __name__=='__main__':
    main()
