import math
import Tkinter as tk
import matplotlib.pyplot as plt

# Funcion para calcular la energia y la fuerza de roce
def calcular():
    # Obtener los valores de entrada
    longitud = float(entry_longitud.get())
    angulo = float(entry_angulo.get())
    masa = float(entry_masa.get())
    constante_roce = float(entry_roce.get())

    # Calculo de la energia potencial gravitatoria
    energia_potencial = masa * 9.8 * (longitud - longitud * math.cos(math.radians(angulo)))

    # Calculo de la fuerza de roce
    fuerza_roce = constante_roce * math.radians(angulo)

    # Actualizar las etiquetas con los resultados
    label_energia.config(text="Energia potencial: " + str(energia_potencial))
    label_roce.config(text="Fuerza de roce: " + str(fuerza_roce))

    # Crear los datos para graficar el pandulo
    tiempo = range(0, 361, 10)  # Valores de tiempo de 0 a 360 grados con incremento de 10 grados
    posicion = [longitud * math.sin(math.radians(t)) for t in tiempo]  # Calcular la posicion en funcion del tiempo

    # Graficar el pendulo
    plt.plot(tiempo, posicion)
    plt.xlabel('angulo (grados)')
    plt.ylabel('Posicion')
    plt.title('Pendulo')
    plt.show()

# Crear la ventana principal
window = tk.Tk()
window.title("Energia y fuerza de roce en un pendulo")
window.geometry("300x250")

# Etiquetas
label_longitud = tk.Label(window, text="Longitud del pendulo (m):")
label_longitud.pack()
entry_longitud = tk.Entry(window)
entry_longitud.pack()

label_angulo = tk.Label(window, text="angulo inicial (grados):")
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

# Boton para calcular
btn_calcular = tk.Button(window, text="Calcular", command=calcular)
btn_calcular.pack()

# Ejecutar la ventana
window.mainloop()
