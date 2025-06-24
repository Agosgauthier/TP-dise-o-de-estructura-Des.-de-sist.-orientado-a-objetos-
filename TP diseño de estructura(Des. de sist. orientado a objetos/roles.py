from usuario import Usuario

class Admin(Usuario):
    def __init__(self, nombre, edad, correo, nivel_acceso):
        Usuario.__init__(self, nombre, edad, correo)
        self.nivel_acceso = nivel_acceso
    
    def mostrar_info(self):
        return f"[Admin] Nombre:{self.nombre}, Edad:{self.edad}, Correo:{self.correo}, Nivel de Acceso:{self.nivel_acceso}"

class Cliente(Usuario):
    def __init__(self, nombre, edad, correo, cuenta_id):
        Usuario.__init__(self, nombre, edad, correo)
        self.cuenta_id = cuenta_id
    
    def mostrar_info(self):
        return f"[Cliente] Nombre:{self.nombre}, Edad:{self.edad}, Correo:{self.correo}, Cuenta ID:{self.cuenta_id}"
