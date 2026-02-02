from Modelo.Libro import Libro
class Periodico(Libro):
    def __init__(self, ISBN, editorial, paginas, autor, ubicacion, tipo):
        super().__init__("Periodico", 0, "2024", 5, "N/A", ISBN, editorial, paginas, autor)
        self.__ubicacion = ubicacion
        self.__tipo = tipo

