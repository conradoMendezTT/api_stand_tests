# EJERCICIO 3: Crear dos clases: `Alumno` y `Curso`.
# La clase `Alumno` debe tener atributos `nombre` y `id`.
# La clase `Curso` debe tener un atributo `nombre` y una lista `alumnos`.
# Implementar un método `agregar_alumno` en `Curso` que añada instancias de `Alumno` a la lista.

# - Define la clase `Alumno` con un constructor que acepte `nombre` y `id`.
# - Define la clase `Curso` con un constructor que acepte `nombre` y una lista vacía de `alumnos`.
# - Implementa el método `agregar_alumno` que añada un objeto `Alumno` a la lista `alumnos`.
# - Implementa un método `listar_alumnos` que imprima los nombres de todos los alumnos en el curso.


class Alumno:
    def __init__(self, nombre , id):
        self.nombre = nombre
        self.id = id

class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.alumnos = []


    def agregar_alumnos(self , alumno):
        self.alumnos.append(alumno)

    def listar_alumnos(self):
        print(self.alumnos)


alumno_1 = Alumno("Conrado" , 1 )
curso_1 = Curso("Primer Curso creado")

curso_1_info = curso_1.agregar_alumnos(alumno_1)
print(f"Los alumnos agregados son {curso_1_info}")