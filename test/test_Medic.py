import pytest
from library.cMedico import cMedico
from library.cPaciente import cPaciente


def test_Atender_Paciente():
    # Crear una instancia de cMedico y cPaciente
    medico = cMedico(12345)
    paciente = cPaciente(9, "25/08/2002",,"Martina","Meyer")
    
    # Realizar la prueba
    result = medico.Atender_Paciente(paciente)
    
    # Verificar el resultado
    assert result == True 
    '''paciente_nulo = None
    result_nulo = medico.Atender_Paciente(paciente_nulo)
    assert result_nulo==False'''