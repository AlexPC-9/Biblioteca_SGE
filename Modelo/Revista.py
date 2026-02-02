from Modelo.Libro import Libro
from Modelo.Libro import Libro

class Revista(Libro):
   
    def __init__(self, ISBN, editorial, paginas, autor, regalo, marca):
        super().__init__("Revista", 0, "2024", 5, "N/A", ISBN, editorial, paginas, autor)
        
        self.__regalo = regalo
        self.__marca = marca

    def regaloOfrecido(self):
        if self.__regalo == True:
             return f"Esta revista tiene regalo y es {self.__regalo}"
        else:
            return f"Esta revista no tiene regalo."