import tkinter as tk
import random
import time

class sensor:
    def __init__ (self):
        self.temperatura = 0
        self.humedad = 0
        self.prueba = True
    
    def leerDatos (self):
        try:
            while self.prueba:
            self.temperatura = random.uniform(0, 50)
            self.humedad = random.uniform(20, 90)
                
        except
            print("Error al leer los datos del sensor")
        
        finally:
            print("sensor detenido")
            
pass


class interfaz:
    
    def __init__ (self, raiz):
        self.raiz = raiz
        self.sensor = sensor()
        self.umbral = 
        
    raiz.tittle("Monitor de temperatura y humedad")
    raiz.geometry("320x270")
    
    self.label.temp = (tk.Label raiz, text="Temperatura:   "c"" font=("Arial" ,12))
    
    self.label.temp = (tk.Label raiz, text="Humedad:   "%"" font=("Arial" ,12))
    
    
    def Actualizar_interfaz:
        pass
