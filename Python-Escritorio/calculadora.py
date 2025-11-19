import tkinter as tk

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.geometry("400x550")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="#1e1e1e")
        
        self.expresion = ""
        self.texto_input = tk.StringVar()
        
        self.crear_pantalla()
        self.crear_botones()
    
    def crear_pantalla(self):
        frame_pantalla = tk.Frame(self.ventana, bg="#1e1e1e")
        frame_pantalla.pack(expand=True, fill="both", padx=10, pady=20)
        
        pantalla = tk.Entry(
            frame_pantalla,
            textvariable=self.texto_input,
            font=("Arial", 32, "bold"),
            bg="#2d2d2d",
            fg="#1e1e1e",
            bd=0,
            justify="right",
            state="readonly"
        )
        pantalla.pack(expand=True, fill="both", ipady=20, padx=5)
    
    def crear_botones(self):
        frame_botones = tk.Frame(self.ventana, bg="#1e1e1e")
        frame_botones.pack(expand=True, fill="both", padx=10, pady=10)
        
        botones = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        for i, fila in enumerate(botones):
            for j, boton in enumerate(fila):
                if boton == '=':
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
        
        for i in range(5):
            frame_botones.grid_rowconfigure(i, weight=1)
        for j in range(4):
            frame_botones.grid_columnconfigure(j, weight=1)
    
    def agregar_caracter(self, caracter):
        self.expresion += str(caracter)
        self.texto_input.set(self.expresion)
    
    def calcular(self):
        try:
            resultado = eval(self.expresion)
            self.texto_input.set(resultado)
            self.expresion = str(resultado)
        except:
            self.texto_input.set("Error")
            self.expresion = ""
    
    def limpiar(self):
        self.expresion = ""
        self.texto_input.set("")
    
    def borrar(self):
        self.expresion = self.expresion[:-1]
        self.texto_input.set(self.expresion)


if __name__ == "__main__":
    ventana = tk.Tk()
    
    calculadora = Calculadora(ventana)
    
    ventana.mainloop()