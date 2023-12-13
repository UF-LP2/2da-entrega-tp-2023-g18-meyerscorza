
from src.cPaciente import cPaciente

class cMedico:
    def __init__(self, NroMatricula: int):
        self.NroMatricula = NroMatricula


    def Atender_Paciente(self, pac: cPaciente) -> bool:
        if pac is not None:
            return True
        else:
            return False
        
