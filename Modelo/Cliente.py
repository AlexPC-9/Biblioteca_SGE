from Persona import Persona

class Cliente(Persona):
    def __init__(self, historial, productoPrestado, fechaPrestamo, fechaDevolucion):
        super().__init__(self.__nombre, self.__apellido, self.__DNI, self.__numTelefono)
        self.__historial = []
        self.__productoPrestado = productoPrestado
        self.__fechaPrestamo = fechaPrestamo
        self.__fechaDevolucion = fechaDevolucion

    def escoger_producto(self, prod):
        self.__historial.append(prod)
        self.__productoPrestado = True
        print(f"El cliente ha comprado {prod}")

    def devolver_producto(self,prod):
        if(self.__productoPrestado):
            self.__productoPrestado = False
        else:
            print("Este cliente no tiene productos pendiente")

    def pagar(self, prod, cantidad):
        precio = prod.precio
        if(cantidad >= precio):
            print("Pago aceptado!")
        else:
            print("Pago rechazado, cantidad insuficiente")

    #Getter setter
    def toString():
        return(f"Nombre: {Persona.__nombre}\n" 
               f"Apellido: {Persona.__apellido}\n"
                f"Historial: {Cliente.__historial}\n"
               )
