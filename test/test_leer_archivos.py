import pytest
from library.leer_archivos import readFile
import csv
from typing import List
@pytest.fixture#aclara que se ejecutará en el momento adecuado antes de que las pruebas  requeridas comiencen a ejecutarse.
def archivo_prueba():
    return "./src/pacientes2.csv"

def test_leer_archivos(archivo_prueba):
    resultado = readFile(archivo_prueba)
    assert isinstance(resultado, list)# asegura que lo que se leyo sea una lista
    assert len(resultado) > 0#que mi tamanio sea mayor a cero
    for i in resultado:# Verifica que haya 4 campos por fila
        assert len(i) == 4


