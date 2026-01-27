class Producto:
    def __init__(self, categoria, antiguedad, fechaPublicacion, precio, garantia):
        self.__categoria = categoria
        self.__antiguedad = antiguedad
        self.__fechaPublicacion = fechaPublicacion
        self.__precio = precio
        self.__garantia = garantia
    
    @property
    def precio(self):
        return self.__precio  

    def calcular_precio_actual(self):
        if self.__antiguedad > 5:
            return self.__precio * 0.9
        return self.__precio


    def tiempo_estimado_lectura(self):
        minutos = self.__paginas * 2
        return f"Tiempo estimado: {minutos // 60} horas y {minutos % 60} minutos."