# EJERCICIO 1: Crear una clase llamada `Persona` con los atributos `nombre` y `edad`.
# Agregar un método `saludar` que imprima un mensaje de saludo utilizando el nombre de la persona.

# - Define la clase `Persona` con un constructor que acepte `nombre` y `edad`.
# - Implementa un método `saludar` que imprima "Hola, mi nombre es [nombre] y tengo [edad] años."


class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(self.nombre)


    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")


# Implementacion

persona_1 = Persona("Conrado" , 25)

persona_1.saludar()