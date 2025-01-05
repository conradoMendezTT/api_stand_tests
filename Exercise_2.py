# EJERCICIO 2: Crear una clase `Coche` y otra clase `Motor`.
# La clase `Coche` debe tener un atributo `motor` que sea una instancia de `Motor`.
# El `Motor` debe tener un atributo `potencia`.
# El método `arrancar` del `Coche` debe imprimir un mensaje que incluya la potencia del motor.

# - Define la clase `Motor` con un constructor que acepte `potencia`.
# - Define la clase `Coche` con un constructor que acepte una instancia de `Motor`.
# - Implementa un método `arrancar` en `Coche` que use la potencia del motor para imprimir "El coche ha arrancado con una potencia de [potencia] caballos."


class Coche:
    def __init__(self, potencia):
        self.motor = Motor(potencia)


    def arrancar(self):
       # potencia = self.motor
        print(f"El coche ha arrancado con una potencia de {self.motor.potencia} caballos.")

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia


coche_1 = Coche(1500)
coche_1.arrancar()

