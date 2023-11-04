import random
from datetime import datetime
from src.cPaciente import cPaciente
from library.cHospital import cHospital
from library.cEnfermero import cEnfermero
from library.leer_archivos import readFileEnfermeros
from library.leer_archivos import readFilePacientes

hora_actual = datetime(2023, 10, 24, 0, 0, 0, 0)

def main() -> None:
    Hospital = cHospital(hora_actual)  # Pasa hora_actual como argumento
    readFilePacientes(Hospital)
    readFileEnfermeros(Hospital)
    
    
   # while i<lista2:
    Hospital.Enf_actuales()  # le da al hospital lista de los enfermeros de ese turno
    print (Hospital.lista_enfermerosDisp)
    Hospital.disp_enfermeros() # este ve cuales estan ocupados o no de de ese turno y atiendo en la entrada
#        i=i+1
    print(Hospital.lista_urgentes)
    print(Hospital.lista_no_urgentes)
#    for i in range(1, len(lista2)):

    #vemos los enfermeros_actuales()#veo q turno es
    # vemos de los que hay, cuales estan de esos disponibles
    #le asigno gravedad paciente (metodo greedy)

    #se ejecutan las cosas y llamo a disp enfermeros
    #aumento 15 minutos el tiempo actual IMPORTANTE SI OSI AL FINAL
if __name__ == "__main__":
  main()


