import csv


def readFile():
    pacientes = []
    try:
        with open(r"pacientes.csv") as file:
            reader = csv.reader(file)
            for i in reader:
                pacientes.append(i)

        return pacientes
    except FileNotFoundError:  # utilizo excepcion que tiene Python para archivos no encontrados
        raise Exception("El archivo no se encuentra")
def readFile2():
    enfermeros = []
    try:
        with open(r"enfermeros.csv") as file:
            reader = csv.reader(file)
            for i in reader:
                enfermeros.append(i)

        return enfermeros
    except FileNotFoundError:  # utilizo excepcion que tiene Python para archivos no encontrados
        raise Exception("El archivo no se encuentra")
