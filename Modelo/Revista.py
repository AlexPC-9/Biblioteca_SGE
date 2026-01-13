from Libro import Libro
class Revista(Libro):
    def __init__(self, regalo, marca):
        super().__init__(self.__ISBN, self.__editorial, self.__paginas, self.__autor)
        self.__regalo = regalo
        self.__marca = marca

    #SUPER, GETTER Y SETTER