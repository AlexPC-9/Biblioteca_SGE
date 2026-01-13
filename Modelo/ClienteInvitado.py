from Cliente import Cliente

class ClienteInvitado(Cliente):
    def __init__(self, idTemporal, duracionPrestamo):
        super().__init__(self.__historial, self.__productoPrestado, self.__fechaPrestamo, self.__fechaDevolucion)
        self.__idTemporal = idTemporal
        self.__duracionPrestamo = duracionPrestamo

    #GETTER SETTER