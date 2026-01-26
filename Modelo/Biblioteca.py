from Biblioteca_SGE.Modelo import Libro


class Biblioteca:

    def __init__(self, nombreBiblioteca, ubicacionBiblioteca):
        self.__nombreBiblioteca = nombreBiblioteca
        self.__ubicacionBiblioteca = ubicacionBiblioteca
        self.inventario = []  
        self.usuarios = []


    #GETTER Y SETTER


    def mostrar_biblioteca(self):
        print(f"Biblioteca: {self.nombre_biblioteca}")
        print(f"Total de productos: {len(self.inventario)}")

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