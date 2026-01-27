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
        return f"{super().toString()} \n ID Empleado: {self.__idTrabajador} \n Turno: {self.__turno}"
    
    def insertarLibros(self, biblioteca, nuevoLibro):
        biblioteca.inventario.append(nuevoLibro)
        print(f"Biblioteca {biblioteca} : {nuevoLibro} añadido al inventario")

    def añadirHistorial(self, cliente, prod):
        cliente.historial.append(prod)
        print(f"Historial actualizado para {cliente.nombre} se añadio {prod}")
    
    def invitado_a_socio(self, invitado, nuevo_id):
        print(f"bibliotecario: {self.nombre}")
        nuevo_socio = invitado.convertir_Socio(nuevo_id)
        return nuevo_socio