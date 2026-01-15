class Persona:
    def __init__(self, nombre, apellido, DNI, numTelefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__DNI = DNI
        self.__numTelefono = numTelefono

    # GETTER
    @property
    def nombre(self):
        return self.__nombre

    # SETTER
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre
        else:
            print("Error: El nombre no puede estar vacío")

    def toString(self):
        return f"DNI: {self.__DNI} | Nombre Completo: {self.__nombre} {self.__apellido}"