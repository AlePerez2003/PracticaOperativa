from federado import Federado
import csv


class ManejadorFederado:
    __federados = []
    
    def __init__(self):
        self.__federados = []
        
    def cargar_federados(self):
        with open('federados.csv','r')as file:
            reader = csv.reader(file, delimiter = ';')
            for fila in reader:
                unFederado = Federado(fila[0], fila[1], fila[2], int(fila[3]), fila[4])
                self.__federados.append(unFederado)
            print('Las evaluaciones fueron cargadas exitosamente')
            
    def buscar_federado(self, dni)->int:
        i=0
        valorRetorno = -1
        Bandera = False
        while i < len(self.__federados) and not Bandera:
            if self.__federados[i].get_dni() == dni:
                Bandera = True
                valorRetorno = i
            else:
                i+=1
        return valorRetorno
    
    def get_federado(self, dni)->Federado:
        pos = self.buscar_federado(dni)
        return self.__federados[pos]