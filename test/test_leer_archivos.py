import pytest
from library.leer_archivos import readFile
from library.leer_archivos import readFileEnfermeros
from library.cHospital import cHospital
import csv
from typing import List
@pytest.fixture#aclara que se ejecutará en el momento adecuado antes de que las pruebas  requeridas comiencen a ejecutarse.

def archivo_prueba():
        return "enfermeros.csv"

def test_leer_archivos(archivo_prueba):
        resultado = readFile(archivo_prueba)
        assert isinstance(resultado, list)# asegura que lo que se leyo sea una lista
        assert len(resultado) > 0#que mi tamanio sea mayor a cero
        for i in resultado:# Verifica que haya 4 campos por fila
            assert len(i) == 4    
        return "enfermeros.csv" 


def test_leerEnfermeros(Hospital:cHospital):
    resultado = readFileEnfermeros (Hospital)
    assert isinstance(resultado, list)# asegura que lo que se leyo sea una lista
    assert len(resultado) > 0 #que mi tamanio sea mayor a cero
    for i in resultado:# Verifica que haya 4 campos por fila
        assert len(i) == 3