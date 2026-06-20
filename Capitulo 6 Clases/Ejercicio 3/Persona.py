#Crea Una Clase Que Captura Datos De Una Persona.
class Persona:
    def __init__(self, Nombre):
        self.Nombre=Nombre
    #gatter(Regresa Un Dato Guardado)
    def getter_Nombre(self):
        return self.Nombre
    