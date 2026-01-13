from Libro import Libro
class Periodico(Libro):
    def __init__(self, ubicacion, tipo):
        super().__init__(self.__ISBN, self.__editorial, self.__paginas, self.__autor)
        self.__ubicacion = ubicacion
        self.__tipo = tipo

    #GETTER SETTER
    