from datetime import datetime
class cPaciente:
    def __init__(self,id:int, nacimiento:datetime,nombre:str,apellido:str,sin1:str,sin2:str,sin3:str): #constructor en el primer momento que llega el paciente al hospital
        self.hora_de_llegada = datetime(2023, 10, 24, 0, 0, 0)
        self.nacimiento=nacimiento
        self.gravedad = "blanco"
        self.tiempo_de_vida = -1
        self.nombre=nombre
        self.idPaciente=id
        self.apellido=apellido
        self.sintoma1=sin1
        self.sintoma2=sin2
        self.sintoma3=sin3
    
        
    def getnacimiento(self):
        return self.nacimiento
    
    def settear (self,diag):
        self.diagnostico=diag
    
