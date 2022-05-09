from claseconjunto import Conjunto\

class Menu:
    __switcher:None
    
    def __init__(self):
        self.__switcher ={  '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.salir
                         }
