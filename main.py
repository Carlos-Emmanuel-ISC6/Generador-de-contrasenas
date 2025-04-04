import customtkinter as ctk
from prueba_contrasena import validar_contrasena

class AplicacionValidadorContrasena:
   def __init__(self, interfaz):
       self.interfaz = interfaz
       self.interfaz.title("Validador de Contraseñas")
       self.interfaz.geometry("400x300")
       self.interfaz.minsize(300, 250)
       
       self.interfaz.grid_columnconfigure(0, weight=1)
       self.interfaz.grid_rowconfigure(0, weight=1)
       
       ctk.set_appearance_mode("light")
       ctk.set_default_color_theme("blue")
       
       self.marco = ctk.CTkFrame(self.interfaz)
       self.marco.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
       
       self.marco.grid_columnconfigure(0, weight=1)
       for i in range(5):
           self.marco.grid_rowconfigure(i, weight=1)
       
       self.etiqueta_titulo = ctk.CTkLabel(
           self.marco, 
           text="Validador de Contraseñas",
           font=ctk.CTkFont(size=20, weight="bold")
       )
       self.etiqueta_titulo.grid(row=0, column=0, pady=10, sticky="ew")
       
       self.etiqueta_descripcion = ctk.CTkLabel(
           self.marco, 
           text="Ingrese una contraseña para validar"
       )
       self.etiqueta_descripcion.grid(row=1, column=0, pady=5, sticky="ew")
       
       self.entrada_contrasena = ctk.CTkEntry(
           self.marco, 
           placeholder_text="Contraseña",
           width=250
       )
       self.entrada_contrasena.grid(row=2, column=0, pady=10, sticky="ew", padx=40)
       
       self.boton_validar = ctk.CTkButton(
           self.marco, 
           text="Validar Contraseña",
           command=self.validar_contrasena,
           width=200
       )
       self.boton_validar.grid(row=3, column=0, pady=10, sticky="ew", padx=60)
       
       self.etiqueta_resultado = ctk.CTkLabel(self.marco, text="")
       self.etiqueta_resultado.grid(row=4, column=0, pady=10, sticky="ew")
   
   def validar_contrasena(self):
    contrasena = self.entrada_contrasena.get()
    
    if contrasena.strip() == "":
        self.etiqueta_resultado.configure(text="Por favor ingrese una contraseña", text_color="orange")
        return
    
    if validar_contrasena(contrasena):
        self.etiqueta_resultado.configure(text="✓ Contraseña válida", text_color="green")
    else:
        self.etiqueta_resultado.configure(text="✗ Contraseña inválida", text_color="red")

    self.entrada_contrasena.delete(0, 'end')
if __name__ == "__main__":
   interfaz = ctk.CTk()
   app = AplicacionValidadorContrasena(interfaz)
   interfaz.mainloop()