from Libro import Libro
class LibroAnimado(Libro):
    def __init__(self, tipo, idioma):
        super().__init__(self.__ISBN, self.__editorial, self.__paginas, self.__autor)
        self.__tipo = tipo
        self.__idioma = idioma