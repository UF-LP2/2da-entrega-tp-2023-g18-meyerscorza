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
    lista = readFileEnfermeros(Hospital)
    lista2 = readFilePacientes(Hospital)
    Hospital.Enf_actuales()  # No es necesario pasar hora_actual
    print(Hospital.lista_enfermerosDisp)



#    for i in range(1, len(lista2)):

    #vemos los enfermeros_actuales()#veo q turno es
    # vemos de los que hay, cuales estan de esos disponibles
    #le asigno gravedad paciente (metodo greedy)

    #se ejecutan las cosas y llamo a disp enfermeros
    #aumento 15 minutos el tiempo actual IMPORTANTE SI OSI AL FINAL
if __name__ == "__main__":
  main()


