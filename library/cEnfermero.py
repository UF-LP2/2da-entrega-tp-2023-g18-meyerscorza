from library.cPaciente import cPaciente
from enum import Enum

class cTurno(Enum):
    maniana=0
    tarde=1
    noche=2
    madrugada=3

class cEnfermero:
    def __init__(self,disponibilidad:bool,horario_atencion:cTurno):
        self.disponibilidad = disponibilidad
        self.horario_atencion= horario_atencion
        self.pac=None
    
    def asignar_gravedad(self,p:cPaciente):
        #en base a los diagnosticos, me le asigno un color de gravedad
        if 0 <= p.diagnostico <= 2:
            p.gravedad = 1
        elif 3 <= p.diagnostico <= 6:
            p.gravedad = 2
        elif 7 <= p.diagnostico <= 12:
            p.gravedad = 3
        elif 13 <= p.diagnostico <= 17:
            p.gravedad = 4
        elif 18 <= p.diagnostico <= 20:
            p.gravedad = 5
        else:
            p.gravedad = None

