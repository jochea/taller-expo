import tkinter as tk
from tkinter import messagebox
import random

# Clase que simula el sensor de temperatura y humedad
class Sensor:
    def __init__(self):
        self.temperaturas = []
        self.humedades = []

    def leer_datos(self):
        try:
            # Simular lectura de sensores
            temperatura = random.uniform(0, 50)
            humedad = random.uniform(20, 90)

            # Validar datos simulados
            if not (0 <= temperatura <= 50) or not (20 <= humedad <= 90):
                raise ValueError("Datos fuera de rango.")

            # Guardar en las listas
            self.temperaturas.append(temperatura)
            self.humedades.append(humedad)

            return temperatura, humedad

        except ValueError as e:
            print("Error al leer los datos:", e)
            return None, None

        finally:
            print("Conexión con el sensor cerrada.\n")  # Simulación de cierre de conexión


# Clase principal de la interfaz
class App:
    def __init__(self, root):
        self.sensor = Sensor()
        self.umbral = 30  # Valor por defecto del umbral

        root.title("Monitor de Temperatura y Humedad")
        root.geometry("300x300")

        # Widgets
        self.label_temp = tk.Label(root, text="Temperatura: -- °C", font=("Arial", 12))
        self.label_temp.pack(pady=5)

        self.label_hum = tk.Label(root, text="Humedad: -- %", font=("Arial", 12))
        self.label_hum.pack(pady=5)

        self.estado_label = tk.Label(root, text="Estado: --", font=("Arial", 12), bg="gray", fg="white", width=20)
        self.estado_label.pack(pady=10)

        self.entry_umbral = tk.Entry(root)
        self.entry_umbral.pack(pady=5)

        self.boton_umbral = tk.Button(root, text="Confirmar Umbral", command=self.establecer_umbral)
        self.boton_umbral.pack(pady=5)

        self.boton_actualizar = tk.Button(root, text="Actualizar Datos", command=self.actualizar_datos)
        self.boton_actualizar.pack(pady=10)

    def establecer_umbral(self):
        try:
            valor = float(self.entry_umbral.get())
            self.umbral = valor
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")
        else:
            messagebox.showinfo("Confirmado", f"Umbral establecido en {self.umbral} °C")

    def actualizar_datos(self):
        temperatura, humedad = self.sensor.leer_datos()
        if temperatura is not None and humedad is not None:
            self.label_temp.config(text=f"Temperatura: {temperatura:.2f} °C")
            self.label_hum.config(text=f"Humedad: {humedad:.2f} %")

            if temperatura > self.umbral:
                self.estado_label.config(text="Estado: ALERTA", bg="red")
            else:
                self.estado_label.config(text="Estado: NORMAL", bg="green")


# Ejecutar el programa
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
