class Email:
    # Atributos privados de la clase
    __id_cuenta=''
    __dominio=''
    __tipo_dominio=''
    __passw=''
    # Métodos públicos de la clase
    def __init__(self, id_cuenta, dominio, tipo_dominio, passw):
        self.__id_cuenta = id_cuenta
        self.__dominio = dominio
        self.__tipo_dominio= tipo_dominio
        self.__passw= passw

    def retornamail(self): # self hace referencia al objeto que envía el mensaje
        mail=self.__id_cuenta+'@'+self.__dominio+'.'+self.__tipo_dominio
        print(mail)
    def getDominio(self):
        return self.__dominio
    
    def crearCuenta(self):
        print("\n CREACION DE CUENTA \n")
        nombre = input("\tIngrese su nombre: ")
        id_cuen = input("\tIngrese nombre de la cuenta: ")
        nuevo_dom = input("\tIndique dominio: ")
        nuevo_tipo_dom = input("\tIndique tipo de dominio: ")
        npass = input("\tEscriba Contraseña: ");
        vernpass = input("\tVuelva a ingresar la contraseña: ")
        if npass == vernpass:
            self.__id_cuenta = id_cuen
            self.__dominio = nuevo_dom
            self.__tipo_dominio = nuevo_tipo_dom
            self.__password = npass
            print("\n\tEstimadx "+nombre+", Su cuenta de mail ha sido creada: "+self.__id_cuenta+"@"+self.__dominio+'.'+self.__tipo_dominio)
        else:
            print("\n ¡Las contraseñas no coinciden!. ¡Por favor Verifique nuevamente! \n")
    def modificaPassword(self):
        print("\n ***** Cambio de Contraseña ***** \n")
        ver_pass = input("\tIntroduzca Contraseña anterior:")
        while ver_pass != self.__password:
            ver_pass = input("\tContraseña inválida. Vuelva a introducir Contraseña anterior:")
        nuevo_pass=input('\tIntroduzca contraseña nueva:')
        vernpass=input('\tConfirme contraseña nueva:')
        while vernpass != nuevo_pass:
            vernpass=input('\tLas contraseñas no coinciden. Vuelva a confirmar contraseña:')
        self.__password = vernpass
        print('\tLa contraseña se cambió correctamente')
    def creardir(self, full):
            frac=full.split('@')
            if len(frac)!= 2:
                raise Exception("Se proporcionó una dirección de mail no válida")
            else: 
                frac2=frac[1].split('.')
                if len(frac2)!=2:
                    raise Exception("Se proporcionó una dirección de mail no válida")
                else:
                    ps=input('\tIngrese password de su nueva cuenta:')
                    vps=input('\tConfirme password de su nueva cuenta:')
                    while vps != ps:
                        vps=input('\tLas contraseñas no coinciden. Confirme password:')
                    self.__id_cuenta=frac[0]
                    self.__dominio=frac2[0]
                    self.__tipo_dominio=frac2[1]
                    self._password=vps
            print('\t Su cuenta ha sido creada:\n')
 
