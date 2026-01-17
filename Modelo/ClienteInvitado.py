from Biblioteca_SGE.Modelo import ClienteSocio
from Cliente import Cliente

class ClienteInvitado(Cliente):
    def __init__(self, idTemporal, duracionPrestamo):
        super().__init__(self.__historial, self.__productoPrestado, self.__fechaPrestamo, self.__fechaDevolucion)
        self.__idTemporal = idTemporal
        self.__duracionPrestamo = duracionPrestamo

    #GETTER SETTER


    def convertir_Socio(self, nuevoIdSocio):
        nuevoSocio = ClienteSocio(
            id_socio=nuevoIdSocio,
            dur_prest_premium=365, 
            nombre=self.nombre,
            apellido=self.apellido,
            dni=self.dni,
            tel=self.tel,
            historial=self.historial,
            prod_prestado=self.prod_prestado,
            fecha_prest=self.fecha_prest,
            fecha_dev=self.fecha_dev
        )

        print(f"{self.nombre} ahora eres socio con ID: {nuevoIdSocio}")
        return nuevoSocio
    
    