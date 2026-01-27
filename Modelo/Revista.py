from Libro import Libro
class Revista(Libro):
    def __init__(self, regalo, marca):
        super().__init__(self.__ISBN, self.__editorial, self.__paginas, self.__autor)
        self.__regalo = regalo
        self.__marca = marca

    def regaloOfrecido(self):
        if self.__regalo == True:
             return f"Esta revista tiene regalo y es {self.__regalo}"
        else:
            return f"Esta revista no tiene regalo."