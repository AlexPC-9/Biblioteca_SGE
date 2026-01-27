from Modelo.ClienteSocio import ClienteSocio
from Modelo.Cliente import Cliente

class ClienteInvitado(Cliente):
    def __init__(self, nombre, apellido, DNI, numTelefono, historial, prodPrestado, fechaPrest, fechaDev, idTemporal, duracionPrestamo):
        super().__init__(nombre, apellido, DNI, numTelefono, historial, prodPrestado, fechaPrest, fechaDev)
        self.__idTemporal = idTemporal
        self.__duracionPrestamo = duracionPrestamo

    def convertir_Socio(self, nuevoIdSocio):
    
        nuevoSocio = ClienteSocio(
            self.nombre, 
            self.apellido,
            self.dni, 
            self.numTelefono,
            self.historial,
            self.productoPrestado,
            self.fechaPrestamo,
            self.fechaDevolucion,
            nuevoIdSocio,
            365  
        )
        print(f"{self.nombre} ha sido ascendido a SOCIO (ID: {nuevoIdSocio})")
        return nuevoSocio