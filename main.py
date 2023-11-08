import random
from datetime import datetime
from src.cPaciente import cPaciente
from library.cHospital import cHospital
from library.cEnfermero import cEnfermero
from library.cMedico import cMedico
from library.leer_archivos import readFileEnfermeros
from library.leer_archivos import readFilePacientes



hora_actual = datetime(2023, 10, 24, 0, 0, 0, 0)

# Declarar pacientes_atendidos a nivel de módulo
pacientes_atendidos = [] # Lista para realizar un seguimiento de pacientes atendidos

def main() -> None:
   
    Hospital = cHospital(hora_actual)  # Pasa hora_actual como argumento
    lista2 = readFilePacientes(Hospital)
    readFileEnfermeros(Hospital)
    i = 0

    #PROG DINAMICA-----------------------------------------------------------------------------------------
    while i < len(lista2):
        Hospital.lista_enfermerosDisp.clear()  # Vacía la lista de enfermeros por si cambia el turno
        Hospital.Enf_actuales()  # Da al hospital lista de los enfermeros de ese turno
        Hospital.disp_enfermeros()  # Verifica cuáles están ocupados o no de ese turno y atiende en la entrada

        Medico = cMedico(56)
        tamEnf=len(Hospital.lista_enfermerosDisp)
        tamPac=len(Hospital.listaPD)
        resultado= Hospital.SeleccionProgDinamica(tamEnf,tamPac,Hospital.listaPD)
        pac=Hospital.buscadorPaciente(resultado)

        # Comprueba si el paciente ya ha sido atendido
        if pac not in pacientes_atendidos:
            a = Medico.Atender_Paciente(pac)
            print("Ha sido atendido el paciente con apellido")
            apellido = pac.apellido
            print(apellido)
            if a:  # Si pudo atender al paciente, elimínalo de la lista de pacientes por atender
                Hospital.eliminar_pac(pac)
            
            pacientes_atendidos.append(pac)  # Agrega al paciente a la lista de atendidos

        i = i + 1
    
    
if __name__ == "__main__":
    main()


"""while i < len(lista2):
        Hospital.lista_enfermerosDisp.clear()  # Vacía la lista de enfermeros por si cambia el turno
        Hospital.Enf_actuales()  # Da al hospital lista de los enfermeros de ese turno
        Hospital.disp_enfermeros()  # Verifica cuáles están ocupados o no de ese turno y atiende en la entrada

        Medico = cMedico(56)
        pac = Hospital.SeleccionGreedy()

        # Comprueba si el paciente ya ha sido atendido
        if pac not in pacientes_atendidos:
            a = Medico.Atender_Paciente(pac)
            print("Ha sido atendido el paciente con apellido")
            apellido = pac.apellido
            print(apellido)
            if a:  # Si pudo atender al paciente, elimínalo de la lista de pacientes por atender
                Hospital.eliminar_pac(pac)
            pacientes_atendidos.append(pac)  # Agrega al paciente a la lista de atendidos

        i = i + 1"""

