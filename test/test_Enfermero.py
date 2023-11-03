from library.cEnfermero import cEnfermero
from src.cPaciente import cPaciente

def test_colorXsintomas():
    paciente=cPaciente(1,"2006-12-21 01:33:46","Marcos","Lopez","paro_cardiaco","otalgias","tos")
    enfermero=cEnfermero(3,"Luis","Armada")
    enfermero.colorSintomaGrave(paciente)
    assert enfermero.colorSintomaGrave() == "rojo"
