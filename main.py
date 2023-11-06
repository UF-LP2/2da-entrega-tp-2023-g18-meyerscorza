import random
from datetime import datetime
from src.cPaciente import cPaciente
from library.cHospital import cHospital
from library.cEnfermero import cEnfermero
from library.cMedico import cMedico
from library.leer_archivos import readFileEnfermeros
from library.leer_archivos import readFilePacientes

hora_actual = datetime(2023, 10, 24, 0, 0, 0, 0)

def main() -> None:
    Hospital = cHospital(hora_actual)  # Pasa hora_actual como argumento
    lista2=readFilePacientes(Hospital)
    readFileEnfermeros(Hospital)
    
    i=0

   #while i<lista2:
    Hospital.Enf_actuales()  # le da al hospital lista de los enfermeros de ese turno
    Hospital.disp_enfermeros() # este ve cuales estan ocupados o no de de ese turno y atiendo en la entrada
    Medico = cMedico(56)
    tamEnf = len(Hospital.lista_enfermerosDisp)
    tamPac = len(Hospital.listaPD)
    resultado = Hospital.SeleccionProgDinamica(tamEnf, tamPac, Hospital.listaPD)
    print(resultado)
    pac=Hospital.SeleccionGreedy()
    a=Medico.Atender_Paciente(pac)

    if a==True: #lo pudo atender
        Hospital.eliminar_pac(pac)

       # i=i+1
    





#    for i in range(1, len(lista2)):

    #vemos los enfermeros_actuales()#veo q turno es
    # vemos de los que hay, cuales estan de esos disponibles
    #le asigno gravedad paciente (metodo greedy)

    #se ejecutan las cosas y llamo a disp enfermeros
    #aumento 15 minutos el tiempo actual IMPORTANTE SI OSI AL FINAL
if __name__ == "__main__":
  main()


