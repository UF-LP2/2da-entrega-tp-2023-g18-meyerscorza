
from src.cPaciente import cPaciente

class cEnfermero:
    def __init__(self, id: int, nombre:str, apellido:str,disp:bool):
        self.nombre = nombre
        self.disponibilidad=disp
        self.id = id
        self.apellido = apellido
    
    def set_disponibilidad(self):
        if(self.disponibilidad==True):
            self.disponibilidad = False
        else:
            self.disponibilidad = True

    def getDisp(self):
        return self.disponibilidad
    
    def AsignoGravedadGreedy(self,paciente:cPaciente):
        #entre los 3 sintomas que tiene el paciente tengo que ver el mas grave y en relacion a ese elijo el color
        color = self.colorSintomaGrave(paciente)
        paciente.gravedad=color

    def colorSintomaGrave(self,paciente:cPaciente):
        listarojo={"paro_cardiaco","insuficiencia_respiratoria_grave","politraumatismo_grave"}
        listanaranja={"coma","convulsiones","hemorragia_digestiva","isquemia"}
        listaamarillo={"cefalea_brusca","paresia","hipertensión_arterial","vertigo_con_afectación_vegetativa","sincope","urgencias_psiquiatricas"}
        listaverde={"otalgias","odontologias","dolor_leve","traumatismo","esguince"}
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
        
        