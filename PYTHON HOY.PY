class equipos:
    def _init_(self, forma, nombre, abreviación, simbolos, color):
        self.forma=forma
        self.nombre=nombre
        self.abreviación=abreviación
        self.simbolos=simbolos
        self.color=color
        
Barcelona = equipos("Poligono con curvas", "Barcelona", "FCB", "Balon y cruz", "azul, rojo, amarillo y dorado")

print(Barcelona.forma)
print(Barcelona.nombre)
print(Barcelona.abreviación)
print(Barcelona.simbolos)
print(Barcelona.color)