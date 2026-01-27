from .Producto import Producto

class ContenidoMultimedia(Producto):

    def __init__(self, categoria, antiguedad, fecha, precio, garantia, tipo, duracion, calidadAudio):
        super().__init__(categoria, antiguedad, fecha, precio, garantia)
        
        # Guarda sus 3 datos
        self.__tipo = tipo
        self.__duracion = duracion
        self.__calidadAudio = calidadAudio
        
    #GETTER SETTER