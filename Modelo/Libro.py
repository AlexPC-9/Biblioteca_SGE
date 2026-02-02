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
        
        return f"Libro: \n Autor : {self.__autor} \n Editorial: {self.__editorial} \n ISBN: {self.__ISBN} \n"
    
    def tipo_lectura(self):
                if self.__paginas > 500:
                    return "Lectura densa (más de 500 páginas)"
                else:
                    return "Lectura rápida"