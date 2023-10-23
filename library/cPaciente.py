
import random
import cDiagnostico

class cPaciente:
    def Asignar_diag_Random()-> cDiagnostico:
        # hacemos random para detertminar el diagnostico del paciente,en este enum estaran //cargadas todas las enfermedades
        diag = random.randrange(len(cDiagnostico))
        return diag
     
    def __init__(self, gravedad, tiempo_de_vida, hora_de_llegada, edad, diagnostico):
        self.tiempo_de_vida = self.calcular_tiempo_de_vida
        self.hora_de_llegada = hora_de_llegada
        self.edad = edad
        self.diagnostico = self.Asignar_diag_Random()
        self.gravedad = gravedad

    '''def calcular_tiempo_de_vida(pac):
        hora_actual = VerificarHorario()  # Debes obtener la hora actual de alguna manera

        tiempo_que_paso_desde_que_llegue = hora_actual - pac.hora_llegada

        if pac.gravedad == "naranja":
            pac.tiempo_de_vida = 30 - tiempo_que_paso_desde_que_llegue
        elif pac.gravedad == "amarillo":
            pac.tiempo_de_vida = 60 - tiempo_que_paso_desde_que_llegue
        elif pac.gravedad == "verde":
            pac.tiempo_de_vida = 120 - tiempo_que_paso_desde_que_llegue
        elif pac.gravedad == "azul":
            pac.tiempo_de_vida = 240 - tiempo_que_paso_desde_que_llegue '''