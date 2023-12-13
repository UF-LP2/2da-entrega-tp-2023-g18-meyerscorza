import csv
from typing import List
from library.cHospital import cHospital
from library.cEnfermero import cEnfermero
from src.cPaciente import cPaciente

def readFileEnfermeros(Hospital:cHospital):
    try:
        with open("enfermeros.csv") as file:
            reader = csv.reader(file)
            next(reader)  # Omitir la primera fila si contiene encabezados
            for row in reader:
                id = int(row[0])  
                nombre = row[1]  
                apellido = row[2] 
                disponibilidad = bool(row[3])
                enfermero = cEnfermero(id, nombre, apellido,disponibilidad) #creo un objeto de enfermero asi se hace una lista de enfermos
                Hospital.lista_enfermeros.append(enfermero)
        return Hospital.lista_enfermeros
    except FileNotFoundError:
        raise Exception("El archivo no se encuentra")

def readFilePacientes(Hospital:cHospital): 
    try:
        with open(r"PACIENTES.csv") as file:
            reader = csv.reader(file)
            next(reader) #no leo encabezado
            for row in reader:
                id = int(row[0])  
                nombre = row[1]  
                apellido = row[2]  
                nacimiento = row[3] 
                sin1 = row[4]  
                sin2 = row[5] 
                sin3 = row[6] 
                paciente = cPaciente(id, nacimiento, nombre, apellido, sin1, sin2, sin3)
                Hospital.lista_pacientesTotales.append(paciente)
        return Hospital.lista_pacientesTotales# NO ES REAL ASI PERO HAY Q GUARDARLO
    except FileNotFoundError:  # utilizo excepcion que tiene Python para archivos no encontrados
        raise Exception("El archivo no se encuentra")