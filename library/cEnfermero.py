import cPaciente

class cEnfermero:
    def __init__(self,disponibilidad,horario_atencion,pac):
        self.disponibilidad = disponibilidad
        self.horario_atencion= horario_atencion
        self.pac=pac
        
    def asignar_gravedad(self,p):
        #en base a los diagnosticos, me le asigno un color de gravedad
        if 0 <= p.diagnostico <= 2:
            p.gravedad = "rojo"
        elif 3 <= p.diagnostico <= 6:
            p.gravedad = "naranja"
        elif 7 <= p.diagnostico <= 12:
            p.gravedad = "amarillo"
        elif 13 <= p.diagnostico <= 17:
            p.gravedad = "verde"
        elif 18 <= p.diagnostico <= 20:
            p.gravedad = "azul"
        else:
            p.gravedad = None
