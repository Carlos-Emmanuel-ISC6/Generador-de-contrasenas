import customtkinter as ctk
import re

class AplicacionValidadorContrasena:
    def __init__(self, interfaz):
        self.interfaz = interfaz
        self.interfaz.title("Validador de Contraseñas")
        self.interfaz.geometry("900x600")  # Aumentamos la altura de la ventana
        self.interfaz.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.interfaz.grid_rowconfigure(0, weight=1)
        self.interfaz.grid_columnconfigure(0, weight=1)
        self.interfaz.grid_columnconfigure(1, weight=1)

        # Marco izquierdo
        self.marco_izquierdo = ctk.CTkFrame(self.interfaz, width=450, height=450)  # Tamaño fijo para el marco izquierdo
        self.marco_izquierdo.grid(row=0, column=0, padx=15, pady=15)

        self.etiqueta_titulo = ctk.CTkLabel(self.marco_izquierdo, text="Validador de Contraseñas", font=ctk.CTkFont(size=24, weight="bold"), anchor="center")
        self.etiqueta_titulo.grid(row=0, column=0, pady=(15, 10), padx=20, sticky="ew")

        self.entrada_contrasena = ctk.CTkEntry(self.marco_izquierdo, placeholder_text="Contraseña", width=350, height=40, border_width=1, corner_radius=5, font=ctk.CTkFont(size=15))
        self.entrada_contrasena.grid(row=1, column=0, pady=(0, 15), padx=20, sticky="ew")

        self.boton_validar = ctk.CTkButton(self.marco_izquierdo, text="Validar Contraseña", command=self.validar_contrasena, width=350, height=40, fg_color="#3498db", hover_color="#2980b9", font=ctk.CTkFont(size=16))
        self.boton_validar.grid(row=2, column=0, pady=(0, 15), padx=20, sticky="ew")

        self.etiqueta_resultado = ctk.CTkLabel(self.marco_izquierdo, text="", font=ctk.CTkFont(size=18, weight="bold"), anchor="center")
        self.etiqueta_resultado.grid(row=3, column=0, pady=(0, 10), padx=20, sticky="ew")

        self.etiqueta_expresion_titulo = ctk.CTkLabel(self.marco_izquierdo, text="Expresión Regular", font=ctk.CTkFont(size=16, weight="bold"), text_color="black", anchor="center")
        self.etiqueta_expresion = ctk.CTkLabel(self.marco_izquierdo, text="", font=ctk.CTkFont(size=10), wraplength=380, justify="center", anchor="center")

        self.etiqueta_expresion_titulo.grid(row=4, column=0, pady=(5, 0), padx=20, sticky="ew")
        self.etiqueta_expresion.grid(row=5, column=0, pady=(2, 15), padx=20, sticky="ew")

        # Nueva área de texto grande con su título
        self.etiqueta_analisis_titulo = ctk.CTkLabel(self.marco_izquierdo, text="Análisis de Cadena", font=ctk.CTkFont(size=16, weight="bold"), anchor="center")
        self.etiqueta_analisis_titulo.grid(row=6, column=0, pady=(5, 10), padx=20, sticky="ew")

        self.area_texto_grande = ctk.CTkTextbox(self.marco_izquierdo, width=350, height=200, font=ctk.CTkFont(size=14), corner_radius=5, border_width=1)
        self.area_texto_grande.grid(row=7, column=0, pady=(5, 20), padx=20, sticky="ew")

        # Marco derecho
        self.marco_derecho = ctk.CTkFrame(self.interfaz, width=450, height=450)  # Tamaño fijo para el marco derecho
        self.marco_derecho.grid(row=0, column=1, padx=15, pady=15)

        self.etiqueta_titulo_requisitos = ctk.CTkLabel(self.marco_derecho, text="Requisitos de la Contraseña", font=ctk.CTkFont(size=22, weight="bold"), anchor="center")
        self.etiqueta_titulo_requisitos.grid(row=0, column=0, pady=(20, 15), padx=20, sticky="ew")

        requisitos_texto = [
            "Mínimo 5 y máximo 14 caracteres",
            "Debe comenzar con una letra",
            "Al menos una letra mayúscula",
            "Al menos una letra minúscula",
            "Al menos un número",
            "Al menos un carácter especial (@ * ? -)"
        ]

        self.requisitos_labels = []
        for i, texto in enumerate(requisitos_texto):
            etiqueta = ctk.CTkLabel(self.marco_derecho, text=f"• {texto}", font=ctk.CTkFont(size=16), justify="center", anchor="center")
            etiqueta.grid(row=i+1, column=0, pady=2, padx=20, sticky="ew")
            self.requisitos_labels.append(etiqueta)

    def validar_contrasena(self):
        contrasena = self.entrada_contrasena.get()
        pattern = r"^(?=.*[a-zñ])(?=.*[A-ZÑ])(?=.*\d)(?=.*[@*?\-])[A-Za-zñÑ][A-Za-zñÑ\d@*?\-]{4,13}$"

        if contrasena.strip() == "":
            self.etiqueta_resultado.configure(text="Por favor ingrese una contraseña", text_color="orange")
            self.resetear_requisitos()
            self.etiqueta_expresion.configure(text="", text_color="black")
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
        self.entrada_contrasena.delete(0, 'end')

    def verificar_requisitos(self, contrasena):
        cumple = []

        cumple.append(5 <= len(contrasena) <= 14)
        cumple.append(bool(re.match(r'^[A-Za-zñÑ]', contrasena)))
        cumple.append(bool(re.search(r'[A-ZÑ]', contrasena)))
        cumple.append(bool(re.search(r'[a-zñ]', contrasena)))
        cumple.append(bool(re.search(r'\d', contrasena)))
        cumple.append(bool(re.search(r'[@*?\-]', contrasena)))

        for i, etiqueta in enumerate(self.requisitos_labels):
            texto_base = etiqueta.cget("text")[2:]
            if cumple[i]:
                etiqueta.configure(text=f"✓ {texto_base}", text_color="green")
            else:
                etiqueta.configure(text=f"✗ {texto_base}", text_color="red")

        return all(cumple)

    def resetear_requisitos(self):
        textos_originales = [
            "Mínimo 5 y máximo 14 caracteres",
            "Debe comenzar con una letra",
            "Al menos una letra mayúscula",
            "Al menos una letra minúscula",
            "Al menos un número",
            "Al menos un carácter especial (@ * ? -)"
        ]
        for i, etiqueta in enumerate(self.requisitos_labels):
            etiqueta.configure(text=f"• {textos_originales[i]}", text_color=("black", "white"))

if __name__ == "__main__":
    interfaz = ctk.CTk()
    app = AplicacionValidadorContrasena(interfaz)
    interfaz.mainloop()
