import re

def validar_contrasena (password: int) -> bool:
    
    pattern = r"^(?=.*[a-zñ])(?=.*[A-ZÑ])(?=.*\d)(?=.*[@*?\-])[A-Za-zñÑ][A-Za-zñÑ\d@*?\-]{4,13}$"
    if re.match(pattern, password):
        return True
    else:
        return False 
