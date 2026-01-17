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