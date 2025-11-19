import tkinter as tk

class Calculadora:
    def __init__(self, ventana):
        # Configuración de la ventana principal
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.geometry("400x550")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="#1e1e1e")
        
        # Variables para almacenar la expresión
        self.expresion = ""
        self.texto_input = tk.StringVar()
        
        # Crear la interfaz
        self.crear_pantalla()
        self.crear_botones()
    
    def crear_pantalla(self):
        """Crea la pantalla de la calculadora"""
        # Frame contenedor para la pantalla
        frame_pantalla = tk.Frame(self.ventana, bg="#1e1e1e")
        frame_pantalla.pack(expand=True, fill="both", padx=10, pady=20)
        
        # Pantalla (Entry) donde se muestra la expresión y resultado
        pantalla = tk.Entry(
            frame_pantalla,
            textvariable=self.texto_input,
            font=("Arial", 32, "bold"),
            bg="#2d2d2d",
            fg="#ffffff",
            bd=0,
            justify="right",
            state="readonly"
        )
        pantalla.pack(expand=True, fill="both", ipady=20, padx=5)
    
    def crear_botones(self):
        """Crea todos los botones de la calculadora"""
        # Frame contenedor para los botones
        frame_botones = tk.Frame(self.ventana, bg="#1e1e1e")
        frame_botones.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Definir la distribución de botones
        botones = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        # Crear cada botón con su configuración
        for i, fila in enumerate(botones):
            for j, boton in enumerate(fila):
                if boton == '=':
                    # Botón igual (verde, ocupa 2 columnas)
                    btn = tk.Button(
                        frame_botones,
                        text=boton,
                        font=("Arial", 20, "bold"),
                        bg="#00a67e",
                        fg="white",
                        activebackground="#008c69",
                        activeforeground="white",
                        bd=0,
                        command=lambda: self.calcular()
                    )
                    btn.grid(row=i, column=j, columnspan=2, sticky="nsew", padx=2, pady=2)
                
                elif boton in ['C', '⌫']:
                    # Botones de limpiar y borrar (rojo)
                    btn = tk.Button(
                        frame_botones,
                        text=boton,
                        font=("Arial", 20, "bold"),
                        bg="#d4526e",
                        fg="white",
                        activebackground="#b83d59",
                        activeforeground="white",
                        bd=0,
                        command=lambda b=boton: self.limpiar() if b == 'C' else self.borrar()
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
                
                elif boton in ['/', '*', '-', '+', '%']:
                    # Botones de operadores (gris oscuro)
                    btn = tk.Button(
                        frame_botones,
                        text=boton,
                        font=("Arial", 20, "bold"),
                        bg="#505050",
                        fg="white",
                        activebackground="#3d3d3d",
                        activeforeground="white",
                        bd=0,
                        command=lambda b=boton: self.agregar_caracter(b)
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
                
                else:
                    # Botones numéricos y punto decimal (gris)
                    btn = tk.Button(
                        frame_botones,
                        text=boton,
                        font=("Arial", 20),
                        bg="#3a3a3a",
                        fg="white",
                        activebackground="#2d2d2d",
                        activeforeground="white",
                        bd=0,
                        command=lambda b=boton: self.agregar_caracter(b)
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
        
        # Configurar el tamaño de las filas y columnas
        for i in range(5):
            frame_botones.grid_rowconfigure(i, weight=1)
        for j in range(4):
            frame_botones.grid_columnconfigure(j, weight=1)
    
    def agregar_caracter(self, caracter):
        """Agrega un carácter a la expresión"""
        self.expresion += str(caracter)
        self.texto_input.set(self.expresion)
    
    def calcular(self):
        """Evalúa la expresión matemática y muestra el resultado"""
        try:
            resultado = eval(self.expresion)
            self.texto_input.set(resultado)
            self.expresion = str(resultado)
        except:
            self.texto_input.set("Error")
            self.expresion = ""
    
    def limpiar(self):
        """Limpia toda la expresión"""
        self.expresion = ""
        self.texto_input.set("")
    
    def borrar(self):
        """Borra el último carácter de la expresión"""
        self.expresion = self.expresion[:-1]
        self.texto_input.set(self.expresion)


# Programa principal
if __name__ == "__main__":
    # Crear la ventana principal
    ventana = tk.Tk()
    
    # Crear la calculadora
    calculadora = Calculadora(ventana)
    
    # Iniciar el loop de la aplicación
    ventana.mainloop()