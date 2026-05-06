#Crea Una Clases Que Almacena A Cada Integrante De La Familia.
class Familia:
      def __init__(self, Padre, Madre, *Hijos):
        self.Padre=Padre
        self.Madre=Madre
        self.Hijos=list(Hijos)
      #Hace Posible La Comparación Entre Clases.
      def __gt__(self, otra):
         return len(self.Hijos) > len(otra.Hijos)
      def __eq__(self, otra):
         return len(self.Hijos) == len(otra.Hijos)
      def __lt__(self, otra):
         return len(self.Hijos) < len(otra.Hijos)
    