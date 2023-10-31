from src.cPaciente import cPaciente
from library.cHospital import cHospital
from typing import List
class cEnfermero:
    def __init__(self,id:int,nombre:str,apellido:str):
        self.nombre=nombre
        self.disponibilidad = True
        self.id=id
        self.apellido=apellido
        self.pac=None
        self.hospital = cHospital()
    def asignar_gravedad(self,paciente:cPaciente):
        #en base a los diagnosticos, me le asigno un color de gravedad
       #asigno hora de llegada al paciente

        if 0 <= paciente.diagnostico <= 2:
            paciente.gravedad = 1
        elif 3 <= paciente.diagnostico <= 6:
            paciente.gravedad = 2
        elif 7 <=paciente.diagnostico <= 12:
            paciente.gravedad = 3
        elif 13 <= paciente.diagnostico <= 17:
            paciente.gravedad = 4
        elif 18 <= paciente.diagnostico <= 20:
            paciente.gravedad = 5
        else:
            paciente.gravedad = None
        #random de hora para cada color, si es amarillo random entre 0 y 30 y asi con todos
        #mi UNICO PROBLEMA VA A SER QUE ENTRE LOS QUE SON DE UN MISMO COLOR NOS HALLA UNO QUE ENTRE DESPUES Y TENGA MENOR HORA DE LLEGADA SERIA ILOGICO
        # aca podriamos asignar el tiempo de ahora pero sumarle siempre algo para que la diferencia no se en nanosegundos de tiempo de ejecucion
        self.hospital.cargar_listas(paciente)
 