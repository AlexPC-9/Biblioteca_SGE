from Libro import Libro
class LibroAnimado(Libro):
    def __init__(self, tipo, idioma):
        super().__init__(self.__ISBN, self.__editorial, self.__paginas, self.__autor)
        self.__tipo = tipo
        self.__idioma = idioma

    
    def apto_para_niños(self):
        if self.__tipo == "niños":
            print("Ideal para niños pequeños..")
        else:
            print("Apto para todas las edades.")