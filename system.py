import os

libros = []

class Libro:
    def __init__(self, codigo, titulo, apellido_autor, nombre_autor, area, publicador, estado="en sala"):
        self.codigo = codigo
        self.titulo = titulo
        self.apellido_autor = apellido_autor
        self.nombre_autor = nombre_autor
        self.area = area
        self.publicador = publicador
        self.estado = estado

    def __str__(self):
        return (f"Código: {self.codigo}\nTítulo: {self.titulo}\n"
                f"Autor: {self.nombre_autor} {self.apellido_autor}\n"
                f"Área: {self.area}\nPublicador: {self.publicador}\n"
                f"Estado: {self.estado}\n")

def guardar_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== AGREGAR NUEVO LIBRO ===")
    codigo = input("Código del libro: ")
    
    for libro in libros:
        if libro.codigo == codigo:
            print("¡Error! Ya existe un libro con ese código.")
            input("Presione Enter para continuar...")
            return
    
    titulo = input("Título: ")
    apellido_autor = input("Apellido del autor: ")
    nombre_autor = input("Nombre del autor: ")
    area = input("Área de conocimiento: ")
    publicador = input("Publicador: ")
    
    nuevo_libro = Libro(codigo, titulo, apellido_autor, nombre_autor, area, publicador)
    libros.append(nuevo_libro)
    print("\n¡Libro agregado con éxito!")
    input("Presione Enter para continuar...")

def modificar_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== MODIFICAR LIBRO ===")
    codigo = input("Ingrese el código del libro a modificar: ")
    
    encontrado = False
    for libro in libros:
        if libro.codigo == codigo:
            encontrado = True
            print("\nDatos actuales del libro:")
            print(libro)
            
            print("Ingrese los nuevos datos (deje en blanco para mantener el valor actual):")
            titulo = input(f"Nuevo título [{libro.titulo}]: ") or libro.titulo
            apellido_autor = input(f"Nuevo apellido del autor [{libro.apellido_autor}]: ") or libro.apellido_autor
            nombre_autor = input(f"Nuevo nombre del autor [{libro.nombre_autor}]: ") or libro.nombre_autor
            area = input(f"Nueva área de conocimiento [{libro.area}]: ") or libro.area
            publicador = input(f"Nuevo publicador [{libro.publicador}]: ") or libro.publicador
            estado = input(f"Nuevo estado [en sala/prestado] [{libro.estado}]: ") or libro.estado
            
            libro.titulo = titulo
            libro.apellido_autor = apellido_autor
            libro.nombre_autor = nombre_autor
            libro.area = area
            libro.publicador = publicador
            libro.estado = estado
            
            print("\n¡Libro modificado con éxito!")
            break
    
    if not encontrado:
        print("No se encontró un libro con ese código.")
    
    input("Presione Enter para continuar...")

def listar_libros():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== LISTADO DE LIBROS ===")
    
    if not libros:
        print("No hay libros registrados.")
    else:
        for i, libro in enumerate(libros, 1):
            print(f"Libro #{i}")
            print(libro)
            print("-" * 40)
    
    input("Presione Enter para continuar...")

def buscar_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== BUSCAR LIBRO ===")
    codigo = input("Ingrese el código del libro a buscar: ")
    
    encontrado = False
    for libro in libros:
        if libro.codigo == codigo:
            encontrado = True
            print("\nInformación del libro:")
            print(libro)
            break
    
    if not encontrado:
        print("No se encontró un libro con ese código.")
    
    input("Presione Enter para continuar...")

def eliminar_libro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== ELIMINAR LIBRO ===")
    codigo = input("Ingrese el código del libro a eliminar: ")
    
    encontrado = False
    for i, libro in enumerate(libros):
        if libro.codigo == codigo:
            encontrado = True
            print("\nLibro a eliminar:")
            print(libro)
            
            confirmacion = input("¿Está seguro que desea eliminar este libro? (s/n): ").lower()
            if confirmacion == 's':
                del libros[i]
                print("¡Libro eliminado con éxito!")
            else:
                print("Operación cancelada.")
            break
    
    if not encontrado:
        print("No se encontró un libro con ese código.")
    
    input("Presione Enter para continuar...")

def menu_principal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== SISTEMA DE BIBLIOTECA ===")
        print("1. Agregar libro")
        print("2. Modificar libro")
        print("3. Listar todos los libros")
        print("4. Buscar libro por código")
        print("5. Eliminar libro")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            guardar_libro()
        elif opcion == "2":
            modificar_libro()
        elif opcion == "3":
            listar_libros()
        elif opcion == "4":
            buscar_libro()
        elif opcion == "5":
            eliminar_libro()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    # Datos de ejemplo para prueba
   
    menu_principal()