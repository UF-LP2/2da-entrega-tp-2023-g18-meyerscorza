import csv
from typing import List
import cHospital

def readFile(archivo):
    lista = []
    try:
        with open(archivo) as file:
            reader = csv.reader(file)
            for i in reader:
                lista.append(i)

        return lista
    except FileNotFoundError:  # utilizo excepcion que tiene Python para archivos no encontrados
        raise Exception("El archivo no se encuentra")

def readFileEnfermeros(Hospital:cHospital): #HACER EL TESTING 
    lista = []
    try:
        with open(r"enfermeros.csv") as file:
            reader = csv.reader(file)
            for i in reader:
                lista.append(i)

        return lista
    except FileNotFoundError:  # utilizo excepcion que tiene Python para archivos no encontrados
        raise Exception("El archivo no se encuentra")