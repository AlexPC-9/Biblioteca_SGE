from Modelo.Persona import Persona
from Modelo.Bibliotecario import Bibliotecario

class controller:
    def ejecutar_pruebas(self):
        print("--- SIMULACIÓN DE BIBLIOTECA ---\n")


        p1 = Persona("Ana", "García", "12345678Z", "600111222")
        print(p1.toString())
        b1 = Bibliotecario("Luis", "López", "87654321X", "699000111", "TR-001", "Tarde")
        print(b1.toString())
        print(f"\nModificando nombre de {b1.nombre}...")
        b1.nombre = "Luis Manuel" 
        print(f"Nuevo nombre: {b1.nombre}") 
    
        print("\n" + b1.toString())