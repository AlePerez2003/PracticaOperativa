class Puntaje:
    __dni: str
    __presentacion: str
    __valoracion = []
    
    def __init__(self, dni, presentacion, v1:float, v2:float, v3:float):
        self.__dni = dni
        self.__presentacion = presentacion
        self.__valoracion = []
        self.__valoracion.append(v1)
        self.__valoracion.append(v2)
        self.__valoracion.append(v3)
        
    def get_dni(self):
        return self.__dni
    
    def get_presentacion(self):
        return self.__presentacion
    
    def calculo_valoracion(self)->float:
        acumNota = 0
        for puntaje in self.__valoracion:
            acumNota+=puntaje
        return acumNota/3
    
    def mostrar_valoracion(self):
        i = 1
        for puntaje in self.__valoracion:
            print('Juez {}: {}'.format(i, puntaje))
            i+=1
    
    def __gt__(self, otroPuntaje):
        return self.calculo_valoracion() > otroPuntaje.calculo_valoracion()
    