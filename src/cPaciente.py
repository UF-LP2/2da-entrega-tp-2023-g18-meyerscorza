from datetime import datetime
class cPaciente:
    def __init__(self,id:int, nacimiento:str,nombre:str,apellido:str,sin1:str,sin2:str,sin3:str): #constructor en el primer momento que llega el paciente al hospital
        self.hora_de_llegada = datetime.strptime("00:00:00", "%H:%M:%S")
        self.nacimiento=nacimiento
        self.gravedad = "blanco"
        self.diagnostico=None #defecto
        self.tiempo_de_vida =-1 #por defecto
        self.nombre=nombre
        self.idPaciente=id
        self.apellido=apellido
        self.sintoma1=sin1
        self.sintoma2=sin2
        self.sintoma3=sin3
        

    def settear (self,diag):
        self.diagnostico=diag
    
