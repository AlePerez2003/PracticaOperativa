from federado import Federado
from puntaje import Puntaje
from manejadorEvaluaciones import ManejadorEvaluaciones
from manejadorFederado import ManejadorFederado
import csv

if __name__ == '__main__':
    MF = ManejadorFederado()
    MF.cargar_federados()
    ME = ManejadorEvaluaciones()
    ME.cargar_evaluaciones()
    print('Requisito N°1')
    ME.listar_estilo(MF)
    print('')
    
    print('Requisito N°2')
    ME.mostrar_maximo(MF)
    print('')
    
    print('Requsito N°3')
    ME.mostrar_libre(MF)
    ME.mostrar_escuela(MF)
    print('')
    
    print('Requisito N°4')
    ME.mostrar_valoracion()
    print('')