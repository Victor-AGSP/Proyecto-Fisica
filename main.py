import math
import Tkinter as tk
import matplotlib.pyplot as plt

# Función para calcular la energía y la fuerza de roce
def calcular():
    # Obtener los valores de entrada
    longitud = float(entry_longitud.get())
    angulo = float(entry_angulo.get())
    masa = float(entry_masa.get())
    constante_roce = float(entry_roce.get())

    # Cálculo de la energía potencial gravitatoria
    energia_potencial = masa * 9.8 * (longitud - longitud * math.cos(math.radians(angulo)))

    # Cálculo de la fuerza de roce
    fuerza_roce = constante_roce * math.radians(angulo)

    # Actualizar las etiquetas con los resultados
    label_energia.config(text="Energía potencial: " + str(energia_potencial))
    label_roce.config(text="Fuerza de roce: " + str(fuerza_roce))

def datos():
    # Crear un widget Label con el texto deseado
    etiqueta = tk.Label(ventana, text="Peso del Objeto")
    # Colocar el widget en la ventana
    etiqueta.pack()

    # Graficar el péndulo
    plt.plot(tiempo, posicion)
    plt.xlabel('Ángulo (grados)')
    plt.ylabel('Posición')
    plt.title('Péndulo')
    plt.show()

# Crear la ventana principal
window = tk.Tk()
window.title("Energía y fuerza de roce en un péndulo")
window.geometry("300x250")

# Etiquetas
label_longitud = tk.Label(window, text="Longitud del péndulo (m):")
label_longitud.pack()
entry_longitud = tk.Entry(window)
entry_longitud.pack()

label_angulo = tk.Label(window, text="Ángulo inicial (grados):")
label_angulo.pack()
entry_angulo = tk.Entry(window)
entry_angulo.pack()

label_masa = tk.Label(window, text="Masa del objeto (kg):")
label_masa.pack()
entry_masa = tk.Entry(window)
entry_masa.pack()

label_roce = tk.Label(window, text="Constante de roce:")
label_roce.pack()
entry_roce = tk.Entry(window)
entry_roce.pack()

label_energia = tk.Label(window, text="")
label_energia.pack()

# Botón para calcular
btn_calcular = tk.Button(window, text="Calcular", command=calcular)
btn_calcular.pack()

# Ejecutar la ventana
window.mainloop()