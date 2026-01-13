from Persona import Persona

class Cliente(Persona):
    def __init__(self, historial, productoPrestado, fechaPrestamo, fechaDevolucion):
        super().__init__(self.__nombre, self.__apellido, self.__DNI, self.__numTelefono)
        self.__historial = historial
        self.__productoPrestado = productoPrestado
        self.__fechaPrestamo = fechaPrestamo
        self.__fechaDevolucion = fechaDevolucion

    #Getter setter, herencia
        