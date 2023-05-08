from puntaje import Puntaje
from federado import Federado
from manejadorFederado import ManejadorFederado
import csv


class ManejadorEvaluaciones:
    __evaluaciones = []
    
    def __init__(self):
        self.__evaluaciones = []
        
    def cargar_evaluaciones(self):
        with open('evaluacion.csv','r')as file:
            reader = csv.reader(file, delimiter = ';')
            for fila in reader:
                unPuntaje = Puntaje(fila[0], fila[1], float(fila[2]), float(fila[3]), float(fila[4]))
                self.__evaluaciones.append(unPuntaje)
            print('Las evaluaciones fueron cargadas exitosamente')
            
    def get_valoracion(self, pos)->Puntaje:
        return self.__evaluaciones[pos]
            
    def buscar_valoración(self, dni, estilo)->int:
        i=0
        valorRetorno = -1
        Bandera = False
        while i < len(self.__evaluaciones) and not Bandera:
            if self.__evaluaciones[i].get_dni() == dni and self.__evaluaciones[i].get_presentacion() == estilo:
                    Bandera = True
                    valorRetorno = i
            else:
                i+=1
        return valorRetorno        
            
    def listar_estilo(self, MF:ManejadorFederado):
        estilo = input('Ingrese el estilo a mostrar')
        edad = int(input('Ingrese la edad de los participantes a mostrar'))
        print('Federados de {} años del estilo {}:'.format(edad, estilo))
        for evaluacion in self.__evaluaciones:
            if evaluacion.get_presentacion() == estilo:
                unFederado = MF.get_federado(evaluacion.get_dni())
                if unFederado.get_edad() == edad:
                    print('Nombre y Apellido:',unFederado.get_nya())
                    print('DNI:{}',unFederado.get_dni())
                    print('')
                
    def max_valoracion(self)->Puntaje:
        maximo = self.__evaluaciones[0]
        for puntaje in self.__evaluaciones:
            if puntaje > maximo:
                maximo = puntaje
        return maximo
    
    def mostrar_maximo(self, MF:ManejadorFederado):
        maxValoracion = self.max_valoracion()
        dni = maxValoracion.get_dni()
        maxFederado = MF.get_federado(dni)
        print('Datos del patinador con mayor puntuación')
        print('Nombre y Apellido: ',maxFederado.get_nya())
        if maxValoracion.get_presentacion() == 'E':
            print('Estilo: Escuela')
        elif maxValoracion.get_presentacion() == 'L':
            print('Estilo: Libre')
        print('Club: ',maxFederado.get_club())
        print('')
        
    def mostrar_libre(self, MF:ManejadorFederado):
        print('Patinadores estilo "Libre"')
        for estilo in self.__evaluaciones:
            if estilo.get_presentacion() == 'L':
                dni = estilo.get_dni()
                FederadoLibre = MF.get_federado(dni)
                print('Nombre y Apellido: ',FederadoLibre.get_nya())
                print('DNI: ',FederadoLibre.get_dni())
                print('Edad: {}'.format(FederadoLibre.get_edad()))
                print('Club: ',FederadoLibre.get_club())
                print('')

    def mostrar_escuela(self, MF:ManejadorFederado):
        print('Patinadores estilo "Escuela"')
        for estilo in self.__evaluaciones:
            if estilo.get_presentacion() == 'E':
                dni = estilo.get_dni()
                FederadoLibre = MF.get_federado(dni)
                print('Nombre y Apellido: ',FederadoLibre.get_nya())
                print('DNI: ',FederadoLibre.get_dni())
                print('Edad: {}'.format(FederadoLibre.get_edad()))
                print('Club: ',FederadoLibre.get_club())
                print('')
                
    def mostrar_valoracion(self):
        print('Ingrese los siguientes datos')
        dni = input('Ingrese el DNI del patinador')
        estilo = input('Ingrese el Estilo a mostrar')
        pos = self.buscar_valoración(dni, estilo)
        unPuntaje = self.get_valoracion(pos)
        print('Valoraciones del participante con DNI ',unPuntaje.get_dni())
        unPuntaje.mostrar_valoracion()

        
