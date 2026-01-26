from Producto import Producto
class Musica(Producto):
    def __init__(self, cantantes, remix, single, album):
        super().__init__(self.__categoria, self.__antiguedad, self.__fechaPublicacion, self.__precio, self.__garantia)
        self.__cantantes = cantantes
        self.__remix = remix
        self.__single = single
        self.__album = album


    def detalle_artista(self):
        if self.__single == True:
            return f"Sencillo de {self.__cantantes}"
        else:
            return f"Álbum '{self.__album}' de {self.__cantantes}"