import random
import library
from library.cHospital import cHospital
from src.cPaciente import cPaciente
from library.cEnfermero import cEnfermero

'''from datetime import datetime
from src.cPaciente import cPaciente
from library.cHospital import cHospital
from library.cEnfermero import cEnfermero
from library.cMedico import cMedico
from library.leer_archivos import readFileEnfermeros
from library.leer_archivos import readFilePacientes'''
from typing import List

def main() -> None:
    Hospital=cHospital()
    #lista=readFileEnfermeros(Hospital)
    #lista2=readFilePacientes(Hospital)

    paciente=cPaciente(1,"2006-12-21 01:33:46","Marcos","Lopez","paro_cardiaco","otalgias","tos")
    enfermero=cEnfermero(3,"Luis","Armada")
    enfermero.AsignoGravedadGreedy(paciente,Hospital)

    Medico=cMedico(1234)
    Medico.Atender_Paciente(paciente)

    

        #vemos los enfermeros_actuales()#veo q turno es
    # vemos de los que hay, cuales estan de esos disponibles
    #le asigno gravedad paciente (metodo greedy)

    #se ejecutan las cosas y llamo a disp enfermeros
    #aumento 15 minutos el tiempo actual IMPORTANTE SI OSI AL FINAL
if __name__ == "__main__":
  main()

 