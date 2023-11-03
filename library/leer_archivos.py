import csv
from typing import List
from library.cHospital import cHospital

'''def readFile(archivo):
    lista = []
    try:
        with open(archivo) as file:
            reader = csv.reader(file)
            for i in reader:
                lista.append(i)

        return lista
    except FileNotFoundError:  # utilizo excepcion que tiene Python para archivos no encontrados
        raise Exception("El archivo no se encuentra")'''

def readFileEnfermeros(Hospital:cHospital): #HACER EL TESTING 
    try:
        with open(r"enfermeros.csv") as file:
            reader = csv.reader(file)
            for i in reader:
                Hospital.lista_enfermeros.append(i)
        return Hospital.lista_enfermeros
    except FileNotFoundError:  # utilizo excepcion que tiene Python para archivos no encontrados
        raise Exception("El archivo no se encuentra")

def readFilePacientes(Hospital:cHospital): #HACER EL TESTING 
    try:
        with open(r"Pacientes.csv") as file:
            reader = csv.reader(file)
            for i in reader:
                Hospital.lista_pacientesTotales.append(i)
        return Hospital.lista_pacientesTotales
    except FileNotFoundError:  # utilizo excepcion que tiene Python para archivos no encontrados
        raise Exception("El archivo no se encuentra")