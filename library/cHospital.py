import random
from datetime import datetime,timedelta
from src.cPaciente import cPaciente
from library.cEnfermero import cEnfermero
class cHospital:
    def __init__(self, hora_actual: datetime):
        self.lista_urgentes = []          # Lista de pacientes urgentes (inicializo en vacío)
        self.lista_no_urgentes = []      # Lista de pacientes no urgentes (inicializo en vacío)
        self.lista_enfermerosDisp = []     # Lista de enfermeros disponibles (inicializo en vacío)
        self.lista_enfermeros=[]            #utilizo para cuando leeo el archivo
        self.lista_pacientesTotales=[]      #utilizo para cuando leeo el archivo
        self.listaPD=[]    #para programacion dinamica
        self.hora_actual = hora_actual  # Almacena la hora_actual como atributo
        self.turno="madrugada"
        self.cont=5 #contador para ir ingresando pacientes

    def cargar_listas(self, pac:cPaciente):#FUNCIONAAA
        if pac.gravedad == "rojo":
            pac.tiempo_de_vida = 0
            self.lista_urgentes.append(pac)
        else:
            self.calcular_tiempo_de_vida(pac)#funcion que calcula cuanto tiempo le queda
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

    def Recorrer_pacientes(self)-> cPaciente: #FUNCIONAAA
        self.cont=self.cont+1
        return self.lista_pacientesTotales[self.cont]

    def disp_enfermeros(self): #FUNCIONA
        i=0
        while i < len(self.lista_enfermerosDisp):#recorro la nueva lista
            if  (self.lista_enfermerosDisp[i].getDisp() == True): #si esta libre
                self.lista_enfermerosDisp[i].set_disponibilidad()  # ahora esta ocupado
                pac=self.Recorrer_pacientes()
                self.lista_enfermerosDisp[i].AsignoGravedadGreedy(pac)
                pac.hora_de_llegada=self.hora_actual
                self.cargar_listas(pac)
                self.cargado_lista_paraPD(pac)
                self.lista_enfermerosDisp[i].set_disponibilidad()  # ahora esta desocupado

            else:#significa que todos los enfermeros estan ocupados, caso extremo
                print("Espere a ser atendido, todos nuestros enfermeros estan ocupados")
            i+=1

    def Enf_actuales(self): #FUNCIONA
        momento_del_dia = self.momento_dia()  #funcion que devuelve, maniana,tarde,noche o madrugada
    
        cant=0
        
        if momento_del_dia =="Madrugada": #elijo solo a 1 
            cant = 1
        elif momento_del_dia=="Maniana": #elijo a 2
            cant = 2
        elif momento_del_dia=="Tarde": #elijo a 5
            cant = 5
        elif momento_del_dia=="Noche": #elijo a 3
            cant = 3
        else:
            raise ValueError("Momento del día no válido")
        i=0
       
        if self.lista_enfermeros: #si no esta vacia la lista entra en este if
                 while i<=cant: #dependiendo del turno llamo a nuevos enfermeros disponibles
                    enfermero_aleatorio = random.choice(self.lista_enfermeros)  # Elige un enfermero aleatorio
                    self.lista_enfermerosDisp.append(enfermero_aleatorio)  # Agrega el enfermero a la lista de enfermeros disp en ese turno del hospital
                    i=i+1
        else:
                raise Exception("No hay enfermeros en la lista")
            

    def momento_dia(self)-> str:#FUNCIONA


        # Define los rangos de tiempo para cada turno
        turno_madrugada= (datetime.strptime("23:00:00", "%H:%M:%S").time(), datetime.strptime("06:00:00", "%H:%M:%S").time())
        turno_maniana = (datetime.strptime("06:00:00", "%H:%M:%S").time(), datetime.strptime("10:00:00", "%H:%M:%S").time())
        turno_tarde = (datetime.strptime("10:00:00", "%H:%M:%S").time(), datetime.strptime("16:00:00", "%H:%M:%S").time())
        turno_noche = (datetime.strptime("16:00:00", "%H:%M:%S").time(), datetime.strptime("23:00:00", "%H:%M:%S").time())

        # Compara la hora actual con los rangos de tiempo y determina el turno
        if turno_noche[0] <= self.hora_actual.time() < turno_noche[1]:# datetime.time es solo hora
            turno = "Noche"
        elif turno_maniana[0] <= self.hora_actual.time() < turno_maniana[1]:
            turno = "Maniana"
        elif turno_tarde[0] <= self.hora_actual.time() < turno_tarde[1]:
            turno = "Tarde"
        else:
            turno = "Madrugada"
        
        return turno
    


    def eliminar_pac(self,pac):
        #no se en cual de las dos de las lista esta, entocnes ponemos esas condiciones
        if pac in self.lista_urgentes:
            self.lista_urgentes.remove(pac)
            if pac in self.listaPD:
                self.listaPD.remove(pac)
        else:
            self.lista_no_urgentes.remove(pac)
            if pac in self.listaPD:
                self.listaPD.remove(pac)
                
    #ALGORITMO DE GREEDY
    def SeleccionGreedy(self):
        # las lista_no_urgente está ordenada por el tiempo que le queda de vida a los pacientes
        empeoraron = self.empeoro_pac_no_urgente()  # devuelve un array con los que empeoraron

        if self.lista_urgentes and len(empeoraron) == 0:
            # Mandamos el primero que es el más urgente, y cuando termina la atención se elimina de la lista
            return self.lista_urgentes[0]
        elif self.lista_urgentes and len(empeoraron) > 0:
            pac = self.dar_prioridad(empeoraron)  # va a tener que dar prioridad entre los más urgentes que empeoraron de la nada
            return pac
        elif not self.lista_urgentes and len(empeoraron) > 0:
            pac = self.dar_prioridad(empeoraron)
            return pac
        else:
            return self.lista_no_urgentes[0]
        
    def dar_prioridad(self, empeoraron):
        if self.lista_urgentes:# si no está vacío, agrega el de la lista de rojo para poder comparar
            empeoraron.append(self.lista_urgentes[0])

        paciente_mas_joven = None# inicializo paciente
        edad_mas_joven = float('4345')# inicializo edad para poder devolver la mínima

        for i in range(len(empeoraron)):
            paciente=empeoraron[i]
            edad_paciente = self.calcular_edad(paciente.getnacimiento())
            if edad_paciente < edad_mas_joven:# comparo si la edad que entra es menor a la anterior
                edad_mas_joven = edad_paciente
                paciente_mas_joven = empeoraron[i]

        return paciente_mas_joven

    def calcular_edad(self, fecha_nacimiento:datetime):
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d %H:%M:%S")
        anionacimiento=fecha_nacimiento.year
        edad = self.hora_actual.year - anionacimiento
        if self.hora_actual.month < fecha_nacimiento.month or (
                self.hora_actual.month == fecha_nacimiento.month and self.hora_actual.day < fecha_nacimiento.day):  # vemos la edad si aún no ha tenido su cumpleaños este año
            edad -= 1# le restamos uno si todavia no cumplio
        return edad

    def empeoro_pac_no_urgente(self):
        empeoraron = []
        for i in range(len(self.lista_no_urgentes)):
            prob_que_empeoro = 0  # Inicializamos la variable

            if self.lista_no_urgentes[i].gravedad == "naranja":
                prob_que_empeoro = random.randint(1, 4)
                if prob_que_empeoro == 1:
                    self.lista_no_urgentes[i].gravedad = "rojo"
                    self.lista_no_urgentes[i].tiempo_de_vida = 0
                    empeoraron.append(self.lista_no_urgentes[i])

            elif self.lista_no_urgentes[i].gravedad == "amarillo":
                prob_que_empeoro = random.randint(1, 100)
                if prob_que_empeoro == 1:
                    self.lista_no_urgentes[i].gravedad = "rojo"
                    self.lista_no_urgentes[i].tiempo_de_vida = 0
                    empeoraron.append(self.lista_no_urgentes[i])
                elif prob_que_empeoro == 2 or prob_que_empeoro == 3:
                    self.lista_no_urgentes[i].gravedad = "naranja"
                    self.calcular_tiempo_de_vida(self.lista_no_urgentes[i])

            elif self.lista_no_urgentes[i].gravedad == "verde":
                prob_que_empeoro = random.randint(1, 100000)
                if prob_que_empeoro == 1:
                    self.lista_no_urgentes[i].gravedad = "rojo"
                    self.lista_no_urgentes[i].tiempo_de_vida = 0
                    empeoraron.append(self.lista_no_urgentes[i])
                elif prob_que_empeoro == 2 or prob_que_empeoro == 30:
                    self.lista_no_urgentes[i].gravedad = "amarillo"
                    self.calcular_tiempo_de_vida(self.lista_no_urgentes[i])
            elif self.lista_no_urgentes[i].gravedad == "azul":
                prob_que_empeoro = random.randint(1, 18000000)
                if prob_que_empeoro == 1:
                    self.lista_no_urgentes[i].gravedad = "rojo"
                    self.lista_no_urgentes[i].tiempo_de_vida = 0
                    empeoraron.append(self.lista_no_urgentes[i])
                elif prob_que_empeoro > 20 or prob_que_empeoro < 50:
                    self.lista_no_urgentes[i].gravedad = "amarillo"
                    self.calcular_tiempo_de_vida(self.lista_no_urgentes[i])

        return empeoraron

    def calcular_tiempo_de_vida(self, pac):#FUNCIONA
        self.bajar_tiempo_vida()
        #considero que tardo 5 minutos en atenderse
        self.hora_actual = self.hora_actual + timedelta(minutes=5)
        tiempo_que_paso_desde_que_llego = self.hora_actual - pac.hora_de_llegada

        if pac.gravedad == "naranja":
            pac.tiempo_de_vida = 30 - tiempo_que_paso_desde_que_llego.total_seconds() / 60  # lo paso a minutos ya que opero con minutos
        elif pac.gravedad == "amarillo":
            pac.tiempo_de_vida = 60 - tiempo_que_paso_desde_que_llego.total_seconds() / 60
        elif pac.gravedad == "verde":
            pac.tiempo_de_vida = 120 - tiempo_que_paso_desde_que_llego.total_seconds() / 60
        elif pac.gravedad == "azul":
            pac.tiempo_de_vida = 240 - tiempo_que_paso_desde_que_llego.total_seconds() / 60

    def bajar_tiempo_vida(self):
        #recorro todas las listas y le decremento a tdos el tiempo
        #menos los urgentes, son los proximos en antenderse
        for i in range (len(self.lista_no_urgentes)):
            pac=self.lista_no_urgentes[i]
            pac.tiempo_de_vida=pac.tiempo_de_vida - timedelta(minutes=5)
            if pac.tiempo_de_vida<=5:
                self.lista_urgentes.append(pac) #lo paso a urgentess si le queda poco tiempo de vida

        for i in range (len(self.listaPD)):
            pac=self.listaPD[i]
            if not (pac.gravedad == "rojo"):
                pac.tiempo_de_vida=pac.tiempo_de_vida - timedelta(minutes=5)    


    def cargado_lista_paraPD(self,paciente:cPaciente): 
        self.listaPD.append(paciente)

    ##ALGORITMO PROG DINAMICA
    def SeleccionProgDinamica(self, cantEnfer: int, Npacientes: int, pacientes: list):
        # Crear una matriz K de (Npacientes + 1) x (cantEnfer + 1) inicializada con ceros
        K = [[0 for x in range(cantEnfer + 1)] for x in range(Npacientes + 1)]

        # Construir la matriz de manera ascendente
        for i in range(Npacientes + 1):  # Recorrer filas
            for w in range(cantEnfer + 1):  # Recorrer columnas
                if i == 0 or w == 0:
                    K[i][w] = 0

                elif pacientes[i - 1].tiempo_de_vida <= w:
                    beneficio = pacientes[i - 1].tiempo_de_vida
                    opcion_con_paciente = pacientes[i - 1]  # Almacenar una referencia al paciente
                    otra_opcion = K[i - 1][w - pacientes[i - 1].tiempo_de_vida]

                    if beneficio + otra_opcion > otra_opcion:
                        K[i][w] = opcion_con_paciente
                    else:
                        K[i][w] = otra_opcion
            
                else:
                    K[i][w] = K[i - 1][w]

        return K[Npacientes][cantEnfer]


 #-------------------------------------------------------------------------------------




