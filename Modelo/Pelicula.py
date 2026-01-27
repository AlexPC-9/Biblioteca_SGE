
from .ContenidoMultimedia import ContenidoMultimedia

class Pelicula(ContenidoMultimedia):
   
    def __init__(self, categoria, antiguedad, fecha, precio, garantia, 
                 tipo, duracion, calidadAudio, 
                 reparto, director, ubicacion, calidadImagen):
        
        super().__init__(categoria, antiguedad, fecha, precio, garantia, tipo, duracion, calidadAudio)
        
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
        

   
    def __str__(self):
        return f"Película: {self.__director} | Formato: {self.__calidadImagen} | Ubicación: {self.__ubicacion}"