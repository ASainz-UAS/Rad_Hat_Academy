#Crea Una Clase Que Captura Datos De Una Persona.
class Persona:
    def __init__(self, Nombre, Edad, Genero):
        self.Nombre=Nombre
        self.Edad=Edad
        self.Genero=Genero
    #gatter(Regresa Un Dato Guardado)
    def getter_Nombre(self):
        return self.Nombre
    def getter_Edad(self):
        return self.Edad
    def getter_Genero(self):
        return self.Genero