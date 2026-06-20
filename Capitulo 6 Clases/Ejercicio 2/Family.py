#Crea Una Clases Que Almacena A Cada Integrante De La Familia.
class Familia:
     def __init__(self, Padre, Madre, *Hijos):
        self.Padre=Padre
        self.Madre=Madre
        self.Hijos=list(Hijos)