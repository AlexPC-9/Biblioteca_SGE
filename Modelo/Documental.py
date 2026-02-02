from .ContenidoMultimedia import ContenidoMultimedia

class Documental(ContenidoMultimedia):
   
    def __init__(self, categoria, antiguedad, fecha, precio, garantia, 
                 tipo, duracion, calidadAudio, 
                 enseñanza, ambientacion, calidadImagen):
        
       
        super().__init__(categoria, antiguedad, fecha, precio, garantia, tipo, duracion, calidadAudio)
    
        self.__enseñanza = enseñanza
        self.__ambientacion = ambientacion
        self.__calidadImagen = calidadImagen

    def __str__(self):
        return f"\n Documental: {self.__enseñanza} \n Calidad: {self.__calidadImagen}\n"