import pytest
from library.cPaciente import cPaciente #ESTO TIENE ERROR
from library.cEnfermero import cEnfermero 
'''from library.cHospital import cTurno

def test_DiagnosticoYGravedad():
    paciente = cPaciente(0,9,25)
    turno= cTurno[0] #maniana
    enfermero=cEnfermero(True,turno)
    resultado = paciente.Asignar_diag_Random()
    # Verifica que el resultado esté en el rango esperado (0 a 20 según tu enum)
    assert resultado<21 '''

def test_Diagnostico():
    paciente = cPaciente(0,9,25)
    resultado = paciente.Asignar_diag_Random()
    # Verifica que el resultado esté en el rango esperado (0 a 20 según tu enum)
    assert resultado<21