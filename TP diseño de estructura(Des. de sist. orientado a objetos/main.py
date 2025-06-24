from gestor_usuario import GestorUsuarios
from roles import Admin, Cliente
from trabajador import Gerente, Empleado

GestorUsuarios.agregar_usuario(Admin("Ana", 35, "ana@email.com", "Alto"))
GestorUsuarios.agregar_usuario(Cliente("Luis", 28, "luis@email.com", "C123"))
GestorUsuarios.agregar_usuario(Gerente("Carlos", 40, "carlos@email.com", "Ventas"))
GestorUsuarios.agregar_usuario(Empleado("Marta", 30, "marta@email.com", 3500))

GestorUsuarios.mostrar_usuarios()
