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
    def apellido(self): 
        return self.__apellido

    @property
    def dni(self): 
        return self.__DNI

    @property
    def numTelefono(self): 
        return self.__numTelefono

    def toString(self):
        return f"\n DNI: {self.__DNI} \n Nombre Completo: {self.__nombre} {self.__apellido}"