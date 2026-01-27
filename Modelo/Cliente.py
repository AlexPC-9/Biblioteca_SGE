from Modelo.Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, DNI, numTelefono, historial, productoPrestado, fechaPrestamo, fechaDevolucion):
      
        super().__init__(nombre, apellido, DNI, numTelefono)
        
        self.__historial = historial if historial is not None else []
        self.__productoPrestado = productoPrestado
        self.__fechaPrestamo = fechaPrestamo
        self.__fechaDevolucion = fechaDevolucion
    
    @property
    def historial(self):
        return self.__historial
    
    @property
    def historial(self):
        return self.__historial
    @property
    def productoPrestado(self):
        return self.__productoPrestado

    @property
    def fechaPrestamo(self):
        return self.__fechaPrestamo

    @property
    def fechaDevolucion(self):
        return self.__fechaDevolucion

    def toString(self):
        return (f"Nombre: {self.nombre}\n" 
                f"Historial: {self.__historial}\n")

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

    def toString(self): 
        return (f"Nombre: {self.nombre}\n" 
                f"Historial: {self.__historial}\n")