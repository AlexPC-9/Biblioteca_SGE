from .Producto import Producto

class Libro(Producto):
   
    def __init__(self, categoria, antiguedad, fecha, precio, garantia, ISBN, editorial, paginas, autor):

        super().__init__(categoria, antiguedad, fecha, precio, garantia)
        
       
        self.__ISBN = ISBN
        self.__editorial = editorial
        self.__paginas = paginas
        self.__autor = autor
    
    @property
    def autor(self):
        return self.__autor

    
    def __str__(self):
        
        return f"Libro: {self.__autor} | Editorial: {self.__editorial} | ISBN: {self.__ISBN}"
    
    def tipo_lectura(self):
                if self.__paginas > 500:
                    return "Lectura densa (más de 500 páginas)"
                else:
                    return "Lectura rápida"