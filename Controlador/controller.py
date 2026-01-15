from Modelo.Persona import Persona
from Modelo.Bibliotecario import Bibliotecario

class controller:
    def ejecutar_pruebas(self):
        print("--- SIMULACIÓN DE BIBLIOTECA ---\n")

        # 1. Crear una Persona normal
        p1 = Persona("Ana", "García", "12345678Z", "600111222")
        print(p1.toString())

        # 2. Crear un Bibliotecario (pasa por Persona)
        b1 = Bibliotecario("Luis", "López", "87654321X", "699000111", "TR-001", "Tarde")
        print(b1.toString())

        # 3. Probar un Setter y un Getter (@property)
        print(f"\nModificando nombre de {b1.nombre}...")
        b1.nombre = "Luis Manuel" # Usa el @setter
        print(f"Nuevo nombre: {b1.nombre}") # Usa el @property
        
        print("\n" + b1.toString())