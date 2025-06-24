class Usuario:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
    
    def mostrar_info(self):
        return f"Nombre:{self.nombre}, Edad:{self.edad}, Correo:{self.correo}"
