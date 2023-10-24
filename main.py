import random
from datetime import datetime, timedelta
from library.cPaciente import cPaciente, cGravedad
from library.cEnfermero import cEnfermero
hora_actual = datetime(2023, 10, 24, 15, 0)  # Hora actual de la simulación
def hora_de_llegada_aleatoria():#con esta funcion genero hora de llegada aleatoria
   #debo asegurarme que la hora de llegada sea menor a la que genera aleatoriamente
    horas_aleatoria = random.randint(0, hora_actual.hour)#entre cero y la hora actual

    #  Calculamos una hora de llegada restando el rango de horas aleatorio
    hora_llegada = hora_actual - timedelta(hours=horas_aleatoria)#time delta se utiliza para realizar operaciones con horas, y se debe indicar que debo restar

    # Agregamos minutos aleatorios a la hora de llegada
    minutos_llegada = random.randint(0, 59)
    hora_llegada = hora_llegada.replace(minute=minutos_llegada)

    return hora_llegada

def main() -> None:
#creamos pacientes randoms con un for
  for i in range (10):

    edad = random.randint(10, 100)
    hora_llegada = hora_de_llegada_aleatoria()
    paciente=cPaciente(0, hora_llegada ,edad)



if __name__ == "__main__":
  main()
