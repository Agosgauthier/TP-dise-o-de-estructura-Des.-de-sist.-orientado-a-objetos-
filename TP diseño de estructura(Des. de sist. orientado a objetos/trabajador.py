from usuario import Usuario

class Trabajador(Usuario):
    def __init__(self, nombre, edad, correo, cargo):
        Usuario.__init__(self, nombre, edad, correo)
        self.cargo = cargo
    
    def mostrar_info(self):
        return f"[Trabajador] Nombre:{self.nombre}, Edad:{self.edad}, Correo:{self.correo}, Cargo:{self.cargo}"

class Gerente(Trabajador):
    def __init__(self, nombre, edad, correo, departamento):
        Trabajador.__init__(self, nombre, edad, correo, "Gerente")
        self.departamento = departamento
    
    def mostrar_info(self):
        return f"[Gerente] Nombre:{self.nombre}, Edad:{self.edad}, Correo:{self.correo}, Cargo:{self.cargo}, Departamento:{self.departamento}"

class Empleado(Trabajador):
    def __init__(self, nombre, edad, correo, salario):
        Trabajador.__init__(self, nombre, edad, correo, "Empleado")
        self.salario = salario
    
    def mostrar_info(self):
        return f"[Empleado] Nombre:{self.nombre}, Edad:{self.edad}, Correo:{self.correo}, Cargo:{self.cargo}, Salario:{self.salario}"