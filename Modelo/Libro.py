from Producto import Producto
class Libro(Producto):
    def __init__(self, ISBN, editorial, paginas, autor):
        super().__init__(self.__categoria, self.__antiguedad, self.__fechaPublicacion, self.__precio, self.__garantia)
        self.__ISBN= ISBN
        self.__editorial = editorial
        self.__paginas = paginas
        self.__autor = autor