class Biblioteca:
    def __init__(self):
        self.pila_libros = []

    def prestar_libro(self, libro):
        self.pila_libros.append(libro)
        print(f'Libro "{libro}" prestado con éxito.')

    def devolver_libro(self):
        if not self.pila_libros:
            print('La pila de libros está vacía. No hay libros para devolver.')
        else:
            libro_devuelto = self.pila_libros.pop()
            print(f'Libro "{libro_devuelto}" devuelto.')

    def mostrar_estado(self):
        if not self.pila_libros:
            print('La pila de libros está vacía.')
        else:
            print('Libros prestados:')
            for libro in reversed(self.pila_libros):
                print(f'- {libro}')

biblioteca = Biblioteca()

biblioteca.prestar_libro("Cien años de soledad")
biblioteca.prestar_libro("Don Quijote de la Mancha")

biblioteca.mostrar_estado()

biblioteca.devolver_libro()

biblioteca.mostrar_estado()
