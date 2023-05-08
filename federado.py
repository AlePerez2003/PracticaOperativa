class Federado:
    __apellido: str
    __nombre: str
    __dni: str
    __edad: int
    __club: str
    
    def __init__(self, apellido, nombre, dni, edad, club):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = dni
        self.__edad = edad
        self.__club = club
        
    def get_apellido(self):
        return self.__apellido
    
    def get_nombre(self):
        return self.__nombre
    
    def get_dni(self):
        return self.__dni
    
    def get_edad(self):
        return self.__edad
    
    def get_club(self):
        return self.__club
    
    def get_nya(self):
        return self.__nombre + '' + self.__apellido
    
    