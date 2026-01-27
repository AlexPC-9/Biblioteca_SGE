from Modelo.Cliente import Cliente

class ClienteSocio(Cliente):
   
    def __init__(self, nombre, apellido, DNI, numTelefono, historial, prodPrestado, fechaPrest, fechaDev, idSocio, duracionPrestamoPremium):
        super().__init__(nombre, apellido, DNI, numTelefono, historial, prodPrestado, fechaPrest, fechaDev)
        self.__idSocio = idSocio
        self.__duracionPrestamoPremium = duracionPrestamoPremium

    def aplica_descuento(self, producto):
        precioOriginal = producto.precio
        desc = precioOriginal * 0.20
        nuevoPrecio = precioOriginal - desc
        print(f"\nSocio {self.__idSocio} ha obtenido un descuento del 20%")
        print(f" Precio original: {precioOriginal}€ \n Nuevo precio: {nuevoPrecio}€")