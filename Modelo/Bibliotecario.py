from Modelo.Persona import Persona

class Bibliotecario(Persona):
    def __init__(self, nombre, apellido, DNI, numTelefono, idTrabajador, turno):
        super().__init__(nombre, apellido, DNI, numTelefono)
        self.__idTrabajador = idTrabajador
        self.__turno = turno

    @property
    def idTrabajador(self):
        return self.__idTrabajador

    @idTrabajador.setter
    def idTrabajador(self, valor):
        self.__idTrabajador = valor

    def toString(self):
        return f"{super().toString()} | ID Empleado: {self.__idTrabajador} | Turno: {self.__turno}"