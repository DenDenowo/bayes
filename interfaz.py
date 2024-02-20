import tkinter as tk
from tkinter import messagebox
from controlador import *

controlador = controlador()
def calcular(genero, tipo, enfermedad):
    probabilidad = 0
    probabilidad = controlador.calcularProbabilidad(genero, tipo, enfermedad)
    # Mostrar el resultado
    mensaje = "La probabilidad de este caso es de: " + str(probabilidad)
    messagebox.showinfo("Resultado", mensaje)

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("400x400")  # Tamaño de la ventana
ventana.title("Encuesta de Salud")
ventana.configure(background='#E3F1F1')  # Establecer color de fondo para la ventana

titulo = tk.Label(ventana, text="Encuesta de Salud", font=("Verdana", 15), background='#E3F1F1')
titulo.pack()

# Pregunta 1: Género
pregunta_genero = tk.Label(ventana, text="¿Eres hombre o mujer?", font=('Helvetica',12), background='#E3F1F1')
pregunta_genero.pack()

opcion_genero = tk.StringVar()
opcion_genero.set("Hombre")  # Opción predeterminada

radio_hombre = tk.Radiobutton(ventana, text="Hombre", variable=opcion_genero, value="Hombre", background='#E3F1F1')
radio_hombre.pack()

radio_mujer = tk.Radiobutton(ventana, text="Mujer", variable=opcion_genero, value="Mujer", background='#E3F1F1')
radio_mujer.pack()

# Pregunta 2: Caso de COVID
pregunta_covid = tk.Label(ventana, text="El caso de COVID fue:", font=('Helvetica',12), background='#E3F1F1')
pregunta_covid.pack()

opcion_covid = tk.StringVar()
opcion_covid.set("Ambulatorio")  # Opción predeterminada

radio_ambulatorio = tk.Radiobutton(ventana, text="Ambulatorio", variable=opcion_covid, value="Ambulatorio", background='#E3F1F1')
radio_ambulatorio.pack()

radio_hospitalizado = tk.Radiobutton(ventana, text="Hospitalizado", variable=opcion_covid, value="Hospitalizado", background='#E3F1F1')
radio_hospitalizado.pack()

# Pregunta 3: Otras enfermedades
pregunta_enfermedad = tk.Label(ventana, text="¿Padece de alguna otra enfermedad?", font=('Helvetica',12), background='#E3F1F1')
pregunta_enfermedad.pack()

opcion_enfermedad = tk.StringVar()
opcion_enfermedad.set("Otros/Ninguna")  # Opción predeterminada

opciones_enfermedad = [
    "Diabetes",
    "Hipertensión",
    "Tabaquismo",
    "Obesidad",
    "Otros/Ninguna"
]

def seleccionar_enfermedad(enfermedad):
    opcion_enfermedad.set(enfermedad)

for enfermedad in opciones_enfermedad:
    radio_button = tk.Radiobutton(ventana, text=enfermedad, variable=opcion_enfermedad, value=enfermedad, command=lambda e=enfermedad: seleccionar_enfermedad(e), background='#E3F1F1')
    radio_button.pack()

# Botón de Calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=lambda:calcular(opcion_genero.get(),opcion_covid.get(),opcion_enfermedad.get()), background='#d3d3d3')
boton_calcular.pack()

# Ejecutar la ventana
ventana.mainloop()
