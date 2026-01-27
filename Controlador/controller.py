from Modelo.ClienteInvitado import ClienteInvitado
from Modelo.Biblioteca import Biblioteca
from Modelo.Bibliotecario import Bibliotecario
from Modelo.ClienteSocio import ClienteSocio
from Modelo.Libro import Libro
from Modelo.Musica import Musica
from Modelo.Pelicula import Pelicula
from Modelo.Documental import Documental
from Vista import view

class controller:

    def inicio(self):
        view.imprimir("INICIO DE SESION, SELECCIONA TU USUARIO:\n")
        view.imprimir("1- Acceso Personal (Bibliotecario)")
        view.imprimir("2 - Acceso Usuario (Socio / Invitado)")
        perfil = input("Seleccione perfil")
        if perfil == "1":
            self.menu_bibliotecario()
        else:
            self.menu_usuarios()

    
    def menu_usuarios(self):
        view.imprimir("\n--- BIENVENIDO A LA BIBLIOTECA ---")
        es_socio = input("¿Eres socio? (s/n): ").lower()
    
        if es_socio == 's':
            self.menu_socio()
        else:
            self.menu_invitado()

    def menu_socio(self):

        socio_encontrado = None
        for persona in self.biblioteca.usuarios:
            if isinstance(persona, ClienteSocio):
                socio_encontrado = persona
                break
        if not socio_encontrado:
            view.imprimir("No hay ningún Socio registrado. El Bibliotecario debe ascender a alguien primero.")
            return

        while True:
            view.imprimir(f"\n--- MENÚ SOCIO DE {socio_encontrado.nombre} ---")
            view.imprimir("1 - Ver catálogo")
            view.imprimir("2 - Escoger producto (Añadir a Historial)")
            view.imprimir("3 - Devolver producto")
            view.imprimir("4 - Pagar")
            view.imprimir("5 - Aplicar Descuento")
            view.imprimir("6 - Ver mis datos (toString)")
            view.imprimir("7 - Salir")

            opc = input("Seleccione una opción: ")

            if opc == "1":
                for prod in self.biblioteca.inventario:
                    view.imprimir(str(prod))

            elif opc == "2":
                if self.biblioteca.inventario:
                    view.imprimir("\nSelecciona el producto que quieres comprar:")
                    for i, prod in enumerate(self.biblioteca.inventario):
                        view.imprimir(f"{i} - {prod}")
                    
                    seleccion = int(input("Introduce el número: "))
                    producto = self.biblioteca.inventario[seleccion]
                    socio_encontrado.escoger_producto(producto)
                else:
                    view.imprimir("Inventario vacío.")

            elif opc == "3":
                socio_encontrado.devolver_producto(None)

            elif opc == "4":
                if self.biblioteca.inventario:
                    producto = self.biblioteca.inventario[0]
                    monto = int(input(f"Precio: {producto.precio}. ¿Cuánto pagas?: "))
                    socio_encontrado.pagar(producto, monto)

            elif opc == "5":
                if self.biblioteca.inventario:
                    producto = self.biblioteca.inventario[0]
                    socio_encontrado.aplica_descuento(producto)

            elif opc == "6":
                view.imprimir(socio_encontrado.toString())

            elif opc == "7":
                break


    def menu_invitado(self):
        while True:
            view.imprimir("\n--- MENÚ INVITADO (Sólo Consulta) ---")
            view.imprimir("1 - Ver catálogo completo")
            view.imprimir("2 - Buscar por autor")
            view.imprimir("3 - Volver al inicio")

            opc = input("Seleccione una opción: ")
            if opc == "1":
                for item in self.biblioteca.inventario: 
                    view.imprimir(str(item))

            elif opc == "2":
                autor = input("Autor: ")
                res = self.biblioteca.buscar_por_autor(autor)
                for r in res: 
                    view.imprimir(str(r))

            elif opc == "3":
                break


    def menu_bibliotecario(self):
        while True:
                view.imprimir("--- PANEL DE CONTROL ---")
                view.imprimir("1 - Registrar nuevo Libro")
                view.imprimir("2 - Ascender Invitado a Socio")
                view.imprimir("3 - Actualizar Historial de Cliente")
                view.imprimir("4 - Ver Inventario Completo")
                view.imprimir("5 - Salir al Menú Principal")
                
                opc = input("Seleccione una opción: ")

                if(opc == "1"):
                        view.imprimir("\n--- FORMULARIO DE INSERCION DE LIBRO ---")
                        
                        categoria = input("Categoría (Novela, Ciencia, etc.): ")
                        antiguedad = int(input("Años de antigüedad: "))
                        fecha = input("Año de publicación: ")
                        precio = int(input("Precio de registro: "))
                        garantia = input("Descripción de la garantía: ")
                        isbn = input("Código ISBN: ")
                        editorial = input("Editorial: ")
                        paginas = int(input("Número de páginas: "))
                        autor = input("Nombre del Autor: ")
                        nuevo_libro = Libro(
                            categoria, antiguedad, fecha, precio, garantia, 
                            isbn, editorial, paginas, autor
                        )

                        self.bibliotecario.insertarLibros(self.biblioteca, nuevo_libro)
                        view.imprimir(f"Éxito: Se ha registrado '{autor}' en el sistema.")

                elif opc == "2":
                    
                    invitado = self.biblioteca.usuarios[0] 
                    if isinstance(invitado, ClienteInvitado):
                        nuevo_id = input("Asigna el ID de Socio: ")
                        nuevo_socio = self.bibliotecario.invitado_a_socio(invitado, nuevo_id)
                        self.biblioteca.usuarios.remove(invitado)
                        self.biblioteca.usuarios.append(nuevo_socio)
                    else:
                        view.imprimir("Ese usuario no es un invitado.")

                elif opc == "3":
                    cliente = self.biblioteca.usuarios[0]
                    producto = self.biblioteca.inventario[0]
                    self.bibliotecario.añadirHistorial(cliente, producto)

                elif opc == "4":
                    view.imprimir("\n--- MI INVENTARIO COMPLETO ---")
                    for item in self.biblioteca.inventario:
                        view.imprimir(str(item))

                elif opc == "5":
                    break

                else:
                     view.imprimir("Por favor, selecciona las opciones correctas.")

    
    
    def ejecutar_pruebas(self):
        self.bibliotecario = Bibliotecario("Luis", "Gonzales","547829475F", 3737474, 1,"Mañana")
        self.biblioteca = Biblioteca("Biblioteca Aranjuez", "Calle Infantas")
        print("--- SIMULACIÓN DE BIBLIOTECA ---\n")
        view.imprimir(f"Es la biblioteca: {self.biblioteca.nombreBiblioteca} \n")
        view.imprimir(f"El bibliotecario de esta biblioteca es: {self.bibliotecario.toString()}")
        

        
        libro1 = Libro("Novela", 2, "2024", 20, "2 años", "123-ABC", "Planeta", 350, "Cervantes")
        libro2 = Libro("Ciencia", 12, "2014", 15, "1 año", "456-DEF", "Anaya", 600, "Stephen Hawking")
        Musica1 = Musica("Rock", 1, "2020", 10, "1 año", "Digital", 300, "Estéreo", "Bon Jovi", "Slippery When Wet", False)
        peli1 = Pelicula("Cine", 5, "2019", 15, "2 años","DVD", 120, "Dolby Digital","Varios", "Spielberg", "Estante B", "4K")
        Doc = Documental("Cultura", 2, "2022", 10, "Sin garantía", "Streaming", 90, "Estéreo", "Edward Bella", "Spielberg", "4K")
        usuario_ejemplo = ClienteInvitado(nombre="Emily",apellido="Kady",DNI="12345678X",numTelefono="600123456",
    historial=[],prodPrestado=None,fechaPrest="---",fechaDev="---",idTemporal="001",  duracionPrestamo=7)

        socio = ClienteSocio("Alex", "Perez", "12345678X", "600123456", [], False, "---", "---", "SOCIO-001", 365)


        self.biblioteca.usuarios.append(usuario_ejemplo)
        self.biblioteca.inventario.append(libro1)
        self.biblioteca.inventario.append(libro2)
        self.biblioteca.inventario.append(peli1)
        self.biblioteca.inventario.append(Musica1)
        self.biblioteca.inventario.append(Doc)
        self.biblioteca.usuarios.append(socio)
        self.biblioteca.usuarios.append(usuario_ejemplo)

        self.inicio()

        # view.imprimir("--- MI INVENTARIO COMPLETO ---")
        # for item in self.biblioteca.inventario:
        #     view.imprimir(str(item))

        # #PRUEBAS
        # #buscando x cervantes
        # self.biblioteca.buscar_por_autor("Cervantes")
       

        # #probando ahora tipo lectura metodo
        # res2 = self.biblioteca.buscar_por_autor("Stephen Hawking")
        # for libro in res2:
        #     view.imprimir(f"encontrado {libro.autor}, y paginas {libro.tipo_lectura()}")

        



        