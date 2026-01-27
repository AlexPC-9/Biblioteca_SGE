from .Libro import Libro

class Biblioteca:
    def __init__(self, nombreBiblioteca, ubicacionBiblioteca):
        self.__nombreBiblioteca = nombreBiblioteca
        self.__ubicacionBiblioteca = ubicacionBiblioteca
        self.inventario = []  
        self.usuarios = []

    # GETTERS Y SETTERS corregidos
    @property
    def nombreBiblioteca(self):
        return self.__nombreBiblioteca

    @nombreBiblioteca.setter
    def nombreBiblioteca(self, valor):
        self.__nombreBiblioteca = valor


    def __str__(self):
        return f"Biblioteca: {self.__nombreBiblioteca} | Ubicación: {self.__ubicacionBiblioteca}"

    def buscar_por_autor(self, autor_buscado):
        resultados = []
        for producto in self.inventario:
            if isinstance(producto, Libro):
                if producto.autor == autor_buscado:
                    resultados.append(producto)
        return resultados

    def realizar_prestamo(self, cliente, producto):
        if producto in self.inventario:
            cliente.escoger_producto(producto) 
            self.inventario.remove(producto)
            print(f"Préstamo realizado: {producto} entregado a {cliente.nombre}")
        else:
            print("Lo sentimos, el producto no está disponible.")