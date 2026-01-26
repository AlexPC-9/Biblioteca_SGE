from ContenidoMultimedia import ContenidoMultimedia

class Pelicula(ContenidoMultimedia):
    def __init__(self, reparto, director, ubicacion, calidadImagen):
        super().__init__(self.__tipo, self.__duracion, self.__calidadAudio)
        self.__reparto = reparto
        self.__director = director
        self.__ubicacion = ubicacion
        self.__calidadImagen = calidadImagen
        
    #GETTER Y SETTER
    def necesita_pantalla_4K(self):
        if self.__calidadImagen == "4K":
            return True
        else:
            return False