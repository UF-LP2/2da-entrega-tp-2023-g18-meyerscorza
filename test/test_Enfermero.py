import pytest
from library.cEnfermero import cEnfermero 
from library.cPaciente import cPaciente

def test_Gravedad():
    paciente = cPaciente(0,9,25)
    enfermero=cEnfermero(True,1)
    paciente.diagnostico=1
    enfermero.asignar_gravedad(paciente)
    # Verifica que el resultado esté en el rango esperado (0 a 20 según tu enum)
    assert paciente.gravedad==1