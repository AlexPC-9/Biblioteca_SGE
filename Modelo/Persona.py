class Persona:

    def __init__(self, nombre, apellido, DNI, numTelefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__DNI = DNI
        self.__numTelefono = numTelefono

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self): # <--- Añade esto
        return self.__apellido

    @property
    def dni(self): # <--- Añade esto (fíjate que lo usamos en minúsculas en convertir_Socio)
        return self.__DNI

    @property
    def numTelefono(self): # <--- Añade esto
        return self.__numTelefono

    def toString(self):
        return f"\n DNI: {self.__DNI} \n Nombre Completo: {self.__nombre} {self.__apellido}"