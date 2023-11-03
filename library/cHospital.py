import random
from datetime import datetime
from src.cPaciente import cPaciente

class cHospital:
    def __init__(self, hora_actual: datetime):
        self.lista_urgentes = []          # Lista de pacientes urgentes (inicializo en vacío)
        self.lista_no_urgentes = []      # Lista de pacientes no urgentes (inicializo en vacío)
        self.lista_enfermerosDisp = []     # Lista de enfermeros disponibles (inicializo en vacío)
        self.lista_enfermeros=[]            #utilizo para cuando leeo el archivo
        self.lista_pacientesTotales=[]      #utilizo para cuando leeo el archivo
        self.hora_actual = hora_actual  # Almacena la hora_actual como atributo
    def cargar_listas(self, pac:cPaciente):
        if pac.gravedad == "rojo":
            pac.tiempo_de_vida = 0
            self.lista_urgentes.append(pac)
        else:
            self.calcular_tiempo_de_vida(pac,self.hora_actual)#funcion que calcula cuanto tiempo le queda
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
                #self. setear_disponibilidad(lista_enfermeros_actuales[i], True) #esto esta en enfermeros
                cont += 1
            i+=1
        if cont == 0:#significa que todos los enfermeros estan ocupados, caso extremo
            print("Espere a ser atendido, todos nuestros enfermeros estan ocupados")

    def Enf_actuales(self): #TESTING
        momento_del_dia = self.momento_dia()  #funcion que devuelve, maniana,tarde,noche o madrugada
    
        cant=0
        
        if momento_del_dia =="Madrugada": #elijo solo a 1 
            cant=1
        elif momento_del_dia=="Maniana": #elijo a 2
            cant=2
        elif momento_del_dia=="Tarde": #elijo a 5
            cant=5
        elif momento_del_dia=="Noche": #elijo a 3
            cant=3
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
            

    def momento_dia(self)-> str:
       

        # Define los rangos de tiempo para cada turno
        turno_madrugada= (datetime.strptime("23:00:00", "%H:%M:%S").time(), datetime.strptime("06:00:00", "%H:%M:%S").time())
        turno_maniana = (datetime.strptime("06:00:00", "%H:%M:%S").time(), datetime.strptime("10:00:00", "%H:%M:%S").time())
        turno_tarde = (datetime.strptime("10:00:00", "%H:%M:%S").time(), datetime.strptime("16:00:00", "%H:%M:%S").time())
        turno_noche = (datetime.strptime("16:00:00", "%H:%M:%S").time(), datetime.strptime("23:00:00", "%H:%M:%S").time())

        # Compara la hora actual con los rangos de tiempo y determina el turno
        if turno_noche[0] <= self.hora_actual < turno_noche[1]:
            turno = "Noche"
        elif turno_maniana[0] <= self.hora_actual < turno_maniana[1]:
            turno = "Maniana"
        elif turno_tarde[0] <= self.hora_actual < turno_tarde[1]:
            turno = "Tarde"
        else:
            turno = "Madrugada"
        
        return turno
    


    def eliminar_pac(self,pac):
        #no se en cual de las dos de las lista esta, entocnes ponemos esas condiciones
        if pac in self.lista_urgentes:
            self.lista_urgentes.remove(pac)
        else:
            self.lista_no_urgentes.remove(pac)
    
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
            edad_paciente = self.calcular_edad(empeoraron[i].nacimiento)
            if edad_paciente < edad_mas_joven:# comparo si la edad que entra es menor a la anterior
                edad_mas_joven = edad_paciente
                paciente_mas_joven = empeoraron[i]

        return paciente_mas_joven

    def calcular_edad(self, fecha_nacimiento:datetime):
        edad = self.hora_actual.year - fecha_nacimiento.year
        if self.hora_actual.month < fecha_nacimiento.month or (
                self.hora_actual.month == fecha_nacimiento.month and self.hora_actual.day < fecha_nacimiento.day):  # vemos la edad si aún no ha tenido su cumpleaños este año
            edad -= 1# le restamos uno si todavia no cumplio
        return edad

    def empeoro_pac_no_urgente(self):
        empeoraron = []
        for i in range(len(self.lista_no_urgentes)):
            prob_que_empeoro = 0  # Inicializamos la variable
            if self.lista_no_urgentes[i].gravedad == "amarillo":
                prob_que_empeoro = random.randint(1, 6)
            elif self.lista_no_urgentes[i].gravedad == "verde":
                prob_que_empeoro = random.randint(1, 10)
            elif self.lista_no_urgentes[i].gravedad == "azul":
                prob_que_empeoro = random.randint(1, 18)

            if prob_que_empeoro == 1:
                self.lista_no_urgentes[i].gravedad = "rojo"
                empeoraron.append(self.lista_no_urgentes[i])

        return empeoraron

    def calcular_tiempo_de_vida(self, pac):
        #hacer una funcion que me devuelva cunato tardo en atenderse cdependiendo su color
        #considero que tardo 15 minutos en atenderse
        tiempo_que_paso_desde_que_llego = self.hora_actual - pac.hora_llegada

        if pac.gravedad == "naranja":
            pac.tiempo_de_vida = 30 - tiempo_que_paso_desde_que_llego.total_seconds() / 60  # lo paso a minutos ya que opero con minutos
        elif pac.gravedad == "amarillo":
            pac.tiempo_de_vida = 60 - tiempo_que_paso_desde_que_llego.total_seconds() / 60
        elif pac.gravedad == "verde":
            pac.tiempo_de_vida = 120 - tiempo_que_paso_desde_que_llego.total_seconds() / 60
        elif pac.gravedad == "azul":
            pac.tiempo_de_vida = 240 - tiempo_que_paso_desde_que_llego.total_seconds() / 60
    

   
'''

    ##ALGORITMO PROG DINAMICA
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

        return K  # Devolver la matriz K '''



