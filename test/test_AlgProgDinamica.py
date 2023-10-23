import pytest
from library.cHospital import cHospital
from library.cPaciente import cPaciente

def test_TesteoAlgoritmoProgDinamica():
    cantEnfer=5
    Npacientes = len(pacientes)
    #no tienen que ser por defecto cambiar esto
    pac1=cPaciente() 
    pac2=cPaciente() 
    pac3=cPaciente() 

    beneficio=[pac1.tiempo_de_vida,pac2.tiempo_de_vida,pac3.tiempo_de_vida,]
    pacientes=[pac1,pac2,pac3]
    