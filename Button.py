

class Button():
    width = 200
    height = 50


    def __init__(self, color, text ):
        self.btn_color = color
        self.btn_txt = text

boton_amarillo = Button("amarillo", "Comprar")
boton_rojo = Button("rojo", "Eliminar")

botones = [boton_rojo, boton_amarillo]


for button in botones:
    print(f"El ancho del boton es {button.width} y el color es {button.btn_color}")