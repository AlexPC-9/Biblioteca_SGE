from Modelo.Libro import Libro

class LibroAnimado(Libro):
    def __init__(self, ISBN, editorial, paginas, autor, idioma, tipo="general"):
        super().__init__("Animado", 1, "2024", 12, "6 meses", ISBN, editorial, paginas, autor)
        
        self.__idioma = idioma
        self.__tipo = tipo 

    def apto_para_niños(self):
        if self.__tipo == "niños":
            return "Ideal para niños pequeños."
        else:
            return "Apto para todas las edades."