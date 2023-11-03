import csv
from typing import List
from library.cHospital import cHospital

#funciones que andan
def readFileEnfermeros(Hospital:cHospital):
    try:
        with open(r"Enfermeros.csv") as file:
            reader = csv.reader(file)
            for i in reader:
                Hospital.lista_enfermeros.append(i)
        return Hospital.lista_enfermeros
    except FileNotFoundError:  # utilizo excepcion que tiene Python para archivos no encontrados
        raise Exception("El archivo no se encuentra")

def readFilePacientes(Hospital:cHospital): 
    try:
        with open(r"Pacientes.csv") as file:
            reader = csv.reader(file)
            for i in reader:
                Hospital.lista_pacientesTotales.append(i)
        return Hospital.lista_pacientesTotales# NO ES REAL ASI PERO HAY Q GUARDARLO
    except FileNotFoundError:  # utilizo excepcion que tiene Python para archivos no encontrados
        raise Exception("El archivo no se encuentra")