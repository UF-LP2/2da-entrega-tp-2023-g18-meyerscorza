from collections import deque
import random
from enum import Enum

#ver donde se inicializa cada cosa
class cPaciente:
    def __init__(self, gravedad, tiempo_de_vida, hora_de_llegada, edad, diagnostico):
        self.gravedad = gravedad
        self.tiempo_de_vida = tiempo_de_vida
        self.hora_de_llegada = hora_de_llegada
        self.edad = edad
        self.diagnostico = diagnostico

class cParamedico:
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

class cEnfermero:
    def __init__(self,disponibilidad,horario_atencion,pac):
        self.disponibilidad = disponibilidad
        self.horario_atencion= horario_atencion
        self.pac = pac #paciente que atiende
class cHospital:
    def __init__(self):
        self.multicola = deque()          # Cola para pacientes en espera
        self.lista_urgentes = []          # Lista de pacientes urgentes
        self.lista_no_urgentes = []       # Lista de pacientes no urgentes
        self.lista_enfermeros = []        # Lista de enfermeros disponibles

    def cargar_listas(self,pac):
        if pac.gravedad == "rojo":
            pac.tiempo_de_vida=0
            self.lista_urgentes.append(pac)
        else:
            pac.tiempo_de_vida=calcular_tiempo_de_vida(pac)#funcion que calculara el tiempo que le queda, en el main, se le debe asignar un horario de llegada
            self.lista_no_urgentes.append(pac)

    def ordenar_no_urgentes(self): #como no son urgentes, los debo atender por tiempo de vida, pero deben ser ordenadoa por tiempo de vida
            for i in range(1, len(self.lista_no_urgentes)):
                key = self.lista_no_urgentes[i]
                j = i - 1

                while j >= 0 and self.lista_no_urgentes[j].tiempo_de_vida > key.tiempo_de_vida:
                    self.lista_no_urgentes[j + 1] = self.lista_no_urgentes[j]
                    j = j - 1
                self.lista_no_urgentes[j + 1] = key

    def disp_enfermeros(self):
        i=0
        cont= 0
        lista_enfermeros_actuales=self.Enf_actuales()#tengo lista de los enfermeros disponibles
        while i< len(lista_enfermeros_actuales):#recorro la nueva lista
            if  (lista_enfermeros_actuales[i].disponibilidad==True): #si esta libre
                pac=self.seleccion_pacientes()#atiende pac, elije por gryddy o por programacion dinamica
                self.setear_disponibilidad(lista_enfermeros_actuales[i],False)#ahora esta ocupado
                self. asignacion_paciente(pac, lista_enfermeros_actuales[i])#pongo como atributo de enfermero el paciente
                #PONER FUNCION TIEMPO DE ATENCION
                #ahora terminaria la consulta
                self.eliminar_pac(pac)#funcion que elimina el paciente de su respectiva lista
                self. setear_disponibilidad(lista_enfermeros_actuales[i], True)  # ahora se supone que se libero
                cont += 1
            i+=1
        if cont == 0:#significa que todos los enfermeros estan ocupados, caso extremo
            print("Espere a ser atendido, todos nuestros enfermeros estan ocupados")

    def Enf_actuales(self):
        momento_del_dia = momento_dia()  #funcion que devuelve, maniana,tarde,noche o madrugada
        lista_enf_disp = []
        for i in self.lista_enfermeros:
            if self.lista_enfermeros[i].horario_atencion == momento_del_dia:
                lista_enf_disp.append(self.lista_enfermeros[i])
        return lista_enf_disp

    def  setear_disponibilidad(self,enfermero,variable_bool):
        enfermero.disponibilidad=variable_bool

    def asignacion_paciente(self,pac,enf):
        enf.paciente(pac)

    def eliminar_pac(self,pac):
        #no se en cual de las dos de las lista esta, entocnes ponemos esas condiciones
        if pac in self.lista_urgentes:
            self.lista_urgentes.remove(pac)
        else:
            self.lista_no_urgentes.remove(pac)
def calcular_tiempo_de_vida(pac):
    hora_actual = VerificarHorario()  # Debes obtener la hora actual de alguna manera

    tiempo_que_paso_desde_que_llegue = hora_actual - pac.hora_llegada

    if pac.gravedad == "naranja":
        pac.tiempo_de_vida = 30 - tiempo_que_paso_desde_que_llegue
    elif pac.gravedad == "amarillo":
        pac.tiempo_de_vida = 60 - tiempo_que_paso_desde_que_llegue
    elif pac.gravedad == "verde":
        pac.tiempo_de_vida = 120 - tiempo_que_paso_desde_que_llegue
    elif pac.gravedad == "azul":
        pac.tiempo_de_vida = 240 - tiempo_que_paso_desde_que_llegue


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

# la siguiente funcion iria en el main para ponerle el atributo diagnositco a los pacientes
def Asignar_enfermedad_Random(pac):
    # hacemos random para detertminar la enfermedad del paciente,en este enum estaran //cargadas todas las enfermedades
    diag = random.randrange(len(cDiagnostico))
    pac.diagostico(diag)
    paramedico=cParamedico()
    paramedico.asignar_gravedad(pac)

 #hago algoritmo griddy

