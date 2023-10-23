import pytest
from library.cPaciente import cPaciente 
from library.cEnfermero import cEnfermero 

def test_Diagnostico():
    paciente = cPaciente(0,9,25)
    paciente.Asignar_diag_Random()
    # Verifica que el resultado esté en el rango esperado (0 a 20 según tu enum)
    assert paciente.diagnostico <21