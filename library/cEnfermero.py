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
       #asigno hora de llegada al paciente ES EL NOW

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

        self.hospital.cargar_listas(paciente)
 