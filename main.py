import random
from datetime import datetime
from src.cPaciente import cPaciente
from library.cHospital import cHospital
from library.cEnfermero import cEnfermero
from library.cMedico import cMedico
from library.leer_archivos import readFileEnfermeros
from library.leer_archivos import readFilePacientes
import tkinter as tk  # Importa la biblioteca Tkinter
from PIL import Image, ImageTk

# Abre la imagen JPG
imagen_jpg = Image.open("hospital.jpg")

# Guarda la imagen en formato PNG
imagen_jpg.save("hospital.png")

hora_actual = datetime(2023, 10, 24, 0, 0, 0, 0)

# Función para mostrar información detallada del paciente al hacer clic en un cuadro
def mostrar_informacion_paciente(event, paciente):
    ventana_informacion = tk.Toplevel()
    ventana_informacion.title("Información del Paciente")
    
    # A continuación, puedes agregar etiquetas y mostrar los atributos del paciente
    etiqueta_nombre = tk.Label(ventana_informacion, text="Nombre: " + paciente.nombre)
    etiqueta_sintoma1 = tk.Label(ventana_informacion, text="Síntoma1: " + paciente.sintoma1)
    etiqueta_sintoma2 = tk.Label(ventana_informacion, text="Síntoma2: " + paciente.sintoma2)
    etiqueta_sintoma3 = tk.Label(ventana_informacion, text="Síntoma3: " + paciente.sintoma3)
    
    # Agrega más etiquetas para otros atributos que desees mostrar
    
    etiqueta_nombre.pack()
    etiqueta_sintoma1.pack()
    etiqueta_sintoma2.pack()
    etiqueta_sintoma3.pack()
    

# Función para distribuir los cuadrados sin superposición en filas y columnas
def distribuir_cuadrados(pacientes, enfermeros, ancho_ventana, alto_ventana, ancho_cuadro, alto_cuadro):
    num_pacientes = len(pacientes)
    max_filas = alto_ventana // alto_cuadro
    max_columnas = ancho_ventana // ancho_cuadro

    if num_pacientes > max_filas * max_columnas:
        print("Advertencia: No hay suficiente espacio en la ventana para todos los pacientes.")
        return []

    posiciones = []
    for fila in range(max_filas):
        for columna in range(max_columnas):
            x = columna * ancho_cuadro
            y = fila * alto_cuadro
            posiciones.append((x, y))

    # Agregar posiciones para enfermeros en la misma cuadrícula
    posiciones_enfermeros = random.sample(posiciones, len(enfermeros))

    return posiciones, posiciones_enfermeros

# Modifica la función representar_pacientes para agregar un evento de clic a cada cuadro
def representar_pacientes(pacientes, canvas, index, posiciones):
    if index < len(pacientes):
        paciente = pacientes[index]
        gravedad = paciente.gravedad  # Obtiene la gravedad del paciente

        if gravedad == "rojo":
            color = "red"
        elif gravedad == "amarillo":
            color = "yellow"
        elif gravedad == "verde":
            color = "green"
        elif gravedad == "azul":
            color = "blue"
        else:
            color = "orange"

        apellido = paciente.apellido  # Obtiene el apellido del paciente

        ancho_cuadro = 50
        alto_cuadro = 50
        x, y = posiciones[index]  # Utiliza la posición precalculada

        cuadro = tk.Canvas(canvas, width=ancho_cuadro, height=alto_cuadro)
        cuadro.create_rectangle(0, 0, ancho_cuadro, alto_cuadro, fill=color)
        cuadro.create_text(ancho_cuadro // 2, alto_cuadro // 2, text=apellido)  # Muestra el apellido en el centro del cuadro

        cuadro.bind("<Button-1>", lambda event, p=paciente: mostrar_informacion_paciente(event, p))
        cuadro.place(x=x, y=y)

        # Programa la próxima llamada a representar_pacientes con un índice incrementado después de 1 segundos
        canvas.after(1000, representar_pacientes, pacientes, canvas, index + 1, posiciones)


def representar_enfermeros(enfermeros, canvas, index, posiciones_enfermeros):
    if index < len(enfermeros):
        enfermero = enfermeros[index]
        id_enfermero = enfermero.id  # Obtener el ID del enfermero

        x, y = posiciones_enfermeros[index]  # Utilizar la posición precalculada
        radio = 20  # Radio del círculo del enfermero

        cuadro_enfermero = tk.Canvas(canvas, width=radio * 2, height=radio * 2)
        cuadro_enfermero.create_oval(0, 0, radio * 2, radio * 2, fill="white")
        cuadro_enfermero.create_text(radio, radio, text=str(id_enfermero), fill="black")
        cuadro_enfermero.place(x=x, y=y)

        # Programar la próxima llamada para representar los enfermeros
        canvas.after(1000, representar_enfermeros, enfermeros, canvas, index + 1, posiciones_enfermeros)



# Declarar pacientes_atendidos a nivel de módulo
pacientes_atendidos = [] # Lista para realizar un seguimiento de pacientes atendidos
cant_enfermeros=[]

def iniciar_atencion_pacientes():
    Hospital = cHospital(hora_actual)  # Pasa hora_actual como argumento
    lista2 = readFilePacientes(Hospital)
    readFileEnfermeros(Hospital)
    i = 0

    #PROG DINAMICA-----------------------------------------------------------------------------------------
    while i < len(lista2):
        Hospital.lista_enfermerosDisp.clear()  # Vacía la lista de enfermeros por si cambia el turno
        Hospital.Enf_actuales()  # Da al hospital lista de los enfermeros de ese turno
        cant_enfermeros=Hospital.lista_enfermerosDisp
        Hospital.disp_enfermeros()  # Verifica cuáles están ocupados o no de ese turno y atiende en la entrada

        Medico = cMedico(56)
        tamEnf=len(Hospital.lista_enfermerosDisp)
        tamPac=len(Hospital.listaPD)
        resultado= Hospital.SeleccionProgDinamica(tamEnf,tamPac,Hospital.listaPD)
        pac=Hospital.buscadorPaciente(resultado)

        # Comprueba si el paciente ya ha sido atendido
        if pac not in pacientes_atendidos:
            a = Medico.Atender_Paciente(pac)
            print("Ha sido atendido el paciente con apellido")
            apellido = pac.apellido
            print(apellido)
            if a:  # Si pudo atender al paciente, elimínalo de la lista de pacientes por atender
                Hospital.eliminar_pac(pac)

            pacientes_atendidos.append(pac)  # Agrega al paciente a la lista de atendidos

        i = i + 1

    root = tk.Tk()
    root.geometry("800x600")  # Ajusta el tamaño de la ventana según tus necesidades
    

    # Llama a la función para distribuir cuadrados sin superposición
    ancho_ventana = 800
    alto_ventana = 600
    ancho_cuadro = 50
    alto_cuadro = 50
    posiciones_pacientes, posiciones_enfermeros = distribuir_cuadrados(pacientes_atendidos, cant_enfermeros, ancho_ventana, alto_ventana, ancho_cuadro, alto_cuadro)
    
    # Llama a la función para representar pacientes con una diferencia de 5 segundos
    representar_pacientes(pacientes_atendidos, root, 0, posiciones_pacientes)
    representar_enfermeros(cant_enfermeros, root, 0, posiciones_enfermeros)
    

    root.mainloop()  # Muestra la ventana

if __name__ == "__main__":
    root = tk.Tk()
    # Agregar un icono a la ventana
    icon = tk.PhotoImage(file="hospital.png")
    root.tk.call('wm', 'iconphoto', root._w, icon)

     # Cargar la imagen y redimensionarla
    imagen = Image.open("hospital.png")
    imagen.thumbnail((100000, 80000)) # Cambiar el tamaño a las dimensiones deseadas
    fondo = ImageTk.PhotoImage(imagen)

    # Crear un widget Label con la imagen como fondo
    label_fondo = tk.Label(root, image=fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)  # Ajustar el tamaño del Label al tamaño de la ventana

    info_label = tk.Label(root, text="Bienvenido al Hospital de Springfield", font=("Arial", 35))
    info_label.pack()
    atender_pacientes_button = tk.Button(root, text="Atender Pacientes", command=iniciar_atencion_pacientes)
    atender_pacientes_button.pack()
    
    root.mainloop()