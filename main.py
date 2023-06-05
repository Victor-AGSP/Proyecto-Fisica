import tkinter as tk

# Crear Ventana
ventana = tk.Tk()

def configurar():
    # Título de la ventana
    #ventana.title("Energía y trabajo de la fuerza de roce (Sistema no conservativo)")
    ventana.title("Proyecto Fisica")

    # Tamaño de la ventana
    ancho = 400
    alto = 300
    ventana.geometry(f"{ancho}x{alto}")

    # Fijar tamaño de la ventana
    ventana.resizable(False, False)

def datos():
    # Crear un widget Label con el texto deseado
    etiqueta = tk.Label(ventana, text="Peso del Objeto")
    # Colocar el widget en la ventana
    etiqueta.pack()

configurar()
datos()

# Mantener ventana permanente
ventana.mainloop()