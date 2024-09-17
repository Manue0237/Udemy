import os
from pathlib import Path

# Función para limpiar la pantalla de la consola
def Limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Lee y muestra el contenido de una receta específica
def Leer_recetas(categoria, nombre_receta):
    try:
        archivo=open(Path(categoria) / nombre_receta, 'r')
        print(archivo.read())
    except FileNotFoundError:
        print("La receta no existe.")

# Crea una nueva receta en la categoría especificada
def Crear_Receta(categoria, nombre_receta, contenido):
    archivo=open(Path(categoria) / nombre_receta, 'w')
    archivo.write(contenido)
    print(f"Receta {nombre_receta} creada con éxito en {categoria}.")

# Elimina una receta existente en la categoría especificada
def Eliminar_receta(categoria, nombre_receta):
    try:
        os.remove(Path(categoria) / nombre_receta)
        print(f"Receta {nombre_receta} eliminada con éxito.")
    except FileNotFoundError:
        print("La receta no existe para eliminar.")

# Función principal que maneja el flujo del programa
def main():
    # Ruta base donde se encuentran las categorías de recetas
    ruta = Path('C:/Users/Manuel/Recetas')
    Limpiar_pantalla()
    while True:
        print("Directorio de recetas:")
        # Lista de categorías disponibles
        categorias = [categoria.name for categoria in ruta.iterdir() if categoria.is_dir()]
        
        # Muestra el menú de opciones
        print("\n1. Leer receta\n2. Crear receta\n3. Crear categoría\n4. Eliminar receta\n5. Eliminar categoría\n6. Salir")
        opcion = input("Elige una opción: ")
        
        # Opción para salir del programa
        if opcion == '6':
            break
        # Opciones para leer, crear y eliminar recetas
        elif opcion in ['1', '2', '4']:
            categoria = input("Elige una categoría: ")
            if categoria not in categorias:
                print("Categoría no existente.")
                continue
            
            if opcion == '1':
                nombre_receta = input("¿Qué receta quieres leer? ")
                Leer_recetas(Path(ruta,categoria), nombre_receta)
            elif opcion == '2':
                nombre_receta = input("Nombre de la nueva receta: ") + '.txt'
                contenido = input("Escribe el contenido de la receta: ")
                Crear_Receta(Path(ruta,categoria), nombre_receta, contenido)
            elif opcion == '4':
                nombre_receta = input("Nombre de la receta a eliminar: ")
                Eliminar_receta(Path(ruta,categoria), nombre_receta)

        # Opción para crear una nueva categoría
        elif opcion == '3':
            nueva_categoria = input("Nombre de la nueva categoría: ")
            os.makedirs(ruta / nueva_categoria, exist_ok=True)
            print(f"Categoría {nueva_categoria} creada con éxito.")
        # Opción para eliminar una categoría existente
        elif opcion == '5':
            eliminar_categoria = input("Nombre de la categoría a eliminar: ")
            os.rmdir(ruta / eliminar_categoria)
            print(f"Categoría {eliminar_categoria} eliminada con éxito.")

        # Pausa para que el usuario pueda leer la salida antes de continuar
        input("Presiona cualquier tecla para continuar...")
        Limpiar_pantalla()

# Punto de entrada del programa
if __name__ == "__main__":
    main()