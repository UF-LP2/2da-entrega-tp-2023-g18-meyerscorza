import random
from datetime import datetime
from src.cPaciente import cPaciente
from library.cHospital import cHospital
from library.cEnfermero import cEnfermero
from library.leer_archivos import readFileEnfermeros
from library.leer_archivos import readFilePacientes
from typing import List

def main() -> None:
    Hospital=cHospital()
    lista=readFileEnfermeros(Hospital)
    lista2=readFilePacientes(Hospital)
    print(lista2) 

    '''hora_actual = datetime(2023, 10, 24, 0, 0, 0, 0)  # Hora actual de la simulación
    pacientes = readFile("pacientes.csv")
    enfermeros = readFile("enfermeros.csv")

    for i in range(1, len(pacientes)):'''

        #vemos los enfermeros_actuales()#veo q turno es
    # vemos de los que hay, cuales estan de esos disponibles
    #le asigno gravedad paciente (metodo greedy)

    #se ejecutan las cosas y llamo a disp enfermeros
    #aumento 15 minutos el tiempo actual IMPORTANTE SI OSI AL FINAL
if __name__ == "__main__":
  main()

  '''pac1=cPaciente(9,15)
  pac2=cPaciente(5,31)
  enfermero=cEnfermero(True,1)
  enfermero.asignar_gravedad(pac1)

  hospital=cHospital()
  hospital.cargar_listas(pac1)
  hospital.cargar_listas(pac2)'''
