import random
from datetime import datetime
from src.cPaciente import cPaciente
from library.cHospital import cHospital
from library.cEnfermero import cEnfermero
from library.leer_archivos import readFile
from typing import List
hora_actual = datetime(2023, 10, 24, 15, 0,0,0)  # Hora actual de la simulación




'''def hora_de_llegada_aleatoria_relacionPacienteAnterior(horallegadaPacAnt:datetime):#con esta funcion genero hora de llegada aleatoria con respecto al otro paciente que ingreso
   #debo asegurarme que la hora de llegada sea mayor a el anterior paciente 
    horas_aleatoria = random.randint(0, hora_actual.hour)#entre cero y la hora actual

    #  Calculamos una hora de llegada restando el rango de horas aleatorio
    hora_llegada = hora_actual - timedelta(hours=horas_aleatoria)#time delta se utiliza para realizar operaciones con horas, y se debe indicar que debo restar

    # Agregamos minutos aleatorios a la hora de llegada
    minutos_llegada = random.randint(0, 59)
    hora_llegada = hora_llegada.replace(minute=minutos_llegada)

    return hora_llegada'''


def main() -> None:
    pacientes = readFile("pacientes.csv")
    enfermeros = readFile("enfermeros.csv")

    for i in range(1, len(pacientes)):
     # vemos los enfermeros_actuales()
    # vemos los de los que hay cuales estan de esos disponibles
    #le asigno gravedad paciente

    #se ejecutan las cosas y llamo a disp enfermeros

if __name__ == "__main__":
  main()

  '''pac1=cPaciente(9,15)
  pac2=cPaciente(5,31)
  enfermero=cEnfermero(True,1)
  enfermero.asignar_gravedad(pac1)

  hospital=cHospital()
  hospital.cargar_listas(pac1)
  hospital.cargar_listas(pac2)'''
