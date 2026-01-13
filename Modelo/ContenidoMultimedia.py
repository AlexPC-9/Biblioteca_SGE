from Producto import Producto
class ContenidoMultimedia(Producto):
    def __init__(self, tipo, duracion, calidadAudio):
        super().__init__(self.__categoria, self.__antiguedad, self.__fechaPublicacion, self.__precio, self.__garantia)
        self.__tipo = tipo
        self.__duracion = duracion
        self.__calidadAudio = calidadAudio
        
    #GETTER SETTER