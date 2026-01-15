from Persona import Persona

class Cliente(Persona):
    def __init__(self, historial, productoPrestado, fechaPrestamo, fechaDevolucion):
        super().__init__(self.__nombre, self.__apellido, self.__DNI, self.__numTelefono)
        self.__historial = historial
        self.__productoPrestado = productoPrestado
        self.__fechaPrestamo = fechaPrestamo
        self.__fechaDevolucion = fechaDevolucion

    #Getter setter
    def toString():
        return(f"Nombre: {Persona.__nombre}\n" 
               f"Apellido: {Persona.__apellido}\n"
                f"Historial: {Cliente.__historial}\n"
               )
