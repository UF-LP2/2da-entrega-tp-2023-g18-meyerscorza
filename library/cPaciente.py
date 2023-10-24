
import random
from enum import Enum

class cGravedad(Enum):
    blanco=0
    rojo=1
    naranja=2
    amarillo=3
    verde=4
    azul=5

#creamos enum para crear diagnosticos
class cDiagnostico(Enum):
    paro_cardiaco=0
    insuficiencia_respiratoria_grave=1
    politraumatismo_grave = 2
    coma = 3
    convulsiones = 4
    hemorragia_digestiva = 5
    isquemia = 6
    cefalea_brusca = 7
    paresia = 8
    hipertensión_arterial = 9
    vértigo_con_afectación_vegetativa = 10
    síncope = 11
    urgencias_psiquiátricas = 12
    Otalgias = 13
    odontologías = 14
    dolor_leve = 15
    traumatismo = 16
    esguince = 17
    Tos = 18
    cefalea_leve = 19
    resfriado = 20

class cPaciente:
    def __init__(self,hora_de_llegada:int, edad:int): #constructor en el primer momento que llega el paciente al hospital
        self.hora_de_llegada = hora_de_llegada
        self.edad = edad
        self.gravedad = 0 #por defecto es blanco; 
        self.diagnostico=None #defecto
        self.tiempo_de_vida =-1 #por defecto
        
    def Asignar_diag_Random(self):
        # hacemos random para detertminar el diagnostico del paciente,en este enum estaran //cargadas todas las enfermedades
        diag = random.randrange(len(cDiagnostico))
        self.settear(diag)
        
    
    def settear (self,diag):
        self.diagnostico=diag
    
