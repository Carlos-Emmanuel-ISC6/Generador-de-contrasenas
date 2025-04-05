import customtkinter as ctk
import re

class AplicacionValidadorContrasena:
    def __init__(self, interfaz):
        self.interfaz = interfaz
        self.interfaz.title("Validador de Contraseñas")
        self.interfaz.geometry("900x600") 
        self.interfaz.resizable(0, 0)

        ctk.set_appearance_mode("light")  
        ctk.set_default_color_theme("blue")

        self.interfaz.grid_rowconfigure(0, weight=1)
        self.interfaz.grid_columnconfigure(0, weight=1)
        self.interfaz.grid_columnconfigure(1, weight=1)

        self.marco_izquierdo = ctk.CTkFrame(self.interfaz, width=450, height=450, corner_radius=15)  
        self.marco_izquierdo.grid(row=0, column=0, padx=15, pady=15)

        self.etiqueta_titulo = ctk.CTkLabel(self.marco_izquierdo, text="Validador de Contraseñas", font=ctk.CTkFont(family="Roboto", size=24, weight="bold"), anchor="center")
        self.etiqueta_titulo.grid(row=0, column=0, pady=(15, 10), padx=20, sticky="ew")

        self.entrada_contrasena = ctk.CTkEntry(self.marco_izquierdo, placeholder_text="Contraseña", width=350, height=40, border_width=2, corner_radius=10, font=ctk.CTkFont(size=15))
        self.entrada_contrasena.grid(row=1, column=0, pady=(0, 15), padx=20, sticky="ew")

        self.boton_validar = ctk.CTkButton(self.marco_izquierdo, text="Validar Contraseña", command=self.validar_contrasena, width=350, height=40, fg_color="#3498db", hover_color="#2980b9", font=ctk.CTkFont(size=16), corner_radius=10)
        self.boton_validar.grid(row=2, column=0, pady=(0, 15), padx=20, sticky="ew")

        self.etiqueta_resultado = ctk.CTkLabel(self.marco_izquierdo, text="", font=ctk.CTkFont(size=18, weight="bold"), anchor="center")
        self.etiqueta_resultado.grid(row=3, column=0, pady=(0, 10), padx=20, sticky="ew")

        self.marco_expresion = ctk.CTkFrame(self.marco_izquierdo, corner_radius=10)
        self.marco_expresion.grid(row=4, column=0, pady=(5, 15), padx=20, sticky="ew")
        
        self.etiqueta_expresion_titulo = ctk.CTkLabel(self.marco_expresion, text="Expresión Regular", font=ctk.CTkFont(size=16, weight="bold"), anchor="center")
        self.etiqueta_expresion_titulo.grid(row=0, column=0, pady=(10, 0), padx=20, sticky="ew")
        
        self.etiqueta_expresion = ctk.CTkLabel(self.marco_expresion, text="", font=ctk.CTkFont(size=12), wraplength=380, justify="center", anchor="center")
        self.etiqueta_expresion.grid(row=1, column=0, pady=(0, 10), padx=20, sticky="ew")

        self.etiqueta_analisis_titulo = ctk.CTkLabel(self.marco_izquierdo, text="Análisis de Cadena", font=ctk.CTkFont(size=16, weight="bold"), anchor="center")
        self.etiqueta_analisis_titulo.grid(row=5, column=0, pady=(5, 10), padx=20, sticky="ew")

        self.area_texto_grande = ctk.CTkTextbox(self.marco_izquierdo, width=350, height=200, font=ctk.CTkFont(size=14), corner_radius=10, border_width=2)
        self.area_texto_grande.grid(row=6, column=0, pady=(5, 20), padx=20, sticky="ew")

        self.marco_derecho = ctk.CTkFrame(self.interfaz, width=450, height=450, corner_radius=15) 
        self.marco_derecho.grid(row=0, column=1, padx=15, pady=15)

        self.etiqueta_titulo_requisitos = ctk.CTkLabel(self.marco_derecho, text="Requisitos de la Contraseña", font=ctk.CTkFont(size=22, weight="bold"), anchor="center")
        self.etiqueta_titulo_requisitos.grid(row=0, column=0, pady=(20, 15), padx=20, sticky="ew")

        self.marco_requisitos = ctk.CTkFrame(self.marco_derecho, corner_radius=10)
        self.marco_requisitos.grid(row=1, column=0, pady=(0, 15), padx=20, sticky="ew")

        requisitos_texto = [
            "Mínimo 5 y máximo 14 caracteres",
            "Debe comenzar con una letra",
            "Al menos una letra mayúscula",
            "Al menos una letra minúscula",
            "Al menos un número",
            "Al menos un carácter especial (@ * ? -)"
        ]
        requisitos_iconos = ["📏", "🔤", "🔠", "🔡", "🔢", "🔣"]
        
        self.requisitos_labels = []
        for i, texto in enumerate(requisitos_texto):
            marco_req = ctk.CTkFrame(self.marco_requisitos, corner_radius=5)
            marco_req.grid(row=i, column=0, pady=5, padx=10, sticky="ew")
            etiqueta = ctk.CTkLabel(marco_req, text=f"{requisitos_iconos[i]} {texto}", font=ctk.CTkFont(size=16), pady=5)
            etiqueta.grid(row=0, column=0, padx=10, sticky="w")
            self.requisitos_labels.append(etiqueta)

    def validar_contrasena(self):
        contrasena = self.entrada_contrasena.get()
        pattern = r"^(?=.*[a-zñ])(?=.*[A-ZÑ])(?=.*\d)(?=.*[@*?\-])[A-Za-zñÑ][A-Za-zñÑ\d@*?\-]{4,13}$"

        if contrasena.strip() == "":
            self.etiqueta_resultado.configure(text="Por favor ingrese una contraseña", text_color="orange")
            self.resetear_requisitos()
            self.etiqueta_expresion.configure(text="", text_color="black")
            self.area_texto_grande.delete("0.0", "end")
            return

        cumple_requisitos = self.verificar_requisitos(contrasena)
        es_valida = re.match(pattern, contrasena) is not None

        if es_valida:
            self.etiqueta_resultado.configure(text="✓ Contraseña válida", text_color="green")
            color_texto = "green"
        else:
            self.etiqueta_resultado.configure(text="✗ Contraseña inválida", text_color="red")
            color_texto = "red"

        self.etiqueta_expresion.configure(text=pattern, text_color=color_texto)
        self.area_texto_grande.delete("0.0", "end")
        self.entrada_contrasena.delete(0, 'end')

    def verificar_requisitos(self, contrasena):
        cumple = [
            5 <= len(contrasena) <= 14,
            bool(re.match(r'^[A-Za-zñÑ]', contrasena)),
            bool(re.search(r'[A-ZÑ]', contrasena)),
            bool(re.search(r'[a-zñ]', contrasena)),
            bool(re.search(r'\d', contrasena)),
            bool(re.search(r'[@*?\-]', contrasena))
        ]
        requisitos_iconos = ["📏", "🔤", "🔠", "🔡", "🔢", "🔣"]
        textos_base = [
            "Mínimo 5 y máximo 14 caracteres",
            "Debe comenzar con una letra",
            "Al menos una letra mayúscula",
            "Al menos una letra minúscula",
            "Al menos un número",
            "Al menos un carácter especial (@ * ? -)"
        ]

        for i, etiqueta in enumerate(self.requisitos_labels):
            etiqueta.configure(text=f"{requisitos_iconos[i]} {textos_base[i]} {'✓' if cumple[i] else '✗'}", text_color="green" if cumple[i] else "red")
        return all(cumple)

    def resetear_requisitos(self):
        requisitos_iconos = ["📏", "🔤", "🔠", "🔡", "🔢", "🔣"]
        textos_originales = [
            "Mínimo 5 y máximo 14 caracteres",
            "Debe comenzar con una letra",
            "Al menos una letra mayúscula",
            "Al menos una letra minúscula",
            "Al menos un número",
            "Al menos un carácter especial (@ * ? -)"
        ]
        for i, etiqueta in enumerate(self.requisitos_labels):
            etiqueta.configure(text=f"{requisitos_iconos[i]} {textos_originales[i]}", text_color="black")

if __name__ == "__main__":
    interfaz = ctk.CTk()
    app = AplicacionValidadorContrasena(interfaz)
    interfaz.mainloop()
