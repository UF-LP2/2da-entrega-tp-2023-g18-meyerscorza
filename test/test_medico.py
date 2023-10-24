import pytest
from library.cMedico import cMedico
from library.cPaciente import cPaciente

def test_Atender_Paciente():

    medico = cMedico()
    paciente = cPaciente(0, 9, 30)
    result = medico.Atender_Paciente(paciente)
    assert result
    paciente_nulo = None
    result_nulo = medico.Atender_Paciente(paciente_nulo)
    assert not result_nulo