
from src.cPaciente import cPaciente

def test_Diagnostico():
    paciente = cPaciente(9,"25/08/2002","Martin","Scorza")
    paciente.Asignar_diag_Random()
    # Verifica que el resultado esté en el rango esperado (0 a 20 según tu enum) y que se sette bien
    assert paciente.diagnostico <21