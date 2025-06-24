from roles import Admin, Cliente
from trabajador import Gerente, Empleado

class GestorUsuarios:
    usuarios = []

    @staticmethod
    def agregar_usuario(usuario):
        GestorUsuarios.usuarios.append(usuario)

    @staticmethod
    def mostrar_usuarios():
        for usuario in GestorUsuarios.usuarios:
            print(usuario.mostrar_info())
