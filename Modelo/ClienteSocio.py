from Cliente import Cliente

class ClienteSocio(Cliente):
    def __init__(self, idSocio, duracionPrestamoPremium):
        super().__init__(self.__historial, self.__productoPrestado, self.__fechaPrestamo, self.__fechaDevolucion)
        self.__idSocio = idSocio
        self.__duracionPrestamoPremium = duracionPrestamoPremium

        