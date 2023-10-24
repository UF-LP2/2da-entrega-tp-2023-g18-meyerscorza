import random
from datetime import datetime, timedelta
from library.cPaciente import cPaciente
from library.cHospital import cHospital
from library.cPaciente import cGravedad
from library.cEnfermero import cEnfermero
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
#creamos pacientes randoms con un for
  for i in range (10):

    edad = random.randint(10, 100)
    hora_llegada = hora_de_llegada_aleatoria()
    paciente=cPaciente(hora_llegada ,edad)



if __name__ == "__main__":
  pac1=cPaciente(9,15)
  pac2=cPaciente(5,31)
  pac1.Asignar_diag_Random()
  pac2.Asignar_diag_Random()
  enfermero=cEnfermero(True,1)
  enfermero.asignar_gravedad(pac1)
  enfermero.asignar_gravedad(pac2)

  hospital=cHospital()
  hospital.cargar_listas(pac1)
  hospital.cargar_listas(pac2)
