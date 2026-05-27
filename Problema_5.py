#Nombre completo: Yesica Verona Tejada
#Documento de identificación: 1067282635
#Grupo: 213022_32
#Programa Ingenieria de sistemas
#Curso: Fundamentos de Programación 
#Codigo fuente: Autoria Propia

import tkinter as tk
from tkinter import ttk, messagebox #importamos librerías de Python para crear interfaces gráficas

class Problema(tk.Frame): #Creamos una clase llamada Problema en el que se pueden poner texto, bones, cajas
    
    def __init__(self, master=None):
        super().__init__(master)  # master: es la ventana principal donde se va a colocar este frame. super().__init__(master): inicializa correctamente la clase padre (Frame)
        self.place(x=0, y=0, width=800, height=650) #Ubicamos el frame dentro de la ventana y le damos tamaño
        self.configure(background="#eefcff") #color de fondo del frame
        self.widgets() #Llamamos al método que crea todos los componentes gráfico
        
    # Función para calcular horas y clasificar recursos 
    def calcular_horas(self):
        try:
            # Crear matriz con datos ingresados
            recursos = []

            for i in range(4): #Repite el proceso 4 veces porque tienes 4 recursos

                nombre = self.entradas_nombres[i].get() #.get() obtiene el texto escrito

                lunes = float(self.entradas_lunes[i].get())
                martes = float(self.entradas_martes[i].get())
                miercoles = float(self.entradas_miercoles[i].get())
                jueves = float(self.entradas_jueves[i].get())
                viernes = float(self.entradas_viernes[i].get())

                recursos.append([nombre, lunes, martes, miercoles, jueves, viernes]) #Agregamos los datos a la matriz recursos

            resultado = "" #Aquí construiremos el texto final que se mostratá en la interfaz

            # Recorrer matriz
            for recurso in recursos: #Recorre cada fila

                nombre = recurso[0] #obtenemos el nombre del recurso en la posición 0

                # Suma de horas
                total_horas = sum(recurso[1:]) #Sumanos las horas desde la posición 1 hasta el final 

                # Clasificación
                if total_horas > 40: #Si supera las 40 horas, se clasifica como sobretiempo
                    clasificacion = "Sobretiempo"
                else:
                    clasificacion = "Horario Estándar" #Si no supera las 40 horas, se clasifica como horario estándar

                resultado += ( #Concatenamos el resultado para cada recurso
                    f"Recurso: {nombre}\n"
                    f"Total de Horas: {total_horas}\n"
                    f"Clasificación: {clasificacion}\n"
                    f"\n"
                )

            # Mostrar resultado
            self.texto_resultado.config(state="normal")
            self.texto_resultado.delete("1.0", tk.END)
            self.texto_resultado.insert(tk.END, resultado)
            self.texto_resultado.config(state="disabled")

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos en las horas.") #Se ejecuta si el usuario escribe algo inválido

    # Se construye toda la interfaz
    def widgets(self):

        #Creamos un titulo
        titulo = tk.Label(self, text="CONTROL DE HORAS SEMANALES", font=("Arial", 16, "bold"), bg="#eefcff", fg="#000000")
        titulo.place(x=240, y=20)

        # Creamos los encabezados
        encabezados = ["Nombre", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

        x_posiciones = [80, 230, 330, 430, 530, 630]

        for i in range(len(encabezados)):
            tk.Label(self, text=encabezados[i], font=("Arial", 12, "bold"), bg="#eefcff").place(x=x_posiciones[i], y=60)

        # Listas de entradas
        self.entradas_nombres = []
        self.entradas_lunes = []
        self.entradas_martes = []
        self.entradas_miercoles = []
        self.entradas_jueves = []
        self.entradas_viernes = []

        # Crear filas para 4 recursos
        for fila in range(4):

            y = 100 + (fila * 40)

            # Nombre
            entrada_nombre = tk.Entry(self)
            entrada_nombre.place(x=80, y=y, width=120)
            self.entradas_nombres.append(entrada_nombre) #Guardamos en lista

            # Lunes
            entrada_lunes = tk.Entry(self)
            entrada_lunes.place(x=230, y=y, width=70)
            self.entradas_lunes.append(entrada_lunes)

            # Martes
            entrada_martes = tk.Entry(self)
            entrada_martes.place(x=330, y=y, width=70)
            self.entradas_martes.append(entrada_martes)

            # Miércoles
            entrada_miercoles = tk.Entry(self)
            entrada_miercoles.place(x=430, y=y, width=70)
            self.entradas_miercoles.append(entrada_miercoles)

            # Jueves
            entrada_jueves = tk.Entry(self)
            entrada_jueves.place(x=530, y=y, width=70)
            self.entradas_jueves.append(entrada_jueves)

            # Viernes
            entrada_viernes = tk.Entry(self)
            entrada_viernes.place(x=630, y=y, width=70)
            self.entradas_viernes.append(entrada_viernes)

        # Botón
        boton_calcular = tk.Button(self, text="Calcular Horas", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.calcular_horas)
        boton_calcular.place(x=350, y=280, width=160, height=40)

        # Área de resultados
        self.texto_resultado = tk.Text(self, font=("Consolas", 11), state="disabled")
        self.texto_resultado.place(x=80, y=340, width=650, height=270)
        
# Crear ventana principal
ventana_principal = tk.Tk() #Crea la ventana principal
ventana_principal.geometry("800x650") #Medidas de la ventana
ventana_principal.resizable(False, False) #Para que no se pueda extender
ventana_principal.title("Problema 5") #Titulo de la ventana
app = Problema(master=ventana_principal) #Crea la interfaz dentro de la ventana

ventana_principal.mainloop() #Inicia el programa (bucle infinito que mantiene la ventana abierta)