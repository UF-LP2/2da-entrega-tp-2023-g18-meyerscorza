from src.cPaciente import cPaciente
from datetime import datetime # modulo de python para poder calcular lo hora actual


class cHospital:
    def __init__(self):
        self.lista_urgentes = []          # Lista de pacientes urgentes (inicializo en vacío)
        self.lista_no_urgentes = []      # Lista de pacientes no urgentes (inicializo en vacío)
        self.lista_enfermeros = []        # Lista de enfermeros disponibles (inicializo en vacío)

    def cargar_listas(self,pac:cPaciente):
        if pac.gravedad == "rojo":
            pac.tiempo_de_vida=0
            self.lista_urgentes.append(pac)
        else:
            pac.tiempo_de_vida=pac.calcular_tiempo_de_vida(pac)#funcion que calcula cuanto tiempo le queda
            self.lista_no_urgentes.append(pac)
            self.ordenar_no_urgentes()
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
                self.asignacion_paciente(pac, lista_enfermeros_actuales[i])#pongo como atributo de enfermero el paciente
                #PONER FUNCION TIEMPO DE ATENCION
                #ahora terminaria la consulta
                self.eliminar_pac(pac)#funcion que elimina el paciente de su respectiva lista
                self. setear_disponibilidad(lista_enfermeros_actuales[i], True)  # ahora se supone que se libero
                cont += 1
            i+=1
        if cont == 0:#significa que todos los enfermeros estan ocupados, caso extremo
            print("Espere a ser atendido, todos nuestros enfermeros estan ocupados")

    def Enf_actuales(self):
        momento_del_dia = self.momento_dia()  #funcion que devuelve, maniana,tarde,noche o madrugada
        lista_enf_disp = []
        for i in self.lista_enfermeros:
            if self.lista_enfermeros[i].horario_atencion == momento_del_dia:
                lista_enf_disp.append(self.lista_enfermeros[i])
        return lista_enf_disp

    '''def momento_dia():
        moment= random.randrange(len(cTurno))
        return moment'''
    
    def setear_disponibilidad(self,enfermero,variable_bool):
        enfermero.disponibilidad=variable_bool

    def eliminar_pac(self,pac):
        #no se en cual de las dos de las lista esta, entocnes ponemos esas condiciones
        if pac in self.lista_urgentes:
            self.lista_urgentes.remove(pac)
        else:
            self.lista_no_urgentes.remove(pac)
    
    #ALGORITMO DE GREEDY
    '''def SeleccionGreedy(self):
        #las lista_no_urgente esta ordenada por tiempo que le quedan de vida a los pacientes
         
    '''

    #ALGORITMO PROG DINAMICA
    def SeleccionProgDinamica(cantEnfer,beneficio,Npacientes,pacientes):
         # Crear una matriz K de (Npacientes + 1) x (cantEnfer + 1) inicializada con ceros
        K = [[0 for x in range(cantEnfer + 1)] for x in range(Npacientes + 1)]

        # Construir la matriz de manera ascendente
        for i in range(Npacientes + 1):  # Recorrer filas
            for w in range(cantEnfer + 1):  # Recorrer columnas
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif pacientes[i - 1] <= w:
                    K[i][w] = min(beneficio[i - 1] + K[i - 1][w - pacientes[i - 1]], K[i - 1][w])
                    #minimizo incluyendo a ese paciente y no incluyendolo,seria el de menor tiempo de espera
                else: #no tengo suficientes enfermeros para hacer atendido ahora
                    #no lo incluyo
                    K[i][w] = K[i - 1][w]

        return K  # Devolver la matriz K

    def calcular_tiempo_de_vida(self,pac):
        hora_actual = self.VerificarHorario()  # Debes obtener la hora actual de alguna manera

        tiempo_que_paso_desde_que_llego = hora_actual - pac.hora_llegada

        if pac.gravedad == "naranja":
            pac.tiempo_de_vida = 30 - tiempo_que_paso_desde_que_llego.total_seconds() / 60 #lo paso a minutos ya que opero con minutos
        elif pac.gravedad == "amarillo":
            pac.tiempo_de_vida = 60 - tiempo_que_paso_desde_que_llego.total_seconds() / 60
        elif pac.gravedad == "verde":
            pac.tiempo_de_vida = 120 - tiempo_que_paso_desde_que_llego.total_seconds() / 60
        elif pac.gravedad == "azul":
            pac.tiempo_de_vida = 240 - tiempo_que_paso_desde_que_llego.total_seconds() / 60

    def VerificarHorario(self):
        hora_actual=datetime.now()
        return hora_actual