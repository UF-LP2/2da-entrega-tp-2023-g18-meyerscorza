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
        
    def asignar_gravedad(self,paciente:cPaciente,Hospital:cHospital):
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

        Hospital.cargar_listas(paciente)
    
    def set_disponibilidad(self,a:bool):
        self.disponibilidad=a
 
    def AsignoGravedadGreedy(self,paciente:cPaciente):
        #entre los 3 sintomas que tiene el paciente tengo que ver el mas grave y en relacion a ese elijo el color
        color=self.colorSintomaGrave(paciente)
    
    def colorSintomaGrave(paciente:cPaciente):
        listarojo={"paro_cardiaco","insuficiencia_respiratoria_grave","politraumatismo_grave"}
        listanaranja={"coma","convulsiones","hemorragia_digestiva","isquemia"}
        listaamarillo={"cefalea_brusca","paresia","hipertensión_arterial","vértigo_con_afectación_vegetativa","síncope","urgencias_psiquiátricas"}
        listaverde={"otalgias","odontologías","dolor_leve","traumatismo","esguince"}
        listaazul={"tos","cefalea_leve","resfriado"}
        
        if paciente.sintoma1 in listarojo or paciente.sintoma2 in listarojo or paciente.sintoma3 in listarojo:
            #alguno de los sintomas representa al rojo
            return "rojo"
        elif paciente.sintoma1 in listanaranja or paciente.sintoma2 in listanaranja or paciente.sintoma3 in listanaranja:
            #alguno de los sintomas representa al naranja 
            return "naranja"
        elif paciente.sintoma1 in listaamarillo or paciente.sintoma2 in listaamarillo or paciente.sintoma3 in listaamarillo:
            #alguno de los sintomas representa al amarillo
            return "amarillo"
        elif paciente.sintoma1 in listaverde or paciente.sintoma2 in listaverde or paciente.sintoma3 in listaverde:
            #alguno de los sintomas representa al verde
            return "verde"
        elif paciente.sintoma1 in listaazul or paciente.sintoma2 in listaazul or paciente.sintoma3 in listaazul:
            #alguno de los sintomas representa al azul
            return "azul"
        
        