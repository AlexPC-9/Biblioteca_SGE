# 📚 Sistema de Gestión de Biblioteca (POO Python)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![UML](https://img.shields.io/badge/UML-Diagram-blue?style=for-the-badge&logo=uml)

Este proyecto es una implementación completa en **Python** de un sistema de gestión de bibliotecas, desarrollado a partir de un modelado **UML**. El sistema permite gestionar de forma eficiente el inventario de productos multimedia y el flujo de usuarios (clientes y personal).

---

## 📋 Características Principales

* **🗂️ Jerarquía de Productos:** Gestión de materiales incluyendo libros, revistas, periódicos y contenido multimedia (música, películas y documentales).
* **👥 Gestión de Usuarios:** Sistema de roles que permite diferenciar entre clientes invitados y socios con beneficios.
* **💳 Sistema de Pagos:** Lógica integrada para procesar transacciones con cálculo automático de descuentos.
* **🔑 Rol del Bibliotecario:** Funciones administrativas para control de stock, actualización de historiales y gestión de membresías.

---

## 🛠️ Arquitectura del Software

El código aplica los pilares fundamentales de la **Programación Orientada a Objetos**:

| Pilar | Aplicación en el Proyecto |
| :--- | :--- |
| **Herencia** | Estructura piramidal desde las clases base `Producto` y `Persona`. |
| **Composición** | La clase `Biblioteca` centraliza y almacena todos los objetos del sistema. |
| **Polimorfismo** | El método `pagar()` se comporta de forma distinta según el tipo de cliente. |
| **Encapsulamiento** | Atributos protegidos y métodos específicos para la manipulación de datos. |



---

## 🚀 Organización de Clases

### 📦 Catálogo de Productos
Se divide en dos grandes ramas bajo la clase padre `Producto`:
* **Material Impreso:** `Libros`, `Revista`, `Periodico`.
* **Material Audiovisual:** `ContenidoMultimedia` → `Pelicula`, `Musica`, `Documental`.

### 👤 Gestión de Personas
Estructura basada en la clase padre `Persona`:
* **Clientes:** * `Invitado`: Usuarios temporales con opción de conversión.
    * `ClienteSocio`: Usuarios con beneficios y descuentos aplicados.
* **Staff:** * `PersonalB`: Bibliotecarios con permisos para insertar libros y gestionar socios.

---

## 💻 Ejemplo de Implementación

```python
# Ejemplo: Un bibliotecario convierte a un invitado en socio y este compra un libro
bibliotecario = PersonalB(nombre="Carlos", id_bibliotecario="B-01", turno="Mañana")
invitado = Invitado(nombre="Lucía", id_temp="T-505")

# Proceso de conversión
nuevo_socio = bibliotecario.invitado_a_socio(invitado, nuevo_id="S-100")

# Compra con descuento
libro = Libros(titulo="Don Quijote", precio=25.0)
precio_final = nuevo_socio.aplica_descuento(libro)
nuevo_socio.pagar(libro, precio_final)
