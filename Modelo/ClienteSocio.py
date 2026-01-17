from Cliente import Cliente

class ClienteSocio(Cliente):
    def __init__(self, idSocio, duracionPrestamoPremium):
        super().__init__(self.__historial, self.__productoPrestado, self.__fechaPrestamo, self.__fechaDevolucion)
        self.__idSocio = idSocio
        self.__duracionPrestamoPremium = duracionPrestamoPremium

        
    def aplica_descuento(self, producto):
        precioOriginal = producto.precio
        desc = precioOriginal * 0.20
        nuevoPrecio = precioOriginal - desc
        print(f"Socio {self.__idSocio} Ha obtenido un descuento de socio")
        print(f"precio original: {precioOriginal}, con descuento: {nuevoPrecio}")

        