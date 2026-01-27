from .ContenidoMultimedia import ContenidoMultimedia

class Musica(ContenidoMultimedia):
    def __init__(self, categoria, antiguedad, fecha, precio, garantia, 
                 tipo, duracion, calidadAudio, 
                 artista, album, es_single):
        
        super().__init__(categoria, antiguedad, fecha, precio, garantia, tipo, duracion, calidadAudio)
        
        self.__artista = artista
        self.__album = album
        self.__es_single = es_single

    def __str__(self):
        return f"Música: {self.__artista} - Álbum: {self.__album}"